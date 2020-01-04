import os
import time
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


kamera_port = 0
kamera = cv2.VideoCapture(kamera_port)
time.sleep(1)  # Burada yarım saniyelik bir bekleme süresi ekliyoruz aksi takdirde resim karanlık çıkıyor.
return_value, image = kamera.read()
cv2.imwrite("kameragoruntusu.png", image)# kamera görüntüsü hangi isimle kaydedilsin?
del(kamera) #kamerayı serbest bırakıyoruz yoksa başka uygulamalar tarafından kullanılamıyor.
time.sleep(2) # mail aşamasına geçmeden önce 2 sn bekleme süresi ekliyoruz.



fromaddr = "s_____s@gmail.com"
toaddr = "______@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "mailin konusu (bilgisayar açıldı)"
body = "mailin içeriği - bilgisayarınız açıldı, kamera görüntüsü ekte"

msg.attach(MIMEText(body, 'plain'))
filename = "kameragoruntusu.png"
attachment = open(os.getcwd() + '/kameragoruntusu.png', "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "gönderici mailin şifresi")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()