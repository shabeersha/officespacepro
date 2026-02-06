#!/usr/bin/env python3
"""
Generate Apple Touch Icon (180x180)
Creates a high-quality PNG icon for iOS home screen
"""

from PIL import Image, ImageDraw

def create_apple_touch_icon():
    """Create apple-touch-icon at 180x180"""
    size = 180
    
    # Create image with primary blue background
    img = Image.new('RGB', (size, size), (59, 130, 246))
    draw = ImageDraw.Draw(img)
    
    # White color for the icon
    white = (255, 255, 255)
    
    # Scale factors for better positioning
    padding = size * 0.15  # 15% padding on all sides
    icon_size = size - (2 * padding)
    
    # Calculate icon area
    left = padding
    top = padding
    right = size - padding
    bottom = size - padding
    
    # Draw apartment/building icon in white
    # Roof (triangle)
    roof_top = top + (icon_size * 0.15)
    roof_bottom = top + (icon_size * 0.35)
    roof_points = [
        (size * 0.5, roof_top),  # Top center
        (left, roof_bottom),  # Bottom left
        (right, roof_bottom),  # Bottom right
    ]
    draw.polygon(roof_points, fill=white)
    
    # Building body (rectangle)
    building_top = roof_bottom
    building_bottom = bottom
    draw.rectangle([left, building_top, right, building_bottom], fill=white)
    
    # Windows (blue rectangles - cutouts)
    window_width = icon_size * 0.15
    window_height = icon_size * 0.30
    window_y = building_top + (icon_size * 0.25)
    
    blue = (59, 130, 246)
    
    # Left window
    window1_x = left + (icon_size * 0.15)
    draw.rectangle([window1_x, window_y, window1_x + window_width, window_y + window_height], fill=blue)
    
    # Middle window
    window2_x = size * 0.5 - (window_width * 0.5)
    draw.rectangle([window2_x, window_y, window2_x + window_width, window_y + window_height], fill=blue)
    
    # Right window
    window3_x = right - (icon_size * 0.15) - window_width
    draw.rectangle([window3_x, window_y, window3_x + window_width, window_y + window_height], fill=blue)
    
    # Save PNG
    img.save('apple-touch-icon.png', 'PNG', optimize=True)
    print(f"✅ Created apple-touch-icon.png (180x180)")
    
    # Get file size
    import os
    file_size = os.path.getsize('apple-touch-icon.png')
    print(f"   File size: {file_size / 1024:.1f} KB")

# Create the icon
create_apple_touch_icon()
