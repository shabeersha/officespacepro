#!/usr/bin/env python3
"""
Update Favicon and OG Image URLs to Absolute URLs
Changes:
1. favicon.svg: /favicon.svg -> https://www.officespacepro.in/images/favicon.svg
2. favicon.ico: /favicon.ico -> https://www.officespacepro.in/images/favicon.ico
3. og:image: images/DSC06837.avif -> https://www.officespacepro.in/images/og.avif
4. twitter:image: images/DSC06837.avif -> https://www.officespacepro.in/images/og.avif
"""

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Updating {len(html_files)} HTML files with absolute URLs")

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update favicon.svg
    content = re.sub(
        r'<link rel="icon" type="image/svg\+xml" href="/favicon\.svg">',
        '<link rel="icon" type="image/svg+xml" href="https://www.officespacepro.in/images/favicon.svg">',
        content
    )
    
    # Update favicon.ico
    content = re.sub(
        r'<link rel="icon" type="image/x-icon" href="/favicon\.ico">',
        '<link rel="icon" type="image/x-icon" href="https://www.officespacepro.in/images/favicon.ico">',
        content
    )
    
    # Update og:image - handle both relative paths
    content = re.sub(
        r'<meta property="og:image" content="images/DSC06837\.avif"',
        '<meta property="og:image" content="https://www.officespacepro.in/images/og.avif"',
        content
    )
    
    # Also handle if it's already been changed to a different relative path
    content = re.sub(
        r'<meta property="og:image" content="(?!https://)[^"]*"',
        '<meta property="og:image" content="https://www.officespacepro.in/images/og.avif"',
        content
    )
    
    # Update twitter:image
    content = re.sub(
        r'<meta property="twitter:image" content="images/DSC06837\.avif"',
        '<meta property="twitter:image" content="https://www.officespacepro.in/images/og.avif"',
        content
    )
    
    # Also handle if it's already been changed to a different relative path
    content = re.sub(
        r'<meta property="twitter:image" content="(?!https://)[^"]*"',
        '<meta property="twitter:image" content="https://www.officespacepro.in/images/og.avif"',
        content
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {filename}")
    else:
        print(f"  - No changes needed for {filename}")

print("\n✅ All files updated with absolute URLs!")
