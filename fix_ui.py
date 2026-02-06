#!/usr/bin/env python3
"""
UI Fixes Script - Apply comprehensive UI improvements to all HTML pages
Fixes:
1. Footer layout redesign with background color
2. Mobile hamburger menu
3. Header spacing improvements
4. Breadcrumb spacing
5. Badge wrapping fixes
6. Gallery responsive grid
"""

import os
import re
from pathlib import Path

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Found {len(html_files)} HTML files to process")

for filename in html_files:
    print(f"\nProcessing: {filename}")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix 1: Update header height and add mobile menu button
    # Find the header tag and update height
    content = re.sub(
        r'(<header[^>]*class="[^"]*?)h-14 sm:h-16',
        r'\1h-16 sm:h-18',
        content
    )
    
    # Add mobile menu button after logo (before the nav element)
    if '<nav class="hidden md:flex' in content and 'id="mobile-menu-btn"' not in content:
        content = re.sub(
            r'(</a>\s*)(<!-- Navigation Menu -->)',
            r'''\1
                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="md:hidden p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors">
                    <span class="material-symbols-outlined">menu</span>
                </button>

                \2''',
            content
        )
    
    # Fix 2: Add mobile menu overlay (before closing body tag)
    if 'id="mobile-menu"' not in content:
        mobile_menu = '''
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="hidden fixed inset-0 bg-black/50 z-50 md:hidden">
        <div class="bg-white dark:bg-gray-900 w-80 h-full shadow-xl">
            <div class="flex items-center justify-between p-4 border-b dark:border-gray-700">
                <h2 class="text-lg font-bold">Menu</h2>
                <button id="mobile-menu-close" class="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <nav class="p-4">
                <a href="/index.html" class="block px-4 py-3 text-sm font-medium hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg mb-1">Home</a>
                
                <div class="mb-1">
                    <button class="mobile-dropdown-btn w-full flex items-center justify-between px-4 py-3 text-sm font-medium hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">
                        <span>Locations</span>
                        <span class="material-symbols-outlined text-sm">expand_more</span>
                    </button>
                    <div class="mobile-dropdown-content hidden pl-4 mt-1">
                        <a href="/office-space-kaloor-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Kaloor</a>
                        <a href="/office-space-thrippunithura-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Thrippunithura</a>
                        <a href="/premium-office-space-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Kochi Central</a>
                        <a href="/office-space-vyttila-junction-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Vyttila Junction</a>
                        <a href="/office-space-near-forum-mall-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Forum Mall</a>
                        <a href="/office-space-near-crowne-plaza-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Crowne Plaza</a>
                        <a href="/office-space-near-le-meridien-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Le Meridien</a>
                    </div>
                </div>
                
                <div>
                    <button class="mobile-dropdown-btn w-full flex items-center justify-between px-4 py-3 text-sm font-medium hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">
                        <span>Office Types</span>
                        <span class="material-symbols-outlined text-sm">expand_more</span>
                    </button>
                    <div class="mobile-dropdown-content hidden pl-4 mt-1">
                        <a href="/fully-furnished-office-kochi-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Fully Furnished</a>
                        <a href="/commercial-space-for-rent-kochi-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Commercial Space</a>
                        <a href="/office-for-rent-kochi-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Office for Rent</a>
                        <a href="/affordable-office-space-kochi-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Affordable</a>
                        <a href="/ready-to-move-office-kochi-kochi.html" class="block px-4 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg">Ready to Move</a>
                    </div>
                </div>
            </nav>
        </div>
    </div>

    <script>
        // Mobile menu toggle
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuClose = document.getElementById('mobile-menu-close');
        
        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('hidden');
            });
        }
        
        if (mobileMenuClose) {
            mobileMenuClose.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
            });
        }
        
        // Close on overlay click
        if (mobileMenu) {
            mobileMenu.addEventListener('click', (e) => {
                if (e.target === mobileMenu) {
                    mobileMenu.classList.add('hidden');
                }
            });
        }
        
        // Mobile dropdown toggles
        document.querySelectorAll('.mobile-dropdown-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const content = btn.nextElementSibling;
                const icon = btn.querySelector('.material-symbols-outlined');
                content.classList.toggle('hidden');
                icon.style.transform = content.classList.contains('hidden') ? 'rotate(0deg)' : 'rotate(180deg)';
            });
        });
    </script>
'''
        content = content.replace('</body>', mobile_menu + '\n</body>')
    
    # Fix 3: Add breadcrumb spacing (add mt-20 to breadcrumb nav)
    content = re.sub(
        r'(<nav class="[^"]*breadcrumb[^"]*")',
        r'<nav class="max-w-[1280px] mx-auto px-6 py-3 text-sm mt-20"',
        content
    )
    
    # Fix 4: Fix badge wrapping - add gap-y-3 to badge containers
    content = re.sub(
        r'(class="[^"]*flex[^"]*flex-wrap[^"]*gap-2)(")',
        r'\1 gap-y-3\2',
        content
    )
    
    # Fix 5: Footer redesign with background color and better layout
    # Find footer and replace entire footer section
    footer_pattern = r'<footer[^>]*>.*?</footer>'
    
    new_footer = '''<footer class="bg-gray-50 dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800 mt-16">
        <div class="max-w-[1280px] mx-auto px-6 py-12">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <!-- Brand Section (spans 2 columns) -->
                <div class="md:col-span-2">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="size-10 bg-primary rounded-lg flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-white text-xl">apartment</span>
                        </div>
                        <h3 class="text-xl font-bold">Office Space Pro</h3>
                    </div>
                    <p class="text-sm text-gray-600 dark:text-gray-400 max-w-md">
                        Specializing in premium, ready-to-move commercial office spaces for growing startups and established enterprises.
                    </p>
                </div>
                
                <!-- Popular Locations -->
                <div>
                    <h4 class="font-bold mb-4 text-gray-900 dark:text-white">Popular Locations</h4>
                    <ul class="space-y-2">
                        <li><a href="/office-space-kaloor-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Office Space Kaloor</a></li>
                        <li><a href="/office-space-thrippunithura-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Office Space Thrippunithura</a></li>
                        <li><a href="/office-space-vyttila-junction-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Office Space Vyttila</a></li>
                        <li><a href="/office-space-near-forum-mall-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Office near Forum Mall</a></li>
                        <li><a href="/premium-office-space-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Office Space Kochi</a></li>
                    </ul>
                </div>
                
                <!-- Office Types -->
                <div>
                    <h4 class="font-bold mb-4 text-gray-900 dark:text-white">Office Types</h4>
                    <ul class="space-y-2">
                        <li><a href="/fully-furnished-office-kochi-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Fully Furnished Office</a></li>
                        <li><a href="/commercial-space-for-rent-kochi-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Commercial Space</a></li>
                        <li><a href="/affordable-office-space-kochi-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Affordable Office</a></li>
                        <li><a href="/ready-to-move-office-kochi-kochi.html" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary transition-colors">Ready to Move Office</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-200 dark:border-gray-800 mt-8 pt-8 text-center">
                <p class="text-sm text-gray-500 dark:text-gray-400">© 2026 Office Space Pro . All rights reserved.</p>
            </div>
        </div>
    </footer>'''
    
    content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
    
    # Fix 6: Gallery grid - convert flex flex-col to grid for gallery sections
    # Find gallery containers and update them
    content = re.sub(
        r'(<div class="[^"]*)(flex flex-col gap-2)([^"]*"[^>]*>.*?<!-- Gallery images -->)',
        r'\1grid grid-cols-2 md:grid-cols-3 gap-2\3',
        content,
        flags=re.DOTALL
    )
    
    # Write back if changes were made
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {filename}")
    else:
        print(f"  - No changes needed for {filename}")

print(f"\n✅ Processed {len(html_files)} files successfully!")
