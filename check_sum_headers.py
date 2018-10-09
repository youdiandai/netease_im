#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用来创建带checksum等参数的http头部
包括AppKey,Nonce,CurTime,CheckSum,Content-Type

"""
import hashlib
import random
from datetime import datetime, timedelta


class CheckSumHeader(object):
    """
    生成一个用来给requests库用的头，携带网易云信需要的checksum函数
    """
    _Content_Type = "application/x-www-form-urlencoded;charset=utf-8"
    _str_num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, app_key, app_secret):
        self.App_key = app_key
        self.app_secret = app_secret
        self.curtime = self.get_CurTime()
        self.Nonce = self.get_random_num_str(30)

    def check_period(self, curtime):
        """
        检查checksum是否过期
        :return: True or False
        """
        five_min = timedelta(seconds=250)
        now = datetime.utcnow()
        if now - datetime.fromtimestamp(float(curtime)) > five_min:
            return False
        else:
            return True

    def update_curtime(self):
        """
        检查curtime参数是否过期
        :return:curtime
        """
        if not self.check_period(self.curtime):
            self.curtime = self.get_CurTime()
        return self.curtime

    def get_random_num_str(self, num):
        """
        获取一个随机数字符串
        :param num: 字符串长度
        :return: 随机字符串
        """
        nonce = ""
        for x in range(num):
            nonce += self._str_num_list[random.randint(0, 9)]
        self.Nonce = nonce
        return nonce

    @staticmethod
    def str_encrypt(str):
        """
        使用sha1加密算法，返回str加密后的字符串
        """
        sha = hashlib.sha1(str)
        encrypts = sha.hexdigest()
        return encrypts

    @staticmethod
    def get_CurTime():
        """
        获取当前时间戳的字符串形式
        :return:
        """
        return str(int(datetime.now().timestamp()))

    def get_checksum_headers(self):
        """
        获取带checksum，AppKey，Nonce，CurTime的头部字典
        :return:
        """
        CheckSum = self.str_encrypt((self.app_secret + self.Nonce + self.update_curtime()).encode('utf8'))
        return {"AppKey": self.App_key, \
                "Nonce": self.Nonce, \
                "CurTime": self.curtime, \
                "CheckSum": CheckSum, \
                "Content-Type": self._Content_Type}


class HeaderApi():
    def __init__(self, app_key, app_secret):
        self.header_seter = CheckSumHeader(app_key, app_secret)
        self.header = self.header_seter.get_checksum_headers()

    def get_header(self):
        self.header = self.header_seter.get_checksum_headers()
        return self.header

    def tran_boolean(self, bool):
        if bool:
            return "true"
        else:
            return "false"


if __name__ == '__main__':
    APPKEY = "APPKEY"
    APP_SECRET = "APP_SECRET"
    checksum_maker = CheckSumHeader(APPKEY, APP_SECRET)
    print(checksum_maker.get_checksum_headers())
