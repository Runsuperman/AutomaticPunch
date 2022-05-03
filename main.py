import request
import util
import time
import json

if __name__ == '__main__':
    address = '浙江省杭州市西湖区蒋村街道文一西路757正绿城西溪国际'
    t = time.localtime()
    # print(time)
    day = str(t.tm_year) + "-" + str('%02d' % t.tm_mon) + "-" + str('%02d' % t.tm_mday)
    ms = str('%02d' % t.tm_hour) + ':' + str('%02d' % t.tm_min) + ':' + str('%02d' % t.tm_sec)
    ddd = str(t.tm_year) + str('%02d' % t.tm_mon) + str('%02d' % t.tm_mday)
    # print(ddd)
    dayType = util.holiday(str(t.tm_year) + str('%02d' % t.tm_mon) + str('%02d' % t.tm_mday))
    json_path = './config.json'
    with open(json_path, 'r') as f:
        data = json.load(f)
    for i in data:
        personId = i['personId']
        email_addr = i['email']
        name = i['name']
        code = i['code']
        if dayType == '非工作日':
            util.send_email("非工作日，今天不用打卡呦", email_addr)
        else:
            imgBase64 = util.water_mark(day, ms, address, name, code)
            # print(res)
            imageKey = request.submit(personId, day+' '+ms, address)
            update_status = request.upload_img(imgBase64, imageKey, personId)
            if json.loads(update_status)['data'].__eq__("success"):
                util.send_email(name + "打卡成功，开启打工人新的一天", email_addr)
            else:
                util.send_email(name + "自动打卡失败", email_addr)
