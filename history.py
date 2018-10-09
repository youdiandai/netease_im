#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/6/20'
"""
from check_sum_headers import HeaderApi
import requests


class History(HeaderApi):
    def querySessionMsg(self, _from, to, begintime, endtime, limit, **kwargs):
        """
        单聊云端历史消息查询
        :param _from:发送者accid
        :param to:接收者accid
        :param begintime:开始时间，ms
        :param endtime:截止时间，ms
        :param limit:本次查询的消息条数上限(最多100条),小于等于0，或者大于100，会提示参数错误
        :param kwargs:reverse:1按时间正序排列，2按时间降序排列。其它返回参数414错误.默认是按降序排列
                      type:查询指定的多个消息类型，类型之间用","分割，不设置该参数则查询全部类型消息格式示例： 0,1,2,3
                           类型支持： 1:图片，2:语音，3:视频，4:地理位置，5:通知，6:文件，10:提示，11:Robot，100:自定义
        :return:
        """
        url = "https://api.netease.im/nimserver/history/querySessionMsg.action"
        data = {'from': _from, 'to': to, 'begintime': begintime, 'endtime': endtime, 'limit': limit}
        for x in kwargs:
            data[x] = kwargs[x]
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queryTeamMsg(self, tid, accid, begintime, endtime, limit, **kwargs):
        """
        群聊云端历史消息查询
        :param tid:
        :param accid:查询用户对应的accid.
        :param begintime:开始时间，ms
        :param endtime:截止时间，ms
        :param limit:本次查询的消息条数上限(最多100条),小于等于0，或者大于100，会提示参数错误
        :param kwargs:reverse:1按时间正序排列，2按时间降序排列。其它返回参数414错误。默认是按降序排列
                      type:查询指定的多个消息类型，类型之间用","分割，不设置该参数则查询全部类型消息格式示例： 0,1,2,3
                           类型支持： 1:图片，2:语音，3:视频，4:地理位置，5:通知，6:文件，10:提示，11:Robot，100:自定义
        :return:
        """
        url = "https://api.netease.im/nimserver/history/queryTeamMsg.action"
        data = {'tid': tid, 'accid': accid, 'begintime': begintime, 'endtime': endtime, 'limit': limit}
        for x in kwargs:
            data[x] = kwargs[x]
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queryChatroomMsg(self, roomid, accid, timetag, limit, **kwargs):
        """
        聊天室云端历史消息查询
        :param roomid:
        :param accid:
        :param timetag:查询的时间戳锚点，13位。reverse=1时timetag为起始时间戳，reverse=2时timetag为终止时间戳
        :param limit:本次查询的消息条数上限(最多200条),小于等于0，或者大于200，会提示参数错误
        :param reverse:
        :param _type:
        :param kwargs:
        :return:
        """
        url = "https://api.netease.im/nimserver/history/queryChatroomMsg.action"
        data = {'roomid': roomid, 'accid': accid, 'timetag': timetag, 'limit': limit}
        for x in kwargs:
            data[x] = kwargs[x]
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def deleteHistoryMessage(self, roomid, fromAcc, msgTimetag):
        """
        删除聊天室云端历史消息
        :param roomid:
        :param fromAcc:消息发送者的accid
        :param msgTimetag:消息的时间戳，单位毫秒，应该拿到原始消息中的时间戳为参数
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/deleteHistoryMessage.action"
        data = {'roomid': roomid, 'fromAcc': fromAcc, 'msgTimetag': msgTimetag}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queryUserEvents(self, accid, begintime, endtime, limit, **kwargs):
        """
        用户登录登出事件记录查询
        :param accid:
        :param begintime:
        :param endtime:
        :param limit:本次查询的消息条数上限(最多100条),小于等于0，或者大于100，会提示参数错误
        :param kwargs:reverse:1按时间正序排列，2按时间降序排列。其它返回参数414错误。默认是按降序排列
        :return:
        """
        url = "https://api.netease.im/nimserver/history/queryUserEvents.action"
        data = {'accid': accid, 'begintime': begintime, 'endtime': endtime, 'limit': limit}
        if 'reverse' in kwargs:
            data['reverse'] = kwargs['reverse']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def deleteMediaFile(self, channelid):
        """
        删除音视频/白板服务器录制文件
        :param channelid:
        :return:
        """
        url = "https://api.netease.im/nimserver/history/deleteMediaFile.action"
        data = {'channelid': channelid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queryBroadcastMsg(self, **kwargs):
        """
        批量查询广播消息
        :param kwargs:broadcastId:查询的起始ID，0表示查询最近的limit条。默认0。
                      limit:查询的条数，最大100。默认100。
                      type:查询的类型，1表示所有，2表示查询存离线的，3表示查询不存离线的。默认1。
        :return:
        """
        url = "https://api.netease.im/nimserver/history/queryBroadcastMsg.action"
        data = {}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queryBroadcastMsgById(self, broadcastId):
        """
        查询单条广播消息
        :param broadcastId:
        :return:
        """
        url = "https://api.netease.im/nimserver/history/queryBroadcastMsgById.action"
        data = {'broadcastId': broadcastId}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()
