from picamera import PiCamera
camara = PiCamera()

def captura():
    camara.capture('/home/pi/s.jpg')

captura()
