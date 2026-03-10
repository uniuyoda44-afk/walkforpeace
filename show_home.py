from PIL import Image
img = Image.open(r'c:\Users\Paulinus Kingsley\OneDrive\Apps\Walk for Peace\images\home.jpg')
print(img.format, img.size)
img.show()