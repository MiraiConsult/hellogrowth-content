#!/usr/bin/env python3
"""
Meta Ads Manager — Skill Script for Opensquad
Publishes and manages ads via Meta Marketing API v21.0
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

API_VERSION = "v21.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


def get_token():
    token = os.environ.get("META_ACCESS_TOKEN")
    if not token:
        print("ERROR: META_ACCESS_TOKEN not set. Add it to your .env file.")
        sys.exit(1)
    return token


def api_get(endpoint, params=None):
    token = get_token()
    params = params or {}
    params["access_token"] = token
    query = urllib.parse.urlencode(params)
    url = f"{BASE_URL}/{endpoint}?{query}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"ERROR {e.code}: {error_body}")
        sys.exit(1)


def api_post(endpoint, data=None, files=None):
    token = get_token()
    url = f"{BASE_URL}/{endpoint}"
    data = data or {}
    data["access_token"] = token

    if files:
        import mimetypes
        boundary = "----FormBoundary7MA4YWxkTrZu0gW"
        body = b""
        for key, value in data.items():
            body += f"--{boundary}\r\n".encode()
            body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode()
            body += f"{value}\r\n".encode()
        for key, filepath in files.items():
            filename = os.path.basename(filepath)
            mime = mimetypes.guess_type(filepath)[0] or "application/octet-stream"
            body += f"--{boundary}\r\n".encode()
            body += f'Content-Disposition: form-data; name="{key}"; filename="{filename}"\r\n'.encode()
            body += f"Content-Type: {mime}\r\n\r\n".encode()
            with open(filepath, "rb") as f:
                body += f.read()
            body += b"\r\n"
        body += f"--{boundary}--\r\n".encode()
        req = urllib.request.Request(url, data=body)
        req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    else:
        encoded = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=encoded)
        req.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"ERROR {e.code}: {error_body}")
        sys.exit(1)


def list_accounts():
    """List all ad accounts accessible with the current token."""
    result = api_get("me/adaccounts", {"fields": "name,account_id,account_status,currency,timezone_name"})
    accounts = result.get("data", [])
    if not accounts:
        print("No ad accounts found. Check your token permissions.")
        return
    print(f"Found {len(accounts)} ad account(s):\n")
    for acc in accounts:
        status = "ACTIVE" if acc.get("account_status") == 1 else "INACTIVE"
        print(f"  ID: act_{acc['account_id']}")
        print(f"  Name: {acc.get('name', 'N/A')}")
        print(f"  Status: {status}")
        print(f"  Currency: {acc.get('currency', 'N/A')}")
        print(f"  Timezone: {acc.get('timezone_name', 'N/A')}")
        print()


def create_campaign(account, name, objective, budget_type, budget):
    """Create a new campaign."""
    data = {
        "name": name,
        "objective": objective,
        "status": "PAUSED",
        "special_ad_categories": "[]",
    }
    if budget_type == "daily":
        data["daily_budget"] = str(int(budget))
    else:
        data["lifetime_budget"] = str(int(budget))

    result = api_post(f"{account}/campaigns", data)
    campaign_id = result.get("id")
    print(f"Campaign created successfully!")
    print(f"  ID: {campaign_id}")
    print(f"  Name: {name}")
    print(f"  Objective: {objective}")
    print(f"  Budget: {budget_type} R${budget/100:.2f}")
    print(f"  Status: PAUSED (activate when ready)")
    return campaign_id


def create_adset(campaign_id, name, budget, targeting_json, placements, optimization):
    """Create an ad set within a campaign."""
    targeting = json.loads(targeting_json) if isinstance(targeting_json, str) else targeting_json

    placement_map = {
        "instagram_feed": {"publisher_platforms": ["instagram"], "instagram_positions": ["stream"]},
        "instagram_stories": {"publisher_platforms": ["instagram"], "instagram_positions": ["story"]},
        "instagram_reels": {"publisher_platforms": ["instagram"], "instagram_positions": ["reels"]},
        "facebook_feed": {"publisher_platforms": ["facebook"], "facebook_positions": ["feed"]},
        "automatic": {},
    }
    if placements in placement_map and placement_map[placements]:
        targeting.update(placement_map[placements])

    data = {
        "name": name,
        "campaign_id": campaign_id,
        "daily_budget": str(int(budget)),
        "billing_event": "IMPRESSIONS",
        "optimization_goal": optimization,
        "targeting": json.dumps(targeting),
        "status": "PAUSED",
    }

    result = api_post(f"act_{campaign_id.split('_')[0]}/adsets" if "act_" not in campaign_id else f"{campaign_id}/adsets", data)
    adset_id = result.get("id")
    print(f"Ad Set created successfully!")
    print(f"  ID: {adset_id}")
    print(f"  Name: {name}")
    print(f"  Budget: daily R${budget/100:.2f}")
    print(f"  Optimization: {optimization}")
    return adset_id


def upload_image(account, filepath):
    """Upload an image to the ad account."""
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    result = api_post(f"{account}/adimages", files={"filename": filepath})

    images = result.get("images", {})
    for name, img_data in images.items():
        image_hash = img_data.get("hash")
        print(f"Image uploaded successfully!")
        print(f"  Hash: {image_hash}")
        print(f"  File: {filepath}")
        return image_hash

    print("ERROR: No image hash returned.")
    sys.exit(1)


def create_ad(adset_id, name, creative_type, images, primary_text, headline, description, cta, link):
    """Create an ad with creative."""
    if creative_type == "single":
        creative_data = {
            "object_story_spec": json.dumps({
                "page_id": os.environ.get("META_PAGE_ID", ""),
                "link_data": {
                    "image_hash": images.split(",")[0],
                    "link": link,
                    "message": primary_text,
                    "name": headline,
                    "description": description,
                    "call_to_action": {"type": cta},
                }
            })
        }
    elif creative_type == "carousel":
        image_hashes = images.split(",")
        headlines_list = headline.split("|") if "|" in headline else [headline] * len(image_hashes)
        child_attachments = []
        for i, img_hash in enumerate(image_hashes):
            h = headlines_list[i] if i < len(headlines_list) else headlines_list[-1]
            child_attachments.append({
                "image_hash": img_hash.strip(),
                "link": link,
                "name": h.strip(),
                "description": description,
                "call_to_action": {"type": cta},
            })
        creative_data = {
            "object_story_spec": json.dumps({
                "page_id": os.environ.get("META_PAGE_ID", ""),
                "link_data": {
                    "link": link,
                    "message": primary_text,
                    "child_attachments": child_attachments,
                }
            })
        }

    data = {
        "name": name,
        "adset_id": adset_id,
        "creative": json.dumps(creative_data),
        "status": "PAUSED",
    }

    result = api_post(f"act_placeholder/ads", data)
    ad_id = result.get("id")
    print(f"Ad created successfully!")
    print(f"  ID: {ad_id}")
    print(f"  Name: {name}")
    print(f"  Type: {creative_type}")
    print(f"  Status: PAUSED")
    return ad_id


def get_insights(object_id, metrics, date_range):
    """Get performance insights for a campaign, ad set, or ad."""
    range_map = {
        "today": {"since": "today", "until": "today"},
        "last_3d": {"date_preset": "last_3d"},
        "last_7d": {"date_preset": "last_7d"},
        "last_14d": {"date_preset": "last_14d"},
        "last_30d": {"date_preset": "last_30d"},
    }
    params = {"fields": metrics}
    if date_range in range_map:
        params.update(range_map[date_range])
    else:
        params["date_preset"] = "last_7d"

    result = api_get(f"{object_id}/insights", params)
    data = result.get("data", [])
    if not data:
        print("No insights data available yet. Wait 24-48h after ad starts running.")
        return

    print(f"Insights for {object_id}:\n")
    for row in data:
        for key, value in row.items():
            if key in ("date_start", "date_stop"):
                continue
            if isinstance(value, list):
                print(f"  {key}:")
                for item in value:
                    print(f"    - {item.get('action_type', 'N/A')}: {item.get('value', 'N/A')}")
            else:
                print(f"  {key}: {value}")
    print(f"\n  Period: {data[0].get('date_start', 'N/A')} to {data[0].get('date_stop', 'N/A')}")


def search_interests(query):
    """Search for targeting interests."""
    result = api_get("search", {"type": "adinterest", "q": query})
    interests = result.get("data", [])
    if not interests:
        print(f"No interests found for '{query}'")
        return

    print(f"Interests matching '{query}':\n")
    for interest in interests[:15]:
        audience = interest.get("audience_size_lower_bound", 0)
        audience_upper = interest.get("audience_size_upper_bound", 0)
        print(f"  ID: {interest['id']}")
        print(f"  Name: {interest['name']}")
        print(f"  Audience: {audience:,} - {audience_upper:,}")
        print(f"  Path: {' > '.join(interest.get('path', []))}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Meta Ads Manager for Opensquad")
    parser.add_argument("--action", required=True,
                       choices=["list-accounts", "create-campaign", "create-adset",
                               "upload-image", "create-ad", "get-insights", "search-interests"],
                       help="Action to perform")
    parser.add_argument("--account", help="Ad Account ID (act_XXXXXXX)")
    parser.add_argument("--campaign", help="Campaign ID")
    parser.add_argument("--adset", help="Ad Set ID")
    parser.add_argument("--name", help="Name for the object being created")
    parser.add_argument("--objective", help="Campaign objective")
    parser.add_argument("--budget-type", choices=["daily", "lifetime"], default="daily")
    parser.add_argument("--budget", type=int, help="Budget in cents (e.g., 5000 = R$50)")
    parser.add_argument("--targeting", help="Targeting JSON")
    parser.add_argument("--placements", default="instagram_feed",
                       choices=["instagram_feed", "instagram_stories", "instagram_reels",
                               "facebook_feed", "automatic"])
    parser.add_argument("--optimization", default="LINK_CLICKS")
    parser.add_argument("--file", help="File path for image upload")
    parser.add_argument("--creative-type", choices=["single", "carousel"], default="single")
    parser.add_argument("--images", help="Comma-separated image hashes")
    parser.add_argument("--primary-text", help="Primary text / caption")
    parser.add_argument("--headline", help="Ad headline (use | for carousel)")
    parser.add_argument("--description", help="Ad description")
    parser.add_argument("--cta", default="LEARN_MORE")
    parser.add_argument("--link", default="https://hellogrowth.site/")
    parser.add_argument("--object-id", help="Object ID for insights")
    parser.add_argument("--metrics", default="impressions,clicks,ctr,cpc,spend")
    parser.add_argument("--date-range", default="last_7d")
    parser.add_argument("--query", help="Search query for interests")

    args = parser.parse_args()

    if args.action == "list-accounts":
        list_accounts()
    elif args.action == "create-campaign":
        create_campaign(args.account, args.name, args.objective, args.budget_type, args.budget)
    elif args.action == "create-adset":
        create_adset(args.campaign, args.name, args.budget, args.targeting, args.placements, args.optimization)
    elif args.action == "upload-image":
        upload_image(args.account, args.file)
    elif args.action == "create-ad":
        create_ad(args.adset, args.name, args.creative_type, args.images,
                 args.primary_text, args.headline, args.description, args.cta, args.link)
    elif args.action == "get-insights":
        get_insights(args.object_id, args.metrics, args.date_range)
    elif args.action == "search-interests":
        search_interests(args.query)


if __name__ == "__main__":
    main()
