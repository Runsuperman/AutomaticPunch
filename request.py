import random
import requests
import json


# 提交员工考勤
def submit(personId, time, address):
    url = "https://h5-40-hw.gaiaworkforce.com/api/deviceCloud/api/v1/deviceCloud/app/SubmitEmployeeAttendanceDataByMAP/greentown"
    gps = gps_info(personId)
    info = json.loads(gps)
    params = {
        'Longitude': info['longitude'],
        'Latitude': info['latitude'],
        'Address': address,
        'MachineID': info['MachineID'],
        'timeStamp': time.replace('-', '').replace(':', '').replace(' ', ''),
        'isNeedLocation': 'false',
        'serverTime': time,
        'personId': personId,
        'imageType': 'jpg',
        'hasImage': 1,
        'overTime': 30,
        'needApprove': 'true'
    }
    res = requests.post(url, json=params)
    imageKey = res.json()['data']['imageKey']
    return imageKey


def upload_img(imgBase64, imgKey, personId):
    url = 'https://h5-40-hw.gaiaworkforce.com/api/deviceCloud/api/v1/deviceCloud/app/uploadEmployeeAttendanceFile/greentown'
    pre = 'data:image/png;base64,'
    params = {
        'imageFile': pre + imgBase64,
        'imageKey': imgKey,
        'personId': personId
    }
    res = requests.post(url, json=params)
    print("上传图片请求：" + res.text)
    return res.text


def gps_info(personId):
    c = ''
    for i in range(8):
        c += str(random.randint(0, 9))
    longitude = '120.0737' + c
    latitude = '30.2912' + c
    # print(longitude + ":" + latitude)
    url = 'https://h5-40-hw.gaiaworkforce.com/api/deviceCloud/api/v1/deviceCloud/app/MatchOptimalLocationInfo/greentown'
    params = {
        'personId': personId,
        "locationInfo": [
            {
                "longitude": longitude,
                "latitude": latitude
            }
        ],
        "locationFlag": 1
    }
    res = requests.post(url, json=params)
    data = json.loads(res.text)['data']
    info = {
        "longitude": longitude,
        "latitude": latitude,
        'MachineID': data['MachineID']
    }
    print(info)
    return json.dumps(info)


