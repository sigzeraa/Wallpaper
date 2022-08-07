from ast import Try
from logging import error, exception
import os
from warnings import catch_warnings
import requests
import ctypes
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

user = os.getlogin()
url = "https://prnt.sc/123fds4"


try:
    r = requests.get(url)
    name = "C:\\Wallpaper\\background_image.png"

    file = open(name, "wb")
    file.write(r.content)
    file.close()
    PATH = os.path.abspath(name)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)

except:
    print("erro no user" + user)
    usuario = 'furukawateste@gmail.com'    
    me = 'furukawateste@gmail.com' 
    subject = ("Problema com Wallpaper " + user)
    mensagem = ("usuario com problema: " + user + "\n" + "ERRO: ")
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = usuario
    msg.preamble = "test" 
    msg.attach(MIMEText(mensagem))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user = 'furukawateste@gmail.com', password = 'ujofygpuuxbrnfod')
    s.sendmail(me, usuario, msg.as_string())
    s.quit()

    #ujofygpuuxbrnfod


