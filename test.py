import json

from PIL import Image
import base64
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# img = open("temp_watermark.jpg", 'rb')
# res = base64.b64encode(img.read())
# print(res)
# img = Image.open("./img/wpeng.jpg.jpg")
# img.show()

# mail_host = 'smtp.qq.com'
# mail_user = '314093315@qq.com'
# mail_pass = 'vwwccxebrlqrbgeb'
#
# sender = '314093315@qq.com'
# receivers = ['wp_hyll@163.com']
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("314093315@qq.com", 'utf-8')
# message['To'] = Header("wp_hyll@163.com", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# smtpObj = smtplib.SMTP()
# smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
# smtpObj.login(mail_user, mail_pass)
# smtpObj.sendmail(sender, receivers, message.as_string())
# print("邮件发送成功")

path = "config.json"
with open(path, 'r') as f:
    data = json.load(f)
for i in data:
    print(i['personId'])


