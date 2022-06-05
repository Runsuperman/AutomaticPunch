import json
import random
import time

import schedule as schedule

import request
import util


# if __name__ == '__main__':
def punch_job():
    address = '浙江省杭州市西湖区文一西路769'
    t = time.localtime()
    # print(time)
    day = str(t.tm_year) + "-" + str('%02d' % t.tm_mon) + "-" + str('%02d' % t.tm_mday)
    ms = str('%02d' % t.tm_hour) + ':' + str('%02d' % t.tm_min) + ':' + str('%02d' % t.tm_sec)
    ddd = str(t.tm_year) + str('%02d' % t.tm_mon) + str('%02d' % t.tm_mday)
    # print(ddd)
    dayType = util.holiday(str(t.tm_year) + str('%02d' % t.tm_mon) + str('%02d' % t.tm_mday))
    # dayType = "工作日"
    json_path = "./config.json"
    with open(json_path, 'r') as f:
        data = json.load(f)
    for i in data:
        personId = i['personId']
        print(personId)
        email_addr = i['email']
        name = i['name']
        code = i['code']
        if dayType == '非工作日':
            util.send_email("非工作日，今天不用打卡呦", email_addr)
        else:
            imgBase64 = util.water_mark(day, ms, address, name, code)
            # print(res)
            imageKey = request.submit(personId, day + ' ' + ms, address)
            print("imageKey:", imageKey)
            update_status = request.upload_img(imgBase64, imageKey, personId)
            if json.loads(update_status)['data'].__eq__("success"):
                util.send_email(name + "打卡成功，开启打工人新的一天", email_addr)
            else:
                util.send_email(name + "自动打卡失败", email_addr)

# dispatch = BlockingScheduler(timezone='Asia/Shanghai')
# # dispatch.add_job(punch_job, "cron", hour=20, minute=13, second=2)
# dispatch.add_job(punch_job, "interval ", second=2)
# # dispatch.add_job(punch_job, "cron", hour=18, minute=random.randint(10, 59), second=2)
# print("开始定时任务")
# dispatch.start()


if __name__ == '__main__':
    print("开始定时任务")
    m = str(random.randint(10, 40))
    s = str(random.randint(10, 59))
    schedule.every().day.at("08:" + m + ":" + s).do(punch_job)
    schedule.every().day.at("18:" + m + ":" + s).do(punch_job)
    while True:
        schedule.run_pending()   # 运行所有可以运行的任务
        time.sleep(1)
