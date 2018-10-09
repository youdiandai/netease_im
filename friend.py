#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/6/20'
"""
from check_sum_headers import HeaderApi
import requests
from datetime import datetime, timedelta


class Friend(HeaderApi):

    def add(self, accid, faccid, type, **kwargs):
        """
        加好友
        :param accid:
        :param faccid:
        :param type(int):1直接加好友，2请求加好友，3同意加好友，4拒绝加好友
        :param msg:
        :return:
        """
        url = "https://api.netease.im/nimserver/friend/add.action"
        data = {"accid": accid, "faccid": faccid, 'type': type}
        if 'msg' in kwargs:
            data.__setitem__('msg', kwargs['msg'])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def update(self, accid, faccid, **kwargs):
        """
        更新好友相关信息
        :param accid:
        :param faccid:
        :param kwargs:alias:给好友增加备注名，限制长度128,ex:修改ex字段，限制长度256
        :return:
        """
        url = "https://api.netease.im/nimserver/friend/update.action"
        data = {"accid": accid, "faccid": faccid}
        if 'alias' in kwargs:
            data.__setitem__('alias', kwargs['alias'])
        if 'ex' in kwargs:
            data.__setitem__('ex', kwargs['ex'])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def delete(self, accid, faccid):
        """
        删除好友
        :param accid:
        :param faccid:
        :return:
        """
        url = "https://api.netease.im/nimserver/friend/delete.action"
        data = {"accid": accid, "faccid": faccid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def get(self, accid, updatetime, **kwargs):
        """
        查询某时间点起到现在有更新的双向好友
        :param accid:
        :param updatetime:更新时间戳，接口返回该时间戳之后有更新的好友列表
        :param kwargs:createtime(【Deprecated】定义同updatetime)
        :return:
        """
        url = "https://api.netease.im/nimserver/friend/get.action"
        data = {"accid": accid, "updatetime": updatetime}
        if 'createtime' in kwargs:
            data.__setitem__('createtime', kwargs['createtime'])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def setSpecialRelation(self, accid, targetAcc, relationType, value):
        """
        设置黑名单/静音
        :param accid:
        :param targetAcc:被加黑或加静音的帐号
        :param relationType(int):本次操作的关系类型,1:黑名单操作，2:静音列表操作
        :param value(int):操作值，0:取消黑名单或静音，1:加入黑名单或静音
        :return:
        """
        url = "https://api.netease.im/nimserver/user/setSpecialRelation.action"
        data = {"accid": accid, "targetAcc": targetAcc, 'relationType': relationType, 'value': value}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def listBlackAndMuteList(self, accid):
        """
        查看指定用户的黑名单和静音列表
        :param accid:
        :return:
        """
        url = "https://api.netease.im/nimserver/user/listBlackAndMuteList.action"
        data = {"accid": accid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()


if __name__ == '__main__':
    APPKEY = "4664d0724e7ae5c7d8637190975d960d"
    APP_SECRET = "f274d63943b1"
    friend = Friend(APPKEY, APP_SECRET)
    print("-" * 30)
    print('add:')
    response = friend.add('test3', 'test2', 1, msg='I want to be your friend')
    print(response)

    print("-" * 30)
    print('update:')
    response = friend.update('test3', 'test2', alias='test friend')
    print(response)

    print("-" * 30)
    print('delete:')
    response = friend.delete('test3', 'test2')
    print(response)
    response = friend.add('test3', 'test2', 1, msg='I want to be your friend')

    print("-" * 30)
    print('get:')
    response = friend.get(accid='test3', updatetime=str(int((datetime.now() - timedelta(minutes=5)).timestamp())))
    print(response)

    print("-" * 30)
    print('setSpecialRelation:')
    response = friend.setSpecialRelation('test3', 'test2', 1, 1)
    print(response)

    print("-" * 30)
    print('listBlackAndMuteList:')
    response = friend.listBlackAndMuteList('test3')
    print(response)
    response = friend.setSpecialRelation('test3', 'test2', 1, 0)


