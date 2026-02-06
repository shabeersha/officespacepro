#!/usr/bin/env python3
"""
Fix Mobile Menu Button - Add hamburger menu button to header
"""

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Fixing mobile menu button in {len(html_files)} files")

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix 1: Update header height from h-14 sm:h-16 to h-16 sm:h-18
    content = re.sub(
        r'(<div class="max-w-\[1280px\] mx-auto px-4 sm:px-6 )h-14 sm:h-16',
        r'\1h-16 sm:h-18',
        content
    )
    
    # Fix 2: Add mobile menu button after the logo/title div and before nav
    # Look for the closing </div> after the title, then add button before <!-- Navigation Menu -->
    if 'id="mobile-menu-btn"' not in content:
        pattern = r'(</h1>\s*</div>)\s*(<!-- Navigation Menu -->)'
        replacement = r'''\1

            <!-- Mobile Menu Button -->
            <button id="mobile-menu-btn" class="md:hidden p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors" aria-label="Open menu">
                <span class="material-symbols-outlined">menu</span>
            </button>

            \2'''
        content = re.sub(pattern, replacement, content)
    
    # Fix 3: Gallery grid - find gallery containers more specifically
    # Look for the specific gallery div pattern
    content = re.sub(
        r'<div class="([^"]*?)flex flex-col gap-2([^"]*?)"([^>]*?)>\s*<!-- Gallery images -->',
        r'<div class="\1grid grid-cols-2 md:grid-cols-3 gap-2\2"\3>\n                <!-- Gallery images -->',
        content
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed {filename}")
    else:
        print(f"  - No changes for {filename}")

print("\n✅ Mobile menu button fix complete!")
