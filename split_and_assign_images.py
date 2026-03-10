from PIL import Image
import os

base = r"c:\Users\Paulinus Kingsley\OneDrive\Apps\Walk for Peace"
img_path = os.path.join(base, "walk.jpg")

img = Image.open(img_path)
print("Original size", img.size)

# compute grid splits (3x3)
width, height = img.size
cols, rows = 3, 3
cell_w = width // cols
cell_h = height // rows

out_dir = os.path.join(base, "images")
os.makedirs(out_dir, exist_ok=True)
filenames = [
    "home.jpg", "about.jpg", "join.jpg",
    "donate.jpg", "events.jpg", "contact.jpg",
    "thank_register.jpg", "stats.jpg", "thank_donate.jpg"
]

idx = 0
for r in range(rows):
    for c in range(cols):
        left = c * cell_w
        upper = r * cell_h
        right = left + cell_w if c < cols-1 else width
        lower = upper + cell_h if r < rows-1 else height
        cropped = img.crop((left, upper, right, lower))
        out_path = os.path.join(out_dir, filenames[idx])
        cropped.save(out_path)
        print("Saved", out_path)
        idx += 1

print("Cropped all images into", out_dir)
