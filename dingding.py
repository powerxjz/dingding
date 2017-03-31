import requests
import json
import time
api = 'https://oapi.dingtalk.com/robot/send?access_token=0ab814bf28690c5d997faca6f20f0651f09b9ac7d1facfd1c1d3de28739b0036'
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

context = {
    "msgtype": "text",
    "text":{
        "content":'业务测试，当前时间{}'.format(time.time())
    }
}
json_context = json.dumps(context)


send = requests.post(api,json_context,headers=headers)

print(send.text)