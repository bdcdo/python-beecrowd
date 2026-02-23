#!/usr/bin/env python3
"""Scrape all Beecrowd beginner problems HTML using Playwright."""
import json
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE_DIR = Path("/home/brunodcdo/Desktop/dev/2026/23_URI")
HTML_DIR = BASE_DIR / "html_raw"
PROBLEMS_FILE = BASE_DIR / "problems_list.json"

EMAIL = os.environ.get("BEECROWD_EMAIL", "")
SENHA = os.environ.get("BEECROWD_SENHA", "")


def login(page):
    print("[*] Navigating to login page...")
    page.goto("https://judge.beecrowd.com/pt/login", wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(3000)

    # Check if already logged in
    if "login" not in page.url:
        print("[+] Already logged in!")
        return True

    print("[*] Filling login form...")
    page.fill('input[name="email"]', EMAIL)
    page.fill('input[name="password"]', SENHA)
    page.click('button[type="submit"]')
    page.wait_for_timeout(5000)

    if "login" not in page.url:
        print("[+] Login successful!")
        return True
    else:
        print("[-] Login failed!")
        return False


def get_already_downloaded():
    """Return set of problem IDs already downloaded."""
    downloaded = set()
    if HTML_DIR.exists():
        for f in HTML_DIR.glob("*.html"):
            pid = f.stem
            # Check file is not empty
            if f.stat().st_size > 100:
                downloaded.add(pid)
    return downloaded


def scrape_problem(page, problem_id):
    """Navigate to problem page and extract iframe HTML."""
    url = f"https://judge.beecrowd.com/pt/problems/view/{problem_id}"
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(3000)

    # Find the iframe with the problem content
    for frame in page.frames:
        if "resources.beecrowd.com/repository/UOJ_" in frame.url:
            html = frame.content()
            return html

    # Retry with longer wait
    page.wait_for_timeout(3000)
    for frame in page.frames:
        if "resources.beecrowd.com/repository/UOJ_" in frame.url:
            html = frame.content()
            return html

    return None


def main():
    HTML_DIR.mkdir(parents=True, exist_ok=True)

    # Load problem list
    with open(PROBLEMS_FILE) as f:
        problems = json.load(f)

    # Check what's already downloaded
    downloaded = get_already_downloaded()
    remaining = [p for p in problems if p["id"] not in downloaded]

    print(f"[*] Total problems: {len(problems)}")
    print(f"[*] Already downloaded: {len(downloaded)}")
    print(f"[*] Remaining: {len(remaining)}")

    if not remaining:
        print("[+] All problems already downloaded!")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()

        # Login
        if not login(page):
            print("[-] Cannot proceed without login")
            browser.close()
            return

        # Scrape each problem
        success = 0
        failed = []
        for i, prob in enumerate(remaining):
            pid = prob["id"]
            name = prob["name"]
            print(f"[{i+1}/{len(remaining)}] Scraping {pid} - {name}...", end=" ", flush=True)

            try:
                html = scrape_problem(page, pid)
                if html:
                    out_path = HTML_DIR / f"{pid}.html"
                    out_path.write_text(html, encoding="utf-8")
                    print(f"OK ({len(html)} bytes)")
                    success += 1
                else:
                    print("FAILED (no iframe)")
                    failed.append(pid)
            except Exception as e:
                print(f"ERROR: {e}")
                failed.append(pid)
                # If too many errors, might need re-login
                if len(failed) > 5 and len(failed) > success * 0.1:
                    print("[!] Too many failures, attempting re-login...")
                    try:
                        login(page)
                    except:
                        pass

            # Small delay between requests
            time.sleep(0.5)

        browser.close()

    print(f"\n[*] Results: {success} success, {len(failed)} failed")
    if failed:
        print(f"[*] Failed IDs: {failed}")
        # Save failed list for retry
        with open(BASE_DIR / "failed_problems.json", "w") as f:
            json.dump(failed, f)


if __name__ == "__main__":
    main()
