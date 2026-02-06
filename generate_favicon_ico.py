#!/usr/bin/env python3
"""
Generate Favicon PNG files at different sizes
We'll create PNG files and then convert to ICO
"""

from PIL import Image, ImageDraw
import os

def create_favicon_png(size, filename):
    """Create a favicon PNG at the specified size"""
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Primary blue color
    blue = (59, 130, 246, 255)
    
    # Scale factors
    scale = size / 24
    
    # Draw apartment/building icon
    # Roof (triangle)
    roof_points = [
        (size * 0.5, size * 0.125),  # Top center
        (size * 0.083, size * 0.375),  # Bottom left
        (size * 0.917, size * 0.375),  # Bottom right
    ]
    draw.polygon(roof_points, fill=blue)
    
    # Building body (rectangle)
    building_left = size * 0.083
    building_top = size * 0.375
    building_right = size * 0.917
    building_bottom = size * 0.917
    draw.rectangle([building_left, building_top, building_right, building_bottom], fill=blue)
    
    # Windows (white rectangles)
    window_width = size * 0.125
    window_height = size * 0.25
    window_y = size * 0.5
    
    # Left window
    draw.rectangle([size * 0.208, window_y, size * 0.333, window_y + window_height], fill=(255, 255, 255, 255))
    # Middle window
    draw.rectangle([size * 0.438, window_y, size * 0.563, window_y + window_height], fill=(255, 255, 255, 255))
    # Right window
    draw.rectangle([size * 0.667, window_y, size * 0.792, window_y + window_height], fill=(255, 255, 255, 255))
    
    # Save PNG
    img.save(filename, 'PNG')
    print(f"Created {filename}")

# Create PNG files at different sizes
create_favicon_png(16, 'favicon-16x16.png')
create_favicon_png(32, 'favicon-32x32.png')
create_favicon_png(48, 'favicon-48x48.png')

# Now create the ICO file from the PNGs
try:
    img16 = Image.open('favicon-16x16.png')
    img32 = Image.open('favicon-32x32.png')
    img48 = Image.open('favicon-48x48.png')
    
    # Save as ICO with multiple sizes
    img48.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print("\n✅ Created favicon.ico with 16x16, 32x32, and 48x48 sizes")
    
    # Clean up PNG files
    os.remove('favicon-16x16.png')
    os.remove('favicon-32x32.png')
    os.remove('favicon-48x48.png')
    print("✅ Cleaned up temporary PNG files")
    
except Exception as e:
    print(f"Error creating ICO: {e}")
    print("PNG files have been created. You can use an online converter to create favicon.ico")
