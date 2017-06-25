# coding: utf-8

from Common.requestUtil import sendRequest
# from Common.log import log
# import logging

class testMyCase(object):
    def __init__(self):
        host = 'https://ruby-china.org'
        path = '/api/v3/topics?limit=1'
        self.url = host+path
        self.header = {'Content-Type':'Application/json', 'User-Agent':'Chrome'}
    def setUp(self):
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def testRCTitle(self):
        #发起请求得到返回
        response = sendRequest(self.url,header = self.header)
        #title = response['topics'][0]['title']
        print(response)
        #断言期望值
        #assert title == 'abc'