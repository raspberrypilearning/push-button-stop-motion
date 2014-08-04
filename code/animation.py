import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
    camera.start_preview()
    frame = 1
    while True:
        GPIO.wait_for_edge(11, GPIO.FALLING)
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    camera.stop_preview()
