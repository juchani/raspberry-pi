from gpiozero import MotionSensor, LED
from picamera import PiCamera
from time import sleep as t
import yagmail
camara = PiCamera()
pir = MotionSensor(4)

while 1:
    print("Sensor pir {}".format(pir.value))
    if pir.value:
        camara.capture('/home/pi/s.jpg')
        try:
            yag = yagmail.SMTP(user='victorfrancojuchani@gmail.com', password='zauwoczkofpfbsvt')
            yag.send(to='victorfrancojuchani@gmail.com', subject='Alarma Activada', contents='El sensor detecto movimiento', attachments='/home/pi/s.jpg')
            print("El email fue enviado")
        except:
            print("Error, El correo no fue enviado")    
    t(3)
