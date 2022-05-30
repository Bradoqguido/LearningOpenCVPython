from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

camera.start_preview()
raw_input(".")
camera.capture('images.png')
camera.stop_preview()

