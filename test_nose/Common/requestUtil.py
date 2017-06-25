# coding: utf-8

import requests
import json

def sendRequest(url,header=''):
    response = requests.get(url,headers=header)
    content = json.loads(response.text)
    return content