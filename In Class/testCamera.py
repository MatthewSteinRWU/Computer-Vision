import picamera
from time import sleep

# Take 5 images 5 seconds apart
camera = picamera.PiCamera()
for i in range(5):
    camera.capture('image%s.jpg' % i)
    sleep(5)
