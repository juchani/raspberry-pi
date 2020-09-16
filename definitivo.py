from gpiozero import MotionSensor, LED
from picamera import PiCamera
from time import sleep as t
import Adafruit_DHT
import yagmail
sensor = Adafruit_DHT.DHT11

pin = '21'

camara = PiCamera()
pir = MotionSensor(4)





while 1:
    print("Sensor pir {}".format(pir.value))
    if pir.value:
        camara.capture('/home/pi/s.jpg')
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        if humedad is not None and temperatura is not None:
            print('Temp={}*C  Humidity={}%'.format(temperatura, humedad))
        try:
            yag = yagmail.SMTP(user='victorfrancojuchani@gmail.com', password='zauwoczkofpfbsvt')
            yag.send(to='victorfrancojuchani@gmail.com', subject='Alarma Activada', contents='El sensor detecto movimiento,Temperatura {}*C Humedad {}%'.format(temperatura, humedad), attachments='/home/pi/s.jpg')
            print("El email fue enviado")
        except:
            print("Error, El correo no fue enviado")    
    t(3)