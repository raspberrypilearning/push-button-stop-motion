from picamzero import Camera
from time import sleep
from gpiozero import Button

button = Button(17)
cam = Camera()

cam.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        cam.take_photo(f'animation/frame{frame:03d}.jpg')
        frame += 1
    except KeyboardInterrupt:
        cam.stop_preview()
        break
