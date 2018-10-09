#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/6/20'
"""
from check_sum_headers import HeaderApi
from msg import Msg
import requests
import json


class Team(HeaderApi):
    def create(self, tname, owner, members, msg, magree, joinmode, **kwargs):
        """
        创建群
        :param tname:群名称，最大长度64字符
        :param owner:群主用户帐号accid，最大长度32字符
        :param members:["aaa","bbb"](JSONArray对应的accid，如果解析出错会报414)，一次最多拉200个成员
        :param msg:邀请发送的文字，最大长度150字符
        :param magree:管理后台建群时，0不需要被邀请人同意加入群，1需要被邀请人同意才可以加入群。其它会返回414
        :param joinmode:群建好后，sdk操作时，0不用验证，1需要验证,2不允许任何人加入。其它返回414
        :param kwargs:announcement:群公告，最大长度1024字符
                      intro:群描述，最大长度512字符
                      custom:自定义高级群扩展属性，第三方可以跟据此属性自定义扩展自己的群属性。（建议为json）,最大长度1024字符
                      icon:群头像，最大长度1024字符
                      beinvitemode:被邀请人同意方式，0-需要同意(默认),1-不需要同意。其它返回414
                      invitemode:谁可以邀请他人入群，0-管理员(默认),1-所有人。其它返回414
                      uptinfomode:谁可以修改群资料，0-管理员(默认),1-所有人。其它返回414
                      upcustommode:谁可以更新群自定义属性，0-管理员(默认),1-所有人。其它返回414
        :return:
        """
        url = "https://api.netease.im/nimserver/team/create.action"
        data = {"tname": tname, 'owner': owner, 'members': members, 'msg': msg, 'magree': magree, 'joinmode': joinmode}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def add(self, tid, owner, members, magree, msg, **kwargs):
        """
        拉人入群
        :param tid:
        :param owner:
        :param members:["aaa","bbb"](JSONArray对应的accid，如果解析出错会报414)，一次最多拉200个成员
        :param magree:管理后台建群时，0不需要被邀请人同意加入群，1需要被邀请人同意才可以加入群。其它会返回414
        :param msg:邀请发送的文字，最大长度150字符
        :param kwargs:attach:自定义扩展字段，最大长度512
        :return:
        """
        url = "https://api.netease.im/nimserver/team/add.action"
        data = {"tid": tid, 'owner': owner, 'members': members, 'msg': msg, 'magree': magree}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def kick(self, tid, owner, **kwargs):
        """
        踢人出群
        :param tid:网易云通信服务器产生，群唯一标识，创建群时会返回，最大长度128字符
        :param owner:群主的accid，用户帐号，最大长度32字符
        :param kwargs:member:被移除人的accid，用户账号，最大长度32字符;注：member或members任意提供一个，优先使用member参数
                      members:["aaa","bbb"]（JSONArray对应的accid，如果解析出错，会报414）一次最多操作200个accid; 注：member或members任意提供一个，优先使用member参数
                      attach:自定义扩展字段，最大长度512
        :return:
        """
        url = "https://api.netease.im/nimserver/team/kick.action"
        data = {"tid": tid, 'owner': owner}
        if not 'member' in kwargs:
            if 'members' in kwargs:
                data['members'] = kwargs['members']
        else:
            data['member'] = kwargs['member']
        if 'attach' in kwargs:
            data['attach'] = kwargs['attach']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def remove(self, tid, owner):
        """
        解散群
        :param tid:
        :param owner:
        :return:
        """
        url = "https://api.netease.im/nimserver/team/remove.action"
        data = {"tid": tid, 'owner': owner}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def update(self, tid, owner, **kwargs):
        """
        编辑群资料
        :param tid:
        :param owner:
        :param kwargs:tname:群名称，最大长度64字符
                      announcement:群公告，最大长度1024字符
                      intro:群描述，最大长度512字符
                      joinmode:群建好后，sdk操作时，0不用验证，1需要验证,2不允许任何人加入。其它返回414
                      custom:自定义高级群扩展属性，第三方可以跟据此属性自定义扩展自己的群属性。（建议为json）,最大长度1024字符
                      icon:群头像，最大长度1024字符
                      beinvitemode:被邀请人同意方式，0-需要同意(默认),1-不需要同意。其它返回414
                      invitemode:谁可以邀请他人入群，0-管理员(默认),1-所有人。其它返回414
                      uptinfomode:谁可以修改群资料，0-管理员(默认),1-所有人。其它返回414
                      upcustommode:谁可以更新群自定义属性，0-管理员(默认),1-所有人。其它返回414
        :return:
        """
        url = "https://api.netease.im/nimserver/team/update.action"
        data = {"tid": tid, 'owner': owner}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def query(self, tids, ope):
        """
        群信息与成员列表查询
        :param tids:群id列表，如["3083","3084"]
        :param ope:1表示带上群成员列表，0表示不带群成员列表，只返回群信息
        :return:
        """
        url = "https://api.netease.im/nimserver/team/query.action"
        data = {"tids": tids, 'ope': ope}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def getMarkReadInfo(self, tid, msgid, fromAccid, **kwargs):
        """
        获取群组已读消息的已读详情信息
        :param tid:
        :param msgid:发送群已读业务消息时服务器返回的消息ID
        :param fromAccid:消息发送者账号
        :param kwargs:snapshot:是否返回已读、未读成员的accid列表，默认为false
        :return:
        """
        url = "https://api.netease.im/nimserver/team/getMarkReadInfo.action"
        data = {"tid": tid, 'msgid': msgid, 'fromAccid': fromAccid}
        if 'snapshot' in kwargs:
            if kwargs['snapshot']:
                data['snapshot'] = "true"
            else:
                data['snapshot'] = "false"
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def changeOwner(self, tid, owner, newowner, leave):
        """
        移交群主
        :param tid:
        :param owner:
        :param newowner:新群主帐号，最大长度32字符
        :param leave:1:群主解除群主后离开群，2：群主解除群主后成为普通成员。其它414
        :return:
        """
        url = "https://api.netease.im/nimserver/team/changeOwner.action"
        data = {"tid": tid, 'owner': owner, 'newowner': newowner, 'leave': leave}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def addManager(self, tid, owner, members):
        """
        任命管理员
        :param tid:
        :param owner:
        :param members:["aaa","bbb"](JSONArray对应的accid，如果解析出错会报414)，长度最大1024字符（一次添加最多10个管理员）
        :return:
        """
        url = "https://api.netease.im/nimserver/team/addManager.action"
        data = {"tid": tid, 'owner': owner, 'members': members}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def removeManager(self, tid, owner, members):
        """
        解除管理员身份，可以批量，但是一次解除最多不超过10个人
        :param tid:
        :param owner:
        :param members:["aaa","bbb"](JSONArray对应的accid，如果解析出错会报414)，长度最大1024字符（一次添加最多10个管理员）
        :return:
        """
        url = "https://api.netease.im/nimserver/team/removeManager.action"
        data = {"tid": tid, 'owner': owner, 'members': members}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def joinTeams(self, accid):
        """
        获取某用户所加入的群信息
        :param accid:
        :return:
        """
        url = "https://api.netease.im/nimserver/team/joinTeams.action"
        data = {'accid': accid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def updateTeamNick(self, tid, owner, accid, nick, **kwargs):
        """
        修改群昵称
        :param tid:
        :param owner:
        :param accid:
        :param nick:
        :param kwargs:custom:自定义扩展字段，最大长度1024字节
        :return:
        """
        url = "https://api.netease.im/nimserver/team/joinTeams.action"
        data = {'tid': tid, 'owner': owner, 'accid': accid, 'nick': nick}
        if 'custom' in kwargs:
            data['custom'] = kwargs['custom']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def muteTeam(self, tid, accid, ope):
        """
        修改消息提醒开关
        :param tid:网易云通信服务器产生，群唯一标识，创建群时会返回
        :param accid:要操作的群成员accid
        :param ope:1：关闭消息提醒，2：打开消息提醒，其他值无效
        :return:
        """
        url = "https://api.netease.im/nimserver/team/muteTeam.action"
        data = {'tid': tid, 'accid': accid, 'ope': ope}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def muteTlist(self, tid, owner, accid, mute):
        """
        禁言群成员
        :param tid:
        :param owner:
        :param accid:禁言对象的accid
        :param mute:1-禁言，0-解禁
        :return:
        """
        url = "https://api.netease.im/nimserver/team/muteTlist.action"
        data = {'tid': tid, 'owner': owner, 'accid': accid, 'mute': mute}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def leave(self, tid, accid):
        """
        主动退群
        :param tid:
        :param accid:
        :return:
        """
        url = "https://api.netease.im/nimserver/team/leave.action"
        data = {'tid': tid, 'accid': accid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def muteTlistAll(self, tid, owner, **kwargs):
        """
        将群组整体禁言
        :param tid:
        :param owner:
        :param kwargs:mute:true:禁言，false:解禁(mute和muteType至少提供一个，都提供时按mute处理)
                      muteType:禁言类型 0:解除禁言，1:禁言普通成员 3:禁言整个群(包括群主)
        :return:
        """
        url = "https://api.netease.im/nimserver/team/muteTlistAll.action"
        data = {'tid': tid, 'owner': owner}
        if not 'mute' in kwargs:
            if 'muteType' in kwargs:
                data['muteType'] = kwargs['muteType']
        else:
            data['mute'] = kwargs['mute']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def listTeamMute(self, tid, owner):
        """
        获取群组禁言列表
        :param tid:
        :param owner:
        :return:
        """
        url = "https://api.netease.im/nimserver/team/listTeamMute.action"
        data = {'tid': tid, 'owner': owner}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()


if __name__ == '__main__':
    APPKEY = "APPKEY"
    APP_SECRET = "APP_SECRET"
    msg = Msg(APPKEY, APP_SECRET)
    team = Team(APPKEY, APP_SECRET)
    print("-" * 30)
    print('create:')
    response = team.create('test_team', 'test3', json.dumps(['test2', 'test1']), 'please join us ', 0, 1)
    print(response)
    tid = response['tid']

    print("-" * 30)
    print('query:')
    response = team.query(json.dumps([tid, ]), 1)
    print(response)

    print("-" * 30)
    print('kick:')
    response = team.kick(tid, 'test3', member='test1')
    print(response)

    print("-" * 30)
    print('query:')
    response = team.query(json.dumps([tid, ]), 1)
    print(response)

    print("-" * 30)
    print('add:')
    response = team.add(tid, 'test3', json.dumps(['test1', ]), 0, 'please join us')
    print(response)

    print("-" * 30)
    print('query:')
    response = team.query(json.dumps([tid, ]), 1)
    print(response)

    print("-" * 30)
    print('update:')
    response = team.update(tid, 'test3', tname='change_name', announcement='will be remove', intro='a team for test')
    print(response)

    print("-" * 30)
    print('query:')
    response = team.query(json.dumps([tid, ]), 1)
    print(response)

    print("-" * 30)
    print('sendmsg:')
    response = msg.sendMsg('test3', 1, tid, 0, msg.text_msg_body('test'))
    print(response)
    msgid = response['data']['msgid']

    print("-" * 30)
    print('getMarkReadInfo:')
    response = team.getMarkReadInfo(tid, msgid, 'test3', snapshot=True)
    print(response)

    print("-" * 30)
    print('changeOwner:')
    response = team.changeOwner(tid, 'test3', 'test2', 2)
    print(response)

    print("-" * 30)
    print('query:')
    response = team.query(json.dumps([tid, ]), 1)
    print(response)

    print("-" * 30)
    print('changeOwner:')
    response = team.changeOwner(tid, 'test2', 'test3', 2)
    print(response)

    print("-" * 30)
    print('query:')
    response = team.query(json.dumps([tid, ]), 1)
    print(response)

    print("-" * 30)
    print('remove:')
    response = team.remove(tid, 'test3')
    print(response)
