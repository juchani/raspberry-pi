import Adafruit_DHT
from time import sleep as t
sensor = Adafruit_DHT.DHT11
pin = '21'

    
    

    
while 1:
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    if humedad is not None and temperatura is not None:
        print('Temp={}*C  Humidity={}%'.format(temperatura, humedad))
   
    t(2)
