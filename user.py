#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用来进行网易云通信id的相关操作
"""
import requests
from check_sum_headers import HeaderApi
import json


class User(HeaderApi):

    def create(self, accid, **kwargs):
        """
        创建网易云通信ID
        :return:
        """
        url = "https://api.netease.im/nimserver/user/create.action"
        data = {"accid": accid}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def update(self, accid, token=None, **kwargs):
        """
        网易云通信ID更新
        :param accid:
        :param token:
        :param kwargs:json属性，第三方可选填，最大长度1024字符
        :return:
        """
        url = "https://api.netease.im/nimserver/user/update.action"
        data = {"accid": accid}
        if token is not None:
            data['token'] = token
        props = {}
        for x in kwargs:
            props.__setitem__(x, kwargs[x])
        if len(props) != 0:
            data['props'] = props
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def refresh_token(self, accid):
        """
        更新并获取新token
        :return:
        """
        url = "https://api.netease.im/nimserver/user/refreshToken.action"
        data = {"accid": accid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def block(self, accid, needkick=False):
        """
        封禁网易云通信ID
        :param accid:
        :param needkick:是否踢掉被禁用户，True or False
        :return:
        """
        url = "https://api.netease.im/nimserver/user/block.action"
        data = {"accid": accid}
        if needkick:
            data.__setitem__('needkick', 'true')
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def unblock(self, accid):
        """
        解禁网易云通信ID
        :return:
        """
        url = "https://api.netease.im/nimserver/user/unblock.action"
        data = {"accid": accid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def updateUinfo(self, accid, **kwargs):
        """
        更新用户名片
        :param accid:
        :param kwargs:name,icon,sign,email,birth,mobile,gender(int),ex(json)
        :return:
        """
        url = "https://api.netease.im/nimserver/user/updateUinfo.action"
        data = {"accid": accid}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def getUinfos(self, *accids):
        """
        获取用户名片(用户信息)
        :param accid:
        :return:
        """
        url = "https://api.netease.im/nimserver/user/getUinfos.action"
        data = {"accids": json.dumps([x for x in accids])}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def setDonnop(self, accid, donnopOpen):
        """
        设置桌面端在线时，移动端是否需要推送
        :param accid:
        :param donnopOpen:True:移动端不需要推送，False:移动端需要推送
        :return:
        """
        url = "https://api.netease.im/nimserver/user/setDonnop.action"
        data = {"accid": accid}
        if donnopOpen:
            data.__setitem__('donnopOpen', 'true')
        else:
            data.__setitem__('donnopOpen', 'false')
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()


if __name__ == '__main__':
    APPKEY = "APPKEY"
    APP_SECRET = "APP_SECRET"
    user = User(APPKEY, APP_SECRET)
    print("-" * 30)
    print('create:')
    response = user.create('test3')
    print(response)

    print("-" * 30)
    print('update:')
    response = user.update('test2')
    print(response)

    print("-" * 30)
    print('refresh_token:')
    response = user.refresh_token('test3')
    print(response)

    print("-" * 30)
    print('block:')
    response = user.block('test3')
    print(response)

    print("-" * 30)
    print('unblock:')
    response = user.unblock('test3')
    print(response)

    print("-" * 30)
    print('updateUinfo:')
    response = user.updateUinfo('test3', name='test', sign='test sign', email='test@test.com', birth='1999-09-09',
                                mobile='18515478511', gender=0)
    print(response)

    print("-" * 30)
    print('getUinfos:')
    response = user.getUinfos('test3', 'test2', 'test1')
    print(response)

    print("-" * 30)
    print('setDonnop:')
    response = user.setDonnop('test3', True)
    print(response)