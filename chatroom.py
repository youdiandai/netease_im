#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/6/20'
"""
from check_sum_headers import HeaderApi
import requests


class ChatRoom(HeaderApi):
    def create(self, creator, name, **kwargs):
        """
        创建聊天室
        :param creator:聊天室属主的账号accid
        :param name:聊天室名称，长度限制128个字符
        :param kwargs:announcement:公告，长度限制4096个字符
                      broadcasturl:直播地址，长度限制1024个字符
                      ext:扩展字段，最长4096字符
                      queuelevel:队列管理权限：0:所有人都有权限变更队列，1:只有主播管理员才能操作变更。默认0
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/create.action"
        data = {'creator': creator, 'name': name}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def get(self, roomid, **kwargs):
        """
        查询聊天室信息
        :param roomid:
        :param kwargs:needOnlineUserCount:是否需要返回在线人数，true或false，默认false
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/create.action"
        data = {'roomid': roomid}
        if 'needOnlineUserCount' in kwargs:
            if kwargs['needOnlineUserCount']:
                data['needOnlineUserCount'] = "true"
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def getBatch(self, roomids, **kwargs):
        """
        查询聊天室信息
        :param roomid:多个roomid，格式为：["6001","6002","6003"]（JSONArray对应的roomid，如果解析出错，会报414错误），限20个roomid
        :param kwargs:needOnlineUserCount:是否需要返回在线人数，true或false，默认false
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/getBatch.action"
        data = {'roomids': roomids}
        if 'needOnlineUserCount' in kwargs:
            if kwargs['needOnlineUserCount']:
                data['needOnlineUserCount'] = "true"
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def update(self, roomid, **kwargs):
        """
        更新聊天室信息
        :param roomid:
        :param kwargs:name:聊天室名称，长度限制128个字符
                      announcement:公告，长度限制4096个字符
                      broadcasturl:直播地址，长度限制1024个字符
                      ext:扩展字段，长度限制4096个字符
                      needNotify:true或false,是否需要发送更新通知事件，默认true
                      notifyExt:通知事件扩展字段，长度限制2048
                      queuelevel:队列管理权限：0:所有人都有权限变更队列，1:只有主播管理员才能操作变更
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/update.action"
        data = {'roomid': roomid}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        if 'needNotify' in kwargs:
            if kwargs['needNotify']:
                data['needNotify'] = "false"
            else:
                data['needNotify'] = "true"
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def toggleCloseStat(self, roomid, operator, valid):
        """
        修改聊天室开/关闭状态
        :param roomid:
        :param operator:操作者账号，必须是创建者才可以操作
        :param valid:true或false，false:关闭聊天室；true:打开聊天室
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/toggleCloseStat.action"
        data = {'roomid': roomid, 'operator': operator, 'valid': 'true' if valid else 'false'}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def setMemberRole(self, roomid, operator, target, opt, optvalue, **kwargs):
        """
        设置聊天室内用户角色
        :param roomid:
        :param operator:操作者账号accid
        :param target:被操作者账号accid
        :param opt:
                   1: 设置为管理员，operator必须是创建者
                   2:设置普通等级用户，operator必须是创建者或管理员
                   -1:设为黑名单用户，operator必须是创建者或管理员
                   -2:设为禁言用户，operator必须是创建者或管理员
        :param optvalue:true或false，true:设置；false:取消设置
        :param kwargs: notifyExt:通知扩展字段，长度限制2048，请使用json格式
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/setMemberRole.action"
        data = {'roomid': roomid, 'operator': operator, 'target': target, 'opt': opt,
                'optvalue': 'optvalue' if optvalue else 'false'}
        if 'notifyExt' in kwargs:
            data['notifyExt'] = kwargs['notifyExt']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def requestAddr(self, roomid, accid, **kwargs):
        """
        请求聊天室地址与令牌
        :param roomid:
        :param accid:
        :param kwargs: clienttype:1:weblink（客户端为web端时使用）; 2:commonlink（客户端为非web端时使用）;3:wechatlink(微信小程序使用), 默认1
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/requestAddr.action"
        data = {'roomid': roomid, 'accid': accid}
        if 'clienttype' in kwargs:
            data['clienttype'] = kwargs['clienttype']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def sendMsg(self, roomid, msgId, fromAccid, msgType, **kwargs):
        """
        发送聊天室消息
        :param roomid:
        :param msgId:客户端消息id，使用uuid等随机串，msgId相同的消息会被客户端去重
        :param fromAccid:消息发出者的账号accid
        :param msgType:
                       消息类型：
                       0: 表示文本消息，
                       1: 表示图片
                       2: 表示语音，
                       3: 表示视频，
                       4: 表示地理位置信息，
                       6: 表示文件，
                       10: 表示Tips消息，
                       100: 自定义消息类型（特别注意，对于未对接易盾反垃圾功能的应用，该类型的消息不会提交反垃圾系统检测）
        :param kwargs: resendFlag:	重发消息标记，0：非重发消息，1：重发消息，如重发消息会按照msgid检查去重逻辑
                       attach:消息内容，格式同消息格式示例中的body字段,长度限制4096字符
                       ext:消息扩展字段，内容可自定义，请使用JSON格式，长度限制4096字符
                       antispam:对于对接了易盾反垃圾功能的应用，本消息是否需要指定经由易盾检测的内容（antispamCustom）。true或false, 默认false。只对消息类型为：100 自定义消息类型 的消息生效。
                       antispamCustom:在antispam参数为true时生效。
                                      自定义的反垃圾检测内容, JSON格式，长度限制同body字段，不能超过5000字符，要求antispamCustom格式如下：
                                      {"type":1,"data":"custom content"}
                                      字段说明：
                                      1. type: 1：文本，2：图片。
                                      2. data: 文本内容or图片地址。
                       skipHistory:是否跳过存储云端历史，0：不跳过，即存历史消息；1：跳过，即不存云端历史；默认0
                       bid:可选，反垃圾业务ID，实现“单条消息配置对应反垃圾”，若不填则使用原来的反垃圾配置
                            highPriority:可选，true表示是高优先级消息，云信会优先保障投递这部分消息；false表示低优先级消息。默认false。
                            强烈建议应用恰当选择参数，以便在必要时，优先保障应用内的高优先级消息的投递。若全部设置为高优先级，则等于没有设置。
                       useYidun:可选，单条消息是否使用易盾反垃圾，可选值为0。
                                0：（在开通易盾的情况下）不使用易盾反垃圾而是使用通用反垃圾，包括自定义消息。
                                若不填此字段，即在默认情况下，若应用开通了易盾反垃圾功能，则使用易盾反垃圾来进行垃圾消息的判断
                       needHighPriorityMsgResend:可选，true表示会重发消息，false表示不会重发消息。默认true
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/sendMsg.action"
        data = {'roomid': roomid, 'msgId': msgId, 'fromAccid': fromAccid, 'msgType': msgType}
        for x in kwargs:
            data[x] = kwargs[x]
        if 'antispam' in kwargs:
            data['antispam'] = self.tran_boolean(kwargs['antispam'])
        if 'highPriority' in kwargs:
            data['highPriority'] = self.tran_boolean(kwargs['highPriority'])
        if 'needHighPriorityMsgResend' in kwargs:
            data['needHighPriorityMsgResend'] = self.tran_boolean(kwargs['needHighPriorityMsgResend'])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def addRobot(self, roomid, accids, **kwargs):
        """
        往聊天室内添加机器人
        :param roomid:
        :param accids:机器人账号accid列表，必须是有效账号，账号数量上限100个
        :param kwargs:roleExt:机器人信息扩展字段，请使用json格式，长度4096字符
                      notifyExt:机器人进入聊天室通知的扩展字段，请使用json格式，长度2048字符
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/sendMsg.action"
        data = {'roomid': roomid, 'accids': accids}
        for x in kwargs:
            data[x] = kwargs[x]
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def removeRobot(self, roomid, accids):
        """
        从聊天室内删除机器人
        :param roomid:
        :param accids:机器人账号accid列表，必须是有效账号，账号数量上限100个
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/removeRobot.action"
        data = {'roomid': roomid, 'accids': accids}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def temporaryMute(self, roomid, operator, target, muteDuration, **kwargs):
        """
        设置临时禁言状态
        :param roomid:
        :param operator:操作者accid,必须是管理员或创建者
        :param target:被禁言的目标账号accid
        :param muteDuration:0:解除禁言;>0设置禁言的秒数，不能超过2592000秒(30天)
        :param kwargs:needNotify:操作完成后是否需要发广播，true或false，默认true
                      notifyExt:通知广播事件中的扩展字段，长度限制2048字符
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/temporaryMute.action"
        data = {'roomid': roomid, 'operator': operator, 'target': target, 'muteDuration': muteDuration}
        if 'needNotify' in kwargs:
            data['needNotify'] = self.tran_boolean(kwargs['needNotify'])
        if 'notifyExt' in kwargs:
            data['notifyExt'] = kwargs['notifyExt']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queueOffer(self, roomid, key, value, **kwargs):
        """
        往聊天室有序队列中新加或更新元素
        :param roomid:
        :param key:
        :param value:
        :param kwargs:operator:提交这个新元素的操作者accid，默认为该聊天室的创建者，若operator对应的帐号不存在，会返回404错误。
                               若指定的operator不在线，则添加元素成功后的通知事件中的操作者默认为聊天室的创建者；
                               若指定的operator在线，则通知事件的操作者为operator。
                      transient:这个新元素的提交者operator的所有聊天室连接在从该聊天室掉线或者离开该聊天室的时候，提交的元素是否需要删除。
                                true：需要删除；false：不需要删除。默认false。
                                当指定该参数为true时，若operator当前不在该聊天室内，则会返回403错误。
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/queueOffer.action"
        data = {'roomid': roomid, 'key': key, 'value': value}
        if 'transient' in kwargs:
            data['transient'] = self.tran_boolean(kwargs['transient'])
        if 'operator' in kwargs:
            data['operator'] = kwargs['operator']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queuePoll(self, roomid, **kwargs):
        """
        从队列中取出元素
        :param roomid:
        :param kwargs:key:目前元素的elementKey,长度限制128字符，不填表示取出头上的第一个
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/queuePoll.action"
        data = {'roomid': roomid}
        if 'key' in kwargs:
            data['key'] = kwargs['key']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queueList(self, roomid):
        """
        排序列出队列中所有元素
        :param roomid:
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/queueList.action"
        data = {'roomid': roomid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queueDrop(self, roomid):
        """
        删除清理整个队列
        :param roomid:
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/queueDrop.action"
        data = {'roomid': roomid}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queueInit(self, roomid, sizeLimit):
        """
        初始化队列
        :param roomid:
        :param sizeLimit:队列长度限制，0~1000
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/queueInit.action"
        data = {'roomid': roomid, 'sizeLimit': sizeLimit}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def muteRoom(self, roomid, operator, mute, **kwargs):
        """
        将聊天室整体禁言
        :param roomid:
        :param operator:操作者accid，必须是管理员或创建者
        :param mute:true或false
        :param kwargs:needNotify:true或false，默认true
                     notifyExt:通知扩展字段
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/muteRoom.action"
        data = {'roomid': roomid, 'operator': operator, 'mute': mute}
        if 'needNotify' in kwargs:
            data['needNotify'] = self.tran_boolean(kwargs['needNotify'])
        if 'notifyExt' in kwargs:
            data['notifyExt'] = kwargs['notifyExt']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def topn(self, **kwargs):
        """
        查询聊天室统计指标TopN
        :param kwargs:topn:topn值，可选值 1~500，默认值100
                      timestamp	:需要查询的指标所在的时间坐标点，不提供则默认当前时间，单位秒/毫秒皆可
                      period:统计周期，可选值包括 hour/day, 默认hour
                      orderby:取排序值,可选值 active/enter/message,分别表示按日活排序，进入人次排序和消息数排序， 默认active
        :return:
        """
        url = "https://api.netease.im/nimserver/stats/chatroom/topn.action"
        data = {}
        for x in kwargs:
            data.__setitem__(w, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def membersByPage(self, roomid, _type, endtime, limit):
        """
        分页获取成员列表
        :param roomid:
        :param type:需要查询的成员类型,0:固定成员;1:非固定成员;2:仅返回在线的固定成员
        :param endtime:单位毫秒，按时间倒序最后一个成员的时间戳,0表示系统当前时间
        :param limit:返回条数，<=100
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/membersByPage.action"
        data = {'roomid': roomid, 'type': _type, 'endtime': endtime, 'limit': limit}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def queryMembers(self, roomid, accids):
        """
        批量获取在线成员信息
        :param roomid:
        :param accids:
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/queryMembers.action"
        data = {'roomid': roomid, 'accids': accids}
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def updateMyRoomRole(self, roomid, accid, **kwargs):
        """
        变更聊天室内的角色信息
        :param roomid:
        :param accid:
        :param kwargs:save:变更的信息是否需要持久化，默认false，仅对聊天室固定成员生效
                      needNotify:是否需要做通知
                      notifyExt:通知的内容，长度限制2048
                      nick:聊天室室内的角色信息：昵称
                      avator:聊天室室内的角色信息：头像
                      ext:聊天室室内的角色信息：开发者扩展字段
        :return:
        """
        url = "https://api.netease.im/nimserver/chatroom/updateMyRoomRole.action"
        data = {'roomid': roomid, 'accid': accid}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        if 'save' in kwargs:
            data['save'] = self.tran_boolean(kwargs['save'])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()
