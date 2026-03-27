import random
from PIL import Image, ImageDraw
import os

def create_identicon(size=420, cells=5):
    background_color = (240, 240, 240)
    foreground_color = (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))
    
    img = Image.new('RGB', (size, size), background_color)
    draw = ImageDraw.Draw(img)
    
    cell_size = size // cells
    
    grid = []
    for _ in range(cells):
        row = [random.choice([True, False]) for _ in range((cells // 2) + 1)]
        mirrored_row = row + row[::-1][1:]
        grid.append(mirrored_row)

    for r in range(cells):
        for c in range(cells):
            if grid[r][c]:
                x0, y0 = c * cell_size, r * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                draw.rectangle([x0, y0, x1, y1], fill=foreground_color)

    return img

if __name__ == "__main__":
    try:
        user_choice = input("how many identicons to generate ")
        num_to_generate = int(user_choice)
        
        if num_to_generate <= 0:
            print("enter a number greater than 0")
            exit()
    except ValueError:
        print("enter a whole number")
        exit()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    output_folder = os.path.join(current_dir, "icons")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"created folder: {output_folder}")

    print(f"\ngenerating {num_to_generate} identicons")
    
    for i in range(num_to_generate):
        icon = create_identicon()
        filename = f"identicon_{i+1}.png"
        
        filepath = os.path.join(output_folder, filename)
        
        icon.save(filepath)
        print(f"saved: {filename} to /icons")

    print("\ndone!")
