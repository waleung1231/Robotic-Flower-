
import picamera
import time

# Initialize the camera
camera = picamera.PiCamera()

try:
    # Start preview for 10 seconds
    camera.start_preview()
    time.sleep(10)
    # Capture an image
    camera.capture('/home/pi/test_image.jpg')
    # Stop preview
    camera.stop_preview()

finally:
    # Release the camera resources
    camera.close()
