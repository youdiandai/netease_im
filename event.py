#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/6/20'
"""
from check_sum_headers import HeaderApi
import requests


class Event(object):
    def add(self, accid, eventType, publisherAccids, ttl):
        """
        在线状态
        :param accid:
        :param eventType:事件类型，固定设置为1，即 eventType=1
        :param publisherAccids:被订阅人的账号列表，最多100个账号，JSONArray格式。示例：["pub_user1","pub_user2"]
        :param ttl:有效期，单位：秒。取值范围：60～2592000（即60秒到30天）
        :return:
        """
        url = "https://api.netease.im/nimserver/event/subscribe/add.action"
        data = {'accid': accid, 'eventType': eventType, 'publisherAccids': publisherAccids, 'ttl': ttl}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def delete(self, accid, eventType, publisherAccids):
        """
        取消在线状态事件订阅
        :param accid:
        :param eventType:
        :param publisherAccids:
        :return:
        """
        url = "https://api.netease.im/nimserver/event/subscribe/delete.action"
        data = {'accid': accid, 'eventType': eventType, 'publisherAccids': publisherAccids}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def batchdel(self, accid, eventType):
        """
        取消全部在线状态事件订阅
        :param accid:
        :param eventType:事件类型，固定设置为1，即 eventType=1
        :return:
        """
        url = "https://api.netease.im/nimserver/event/subscribe/batchdel.action"
        data = {'accid': accid, 'eventType': eventType}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def query(self, accid, eventType, publisherAccids):
        """
        查询在线状态事件订阅关系
        :param accid:
        :param eventType:
        :param publisherAccids:
        :return:
        """
        url = "https://api.netease.im/nimserver/event/subscribe/query.action"
        data = {'accid': accid, 'eventType': eventType, 'publisherAccids': publisherAccids}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()
