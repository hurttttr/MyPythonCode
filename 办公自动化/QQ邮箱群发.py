from email.mime import base
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

my_mail = ''
key = ''

smtp_server = 'smtp.qq.com'

server = smtplib.SMTP(smtp_server)
server.connect(smtp_server, 25)
server.login(my_mail, key)

to_address = [
    '241778****@qq.com',
    '94539***0@qq.com'
]

for i in to_address:
    msg = MIMEMultipart()
    msg['From'] = Header('Python')  # 发件人
    msg['To'] = Header(i)  # 收件人
    msg['Subject'] = Header('test')  # 邮件标题

    part1 = MIMEText(open(r'QQ邮箱群发邮件\三国演义.txt', 'rb').read(),
                     'base64', 'utf-8')
    part1.add_header('Content-Disposition', 'attachment',
                     filename=('utf-8', '', '测试1.txt'))

    part2 = MIMEText(open(r'QQ邮箱群发邮件\test.docx', 'rb').read(),
                     'base64', 'utf-8')
    part2.add_header('Content-Disposition', 'attachment',
                     filename=('utf-8', '', '测试2.docx'))

    part3 = MIMEImage(open(r'QQ邮箱群发邮件\bird1.gif', 'rb').read())
    part3.add_header('Content-Disposition', 'attachment',
                     filename=('utf-8', '', '测试3.gif'))

    part4 = MIMEApplication(open(r'QQ邮箱群发邮件\牛牛.zip', 'rb').read())
    part4.add_header('Content-Disposition', 'attachment',
                     filename=('utf-8', '', '测试4.zip'))

    part5 = MIMEText('Test:send by Python', 'plain', 'utf-8')  # 正文

    msg.attach(part1)
    msg.attach(part2)
    msg.attach(part3)
    msg.attach(part4)
    msg.attach(part5)

    server.sendmail(my_mail, i, msg.as_string())
server.close()
