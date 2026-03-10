from PIL import Image
import os

base = r"c:\Users\Paulinus Kingsley\OneDrive\Apps\Walk for Peace\images"
for f in os.listdir(base):
    if f.lower().endswith(('.jpg','.png')):
        path = os.path.join(base, f)
        print('Showing', f)
        img = Image.open(path)
        img.show()
