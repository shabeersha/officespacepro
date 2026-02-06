#!/usr/bin/env python3
"""
Add favicon.ico link to all HTML pages
"""

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Adding favicon.ico to {len(html_files)} files")

favicon_ico_link = '    <link rel="icon" type="image/x-icon" href="/favicon.ico">'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Check if favicon.ico already exists
    if 'favicon.ico' in content:
        print(f"  - favicon.ico already exists in {filename}")
        continue
    
    # Add favicon.ico link after the SVG favicon
    content = re.sub(
        r'(<link rel="icon" type="image/svg\+xml" href="/favicon\.svg">)',
        r'\1\n' + favicon_ico_link,
        content,
        count=1
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Added favicon.ico to {filename}")
    else:
        print(f"  - Could not add favicon.ico to {filename}")

print("\n✅ favicon.ico links added!")
