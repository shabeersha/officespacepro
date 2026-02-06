#!/usr/bin/env python3
"""
Add Apple Touch Icon link to all HTML pages
"""

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Adding apple-touch-icon to {len(html_files)} files")

apple_icon_link = '    <link rel="apple-touch-icon" href="https://www.officespacepro.in/images/apple-touch-icon.png">'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Check if apple-touch-icon already exists
    if 'apple-touch-icon' in content:
        print(f"  - apple-touch-icon already exists in {filename}")
        continue
    
    # Add apple-touch-icon link after the favicon.ico line
    content = re.sub(
        r'(<link rel="icon" type="image/x-icon" href="https://www\.officespacepro\.in/images/favicon\.ico">)',
        r'\1\n' + apple_icon_link,
        content,
        count=1
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Added apple-touch-icon to {filename}")
    else:
        print(f"  - Could not add apple-touch-icon to {filename}")

print("\n✅ Apple touch icon links added!")
