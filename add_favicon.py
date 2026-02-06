#!/usr/bin/env python3
"""
Add Favicon - Add favicon link to all HTML pages
"""

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Adding favicon to {len(html_files)} files")

favicon_link = '    <link rel="icon" type="image/svg+xml" href="/favicon.svg">'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Check if favicon already exists
    if 'favicon.svg' in content or '<link rel="icon"' in content:
        print(f"  - Favicon already exists in {filename}")
        continue
    
    # Add favicon link in the <head> section, right after the charset meta tag
    # Look for </title> tag and add after it
    content = re.sub(
        r'(</title>)',
        r'\1\n' + favicon_link,
        content,
        count=1
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Added favicon to {filename}")
    else:
        print(f"  - Could not add favicon to {filename}")

print("\n✅ Favicon setup complete!")
