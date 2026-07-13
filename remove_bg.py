import sys
from PIL import Image

def make_white_transparent(img_path):
    try:
        img = Image.open(img_path).convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            # Check if pixel is white or very close to white
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                # Make transparent
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(img_path, "PNG")
        print(f"Successfully processed {img_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    make_white_transparent("images/logo.png")
