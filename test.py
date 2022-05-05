import json
import random
import sched

from PIL import Image
import base64
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from apscheduler.schedulers.blocking import BlockingScheduler


# img = open("temp_watermark.jpg", 'rb')
# res = base64.b64encode(img.read())
# print(res)
# img = Image.open("./img/wpeng0.jpg.jpg")
# img.show()

# mail_host = 'smtp.qq.com'
# mail_user = '314093315@qq.com'
# mail_pass = 'vwwccxebrlqrbgeb'
#
# sender = '314093315@qq.com'
# receivers = ['1732218052@qq.com']
#
# message = MIMEText('测试发送', 'plain', 'utf-8')
# # message['From'] = Header("314093315@qq.com", 'utf-8')
# # message['To'] = Header("wp_hyll@163.com", 'utf-8')
#
# subject = '邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# smtpObj = smtplib.SMTP()
# smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
# smtpObj.login(mail_user, mail_pass)
# smtpObj.sendmail(sender, receivers, message.as_string())
# print("邮件发送成功")

# path = "config.json"
# with open(path, 'r') as f:
#     data = json.load(f)
# for i in data:
#     print(i['personId'])
# var = random.randint(0, 2)
# print(var)
# path = os.path.abspath(".")
def my_job():
    print("测试")


# sched = BlockingScheduler(timezone='Asia/Shanghai')
# sched.add_job(my_job, "cron", hour=11, minute=53, second=2)
# sched.start()
