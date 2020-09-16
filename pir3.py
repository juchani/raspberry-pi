from gpiozero import MotionSensor, LED
from time import sleep as t

pir = MotionSensor(4)

while 1:
    print(pir.value)
    t(3)
  

