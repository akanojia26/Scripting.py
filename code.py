from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.220',
    'username':'aditya',
    'password':'cisco',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show ip int brief')
print(output)



import csv
res = [output]
csvfile = "/root/python.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output,quotechar=' ', quoting=csv.QUOTE_ALL )
    writer.writerow(res)




import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

email_user = '**************@gmail.com'
email_send = '**************@gmail.com'

msg = MIMEMultipart()
filename='python.csv'
attachment =open(filename,'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= '+filename)
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'********')
server.sendmail(email_user,email_send,text)
server.quit()
