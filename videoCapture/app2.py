from PIL import Image
from pytesseract import *
import re
import cv2

num = int(6)
list = []

for i in range(num):
    print(i)
    img = Image.open('/Users/kimseonmin/Documents/pic'+str(i+1)+'.png')
    text = pytesseract.image_to_string(img,lang='kor')
    print(text)
    list.append(text)

print(list)
#img = Image.open('/Users/kimseonmin/Documents/pic7.png')
#text = pytesseract.image_to_string(img,lang='kor')

#print(text)
print("d")
#print(pytesseract.image_to_string(Image.open('/Users/kimseonmin/Documents/a.png'), lang='kor'))