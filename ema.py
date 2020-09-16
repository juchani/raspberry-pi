import yagmail

try:
    yag = yagmail.SMTP(user='victorfrancojuchani@gmail.com', password='zauwoczkofpfbsvt')
    yag.send(to='victorfrancojuchani@gmail.com', subject='Alarma Activada', contents='El sensor detecto movimiento', attachments='/home/pi/s.jpg')
    print("El email fue enviado")
except:
    print("Error, El email no fue enviado")
