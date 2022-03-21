from PIL import ImageGrab
import time

time.sleep(10)


for i in range(1, 11):
    img = ImageGrab.grab()
    img.save("./image_captured/img{idx}.jpg".format(idx=i))
    time.sleep(2)
