import os
from PIL import Image

assets_dir = r"d:\Aasteek\assets"
for filename in os.listdir(assets_dir):
    if filename.endswith(".png"):
        filepath = os.path.join(assets_dir, filename)
        print(f"Processing {filepath}...")
        img = Image.open(filepath).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            r, g, b, a = item
            # Soft feathering threshold for black background
            brightness = (r + g + b) / 3.0
            if brightness < 25:
                # Fade out dark pixels
                if brightness < 6:
                    newData.append((0, 0, 0, 0))
                else:
                    alpha = int(((brightness - 6) / 19.0) * 255)
                    newData.append((r, g, b, alpha))
            else:
                newData.append((r, g, b, a))
                
        img.putdata(newData)
        img.save(filepath, "PNG")
        print(f"Saved transparent version of {filename}")
