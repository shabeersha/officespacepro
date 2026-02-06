#!/usr/bin/env python3
"""
Remove Mobile Menu - Remove hamburger menu button and mobile menu overlay
"""

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Removing mobile menu from {len(html_files)} files")

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove mobile menu button
    content = re.sub(
        r'\s*<!-- Mobile Menu Button -->.*?</button>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    # Remove mobile menu overlay (everything from <!-- Mobile Menu Overlay --> to the closing script tag)
    content = re.sub(
        r'\s*<!-- Mobile Menu Overlay -->.*?</script>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Removed mobile menu from {filename}")
    else:
        print(f"  - No mobile menu found in {filename}")

print("\n✅ Mobile menu removal complete!")
