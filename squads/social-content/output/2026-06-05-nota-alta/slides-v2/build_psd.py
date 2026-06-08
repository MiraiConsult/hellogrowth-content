#!/usr/bin/env python3
"""Generate layered PSD files from carousel HTML slides."""
import struct
from PIL import Image
from psd_tools import PSDImage
from psd_tools.constants import ColorMode
import subprocess, os, json

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 1080, 1350

def render_html(html_path, png_path, width=W, height=H):
    subprocess.run([
        CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
        "--disable-software-rasterizer", "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--screenshot={png_path}", f"--window-size={width},{height}",
        f"file://{html_path}"
    ], capture_output=True)

def create_layer_html(base_dir, layer_name, css_body, html_content, bg="transparent"):
    """Create a temporary HTML with just one layer's content."""
    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; background: {bg}; font-family: 'Inter', sans-serif; overflow: hidden; letter-spacing: -0.02em; }}
{css_body}
</style></head><body>
{html_content}
</body></html>"""
    path = os.path.join(base_dir, f"_layer_{layer_name}.html")
    with open(path, "w") as f:
        f.write(html)
    return path

def make_psd_from_layers(layers, output_path, width=W, height=H):
    """
    Create a PSD with named layers from a list of (name, PIL.Image) tuples.
    Uses the flat composite as the merged image.
    """
    # Composite all layers bottom-to-top for the merged image
    merged = Image.new("RGBA", (width, height), (0,0,0,0))
    for name, img in layers:
        merged = Image.alpha_composite(merged, img.convert("RGBA"))

    # Create PSD
    psd = PSDImage.new("RGBA", (width, height))

    # Unfortunately psd-tools has limited layer creation.
    # We'll save as flattened PSD with the composite.
    merged_rgb = merged.convert("RGB")
    psd._record = None  # force fresh

    # Save the merged composite as PSD
    merged_rgb.save(output_path.replace('.psd', '_flat.psd'))

    return output_path

# Since psd-tools has limited programmatic layer creation,
# we'll use a raw PSD builder approach
def build_layered_psd(layers, output_path, width=W, height=H):
    """Build a PSD file with multiple layers using raw binary format."""
    from io import BytesIO

    def write_pascal_string(s):
        """Write a Pascal string (length-prefixed, padded to even)."""
        encoded = s.encode('ascii', errors='replace')
        length = len(encoded)
        data = struct.pack('B', length) + encoded
        if len(data) % 2 != 0:
            data += b'\x00'
        return data

    def get_channel_data(img, channel_idx):
        """Get raw channel data for a layer. channel_idx: 0=R, 1=G, 2=B, -1=A"""
        if channel_idx == -1:
            if img.mode == 'RGBA':
                return img.split()[3].tobytes()
            else:
                return bytes([255] * (img.width * img.height))
        else:
            bands = img.split()
            if channel_idx < len(bands):
                return bands[channel_idx].tobytes()
            return bytes([0] * (img.width * img.height))

    buf = BytesIO()

    # -- File Header --
    buf.write(b'8BPS')  # Signature
    buf.write(struct.pack('>H', 1))  # Version
    buf.write(b'\x00' * 6)  # Reserved
    buf.write(struct.pack('>H', 4))  # Channels (RGBA)
    buf.write(struct.pack('>I', height))  # Height
    buf.write(struct.pack('>I', width))  # Width
    buf.write(struct.pack('>H', 8))  # Bits per channel
    buf.write(struct.pack('>H', 3))  # Color mode (RGB)

    # -- Color Mode Data --
    buf.write(struct.pack('>I', 0))

    # -- Image Resources --
    buf.write(struct.pack('>I', 0))

    # -- Layer and Mask Information --
    layer_buf = BytesIO()

    # Layer Info
    layer_info_buf = BytesIO()
    layer_info_buf.write(struct.pack('>h', len(layers)))  # Layer count

    # Channel image data for each layer
    channel_datas = []
    for name, img in layers:
        img = img.convert('RGBA')
        t, l, b, r = 0, 0, img.height, img.width

        layer_info_buf.write(struct.pack('>i', t))  # Top
        layer_info_buf.write(struct.pack('>i', l))  # Left
        layer_info_buf.write(struct.pack('>i', b))  # Bottom
        layer_info_buf.write(struct.pack('>i', r))  # Right

        num_channels = 4
        layer_info_buf.write(struct.pack('>H', num_channels))

        # Channel info (A, R, G, B)
        ch_ids = [-1, 0, 1, 2]
        ch_raw = []
        for ch_id in ch_ids:
            raw = get_channel_data(img, ch_id)
            compressed = struct.pack('>H', 0) + raw  # 0 = raw compression
            ch_raw.append(compressed)
            layer_info_buf.write(struct.pack('>h', ch_id))
            layer_info_buf.write(struct.pack('>I', len(compressed)))

        channel_datas.append(ch_raw)

        # Blend mode signature
        layer_info_buf.write(b'8BIM')
        layer_info_buf.write(b'norm')  # Normal blend
        layer_info_buf.write(struct.pack('B', 255))  # Opacity
        layer_info_buf.write(struct.pack('B', 0))  # Clipping
        layer_info_buf.write(struct.pack('B', 1))  # Flags (visible)
        layer_info_buf.write(struct.pack('B', 0))  # Filler

        # Extra data
        extra_buf = BytesIO()
        # Layer mask data
        extra_buf.write(struct.pack('>I', 0))
        # Layer blending ranges
        extra_buf.write(struct.pack('>I', 0))
        # Layer name (Pascal string)
        extra_buf.write(write_pascal_string(name))
        # Pad to multiple of 4
        while extra_buf.tell() % 4 != 0:
            extra_buf.write(b'\x00')

        extra_data = extra_buf.getvalue()
        layer_info_buf.write(struct.pack('>I', len(extra_data)))
        layer_info_buf.write(extra_data)

    # Write channel image data
    for ch_raw in channel_datas:
        for compressed in ch_raw:
            layer_info_buf.write(compressed)

    layer_info_data = layer_info_buf.getvalue()
    # Pad to even
    if len(layer_info_data) % 2 != 0:
        layer_info_data += b'\x00'

    layer_buf.write(struct.pack('>I', len(layer_info_data)))
    layer_buf.write(layer_info_data)

    # Global layer mask info
    layer_buf.write(struct.pack('>I', 0))

    layer_data = layer_buf.getvalue()
    buf.write(struct.pack('>I', len(layer_data)))
    buf.write(layer_data)

    # -- Image Data (merged composite) --
    merged = Image.new("RGBA", (width, height), (0,0,0,0))
    for name, img in layers:
        merged = Image.alpha_composite(merged, img.convert("RGBA"))

    buf.write(struct.pack('>H', 0))  # Raw compression
    for ch in [0, 1, 2, 3]:  # R, G, B, A
        buf.write(merged.split()[ch].tobytes())

    with open(output_path, 'wb') as f:
        f.write(buf.getvalue())

    return output_path

print("PSD builder ready")
