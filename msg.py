#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/6/20'
"""
from check_sum_headers import HeaderApi
import requests
import json


class Msg(HeaderApi):
    @staticmethod
    def text_msg_body(str):
        return json.dumps({"msg": str})

    @staticmethod
    def img_msg_body(name, md5, url, ext, w, h, size):
        return json.dumps({"name": name, "md5": md5,
                           "url": url, "ext": ext,
                           "w": w, "h": h, "size": size})

    @staticmethod
    def voice_msg_body(dur, md5, url, ext, size):
        return json.dumps({"dur": dur,
                           "md5": md5,
                           "url": url,
                           "ext": ext,
                           "size": size})

    @staticmethod
    def video_msg_body(dur, md5, url, w, h, ext, size):
        return json.dumps({"dur": dur,
                           "md5": md5,
                           "url": url,
                           "ext": ext,
                           "size": size,
                           "w": w,
                           "h": h})

    @staticmethod
    def add_msg_body(title, lng, lat):
        return json.dumps({"title": title,
                           "lng": lng,
                           "lat": lat})

    @staticmethod
    def file_msg_body(name, md5, url, ext, size):
        return json.dumps({"name": name,
                           "md5": md5,
                           "url": url,
                           "ext": ext,
                           "size": size})

    @staticmethod
    def third_msg_body(_dict):
        return json.dumps(_dict)

    def sendMsg(self, _from, _ope, _to, _type, _body, **kwargs):
        """
        发送普通消息
        :param _from:发送者accid
        :param _ope:0：点对点个人消息，1：群消息（高级群），其他返回414
        :param _to:ope==0是表示accid即用户id，ope==1表示tid即群id
        :param _type:0 表示文本消息,
                     1 表示图片，
                     2 表示语音，
                     3 表示视频，
                     4 表示地理位置信息，
                     6 表示文件，
                     100 自定义消息类型
        :param _body:
        :param kwargs:antispam:本消息是否需要指定经由易盾检测的内容
                      antispamCustom:在antispam参数为true时生效。自定义的反垃圾检测内容, JSON格式，长度限制同body字段
                      option:发消息时特殊指定的行为选项
                      pushcontent:ios推送内容
                      payload:ios 推送对应的payload
                      ext:开发者扩展字段
                      forcepushlist:发送群消息时的强推（@操作）用户列表
                      forcepushcontent:发送群消息时，针对强推（@操作）列表forcepushlist中的用户，强制推送的内容
                      forcepushall:发送群消息时，强推（@操作）列表是否为群里除发送者外的所有有效成员，true或false，默认为false
                      bid:可选，反垃圾业务ID
                      useYidun:可选，单条消息是否使用易盾反垃圾
                      markRead:可选，群消息是否需要已读业务（仅对群消息有效），0:不需要，1:需要
        :return:
        """
        """
        option示例:{"push":false,"roam":true,"history":false,"sendersync":true,"route":false,"badge":false,"needPushNick":true}

        字段说明：
        1. roam: 该消息是否需要漫游，默认true（需要app开通漫游消息功能）； 
        2. history: 该消息是否存云端历史，默认true；
         3. sendersync: 该消息是否需要发送方多端同步，默认true；
         4. push: 该消息是否需要APNS推送或安卓系统通知栏推送，默认true；
         5. route: 该消息是否需要抄送第三方；默认true (需要app开通消息抄送功能);
         6. badge:该消息是否需要计入到未读计数中，默认true;
        7. needPushNick: 推送文案是否需要带上昵称，不设置该参数时默认true;
        8. persistent: 是否需要存离线消息，不设置该参数时默认true。
        """
        url = "https://api.netease.im/nimserver/msg/sendMsg.action"
        data = {"from": _from, "ope": _ope, "to": _to, "type": _type, "body": _body}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def sendBatchMsg(self, fromAccid, toAccids, _type, body, **kwargs):
        """
        批量发送点对点普通消息
        :param fromAccid:
        :param toAccids:JSONArray
        :param _type:同sendMsg
        :param body:
        :param kwargs:option,pushcontent,payload,ext,bid，useYidun (同sendMsg)
        :return:
        """
        url = "https://api.netease.im/nimserver/msg/sendBatchMsg.action"
        data = {"fromAccid": fromAccid, "toAccids": toAccids, "body": body, "type": _type}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

        pass

    def sendAttachMsg(self, _from, msgtype, to, attach, **kwargs):
        """
        发送自定义的系统通知
        :param _from:发送者accid，用户帐号，最大32字符，APP内唯一
        :param msgtype:0：点对点自定义通知，1：群消息自定义通知，其他返回414
        :param to:msgtype==0是表示accid即用户id，msgtype==1表示tid即群id
        :param attach: 自定义通知内容，第三方组装的字符串，建议是JSON串，最大长度4096字符
        :param kwargs: pushcontent:iOS推送内容，第三方自己组装的推送内容,不超过150字符
                       payload:iOS推送对应的payload,必须是JSON,不能超过2k字符
                       sound:如果有指定推送，此属性指定为客户端本地的声音文件名，长度不要超过30个字符，如果不指定，会使用默认声音
                       save:1表示只发在线，2表示会存离线，其他会报414错误。默认会存离线
                       option:
                       发消息时特殊指定的行为选项,Json格式，可用于指定消息计数等特殊行为;option中字段不填时表示默认值。
                       option示例：
                       {"badge":false,"needPushNick":false,"route":false}
                       字段说明：
                       1. badge:该消息是否需要计入到未读计数中，默认true;
                       2. needPushNick: 推送文案是否需要带上昵称，不设置该参数时默认false(ps:注意与sendMsg.action接口有别);
                       3. route: 该消息是否需要抄送第三方；默认true (需要app开通消息抄送功能)
        :return
        """
        url = "https://api.netease.im/nimserver/msg/sendAttachMsg.action"
        data = {"from": _from, "msgtype": msgtype, "to": to, "attach": attach}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def sendBatchAttachMsg(self, fromAccid, toAccids, attach, **kwargs):
        """
        批量发送点对点自定义系统通知
        :param fromAccid:
        :param toAccids:
        :param attach:
        :param kwargs:pushcontent:同sendAttachMsg
                      payload:同sendAttachMsg
                      sound:同sendAttachMsg
                      save:同sendAttachMsg
                      option:同sendAttachMsg
        :return:
        """
        url = "https://api.netease.im/nimserver/msg/sendBatchAttachMsg.action"
        data = {"fromAccid": fromAccid, "toAccids": toAccids, "attach": attach}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def upload(self, content, **kwargs):
        """
        文件上传
        :param content:字符流base64串(Base64.encode(bytes)) ，最大15M的字符流
        :param kwargs:_type:上传文件类型
                      ishttps:返回的url是否需要为https的url，True或False，默认False
        :return:
        """
        url = "https://api.netease.im/nimserver/msg/upload.action"
        data = {"content": content}
        if '_type' in kwargs:
            data.__setitem__('type', kwargs['_type'])
        if 'ishttps' in kwargs:
            data['ishttps'] = 'true' if kwargs['ishttps'] else 'false'
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def fileUpload(self, content, **kwargs):
        """
        文件上传（multipart方式）
        :param content:最大15M的字符流
        :param kwargs:_type:上传文件类型
                      ishttps:返回的url是否需要为https的url，True或False，默认False
        :return:
        """
        url = "https://api.netease.im/nimserver/msg/fileUpload.action"
        data = {"content": content}
        if '_type' in kwargs:
            data.__setitem__('type', kwargs['_type'])
        if 'ishttps' in kwargs:
            data['ishttps'] = 'true' if kwargs['ishttps'] else 'false'
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def recall(self, deleteMsgid, timetag, _type, _from, to, **kwargs):
        """
        消息撤回
        :param deleteMsgid:要撤回消息的msgid
        :param timetag:要撤回消息的创建时间
        :param type: 7:表示点对点消息撤回，8:表示群消息撤回，其它为参数错误
        :param _from:发消息的accid
        :param to:如果点对点消息，为接收消息的accid,如果群消息，为对应群的tid
        :param kwargs: msg:可以带上对应的描述
                       ignoreTime:1表示忽略撤回时间检测，其它为非法参数，如果需要撤回时间检测，不填即可
        :return:
        """
        url = "https://api.netease.im/nimserver/msg/recall.action"
        data = {"deleteMsgid": deleteMsgid, 'timetag': timetag, 'type': _type, "from": _from, "to": to}
        if 'msg' in kwargs:
            data.__setitem__('msg', kwargs['msg'])
        if 'ignoreTime' in kwargs and kwargs['ignoreTime'] == 1:
            data['ignoreTime'] = 1
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()

    def broadcastMsg(self, body, **kwargs):
        """
        发送广播消息
        :param body:广播消息内容，最大4096字符
        :param kwargs: _from:发送者accid, 用户帐号，最大长度32字符，必须保证一个APP内唯一
                       isOffline:是否存离线，true或false，默认false
                       ttl:存离线状态下的有效期，单位小时，默认7天
                       targetOs:目标客户端，默认所有客户端，jsonArray，格式：["ios","aos","pc","web","mac"]
        :return:
        """
        url = "https://api.netease.im/nimserver/msg/broadcastMsg.action"
        data = {"body": body}
        for x in kwargs:
            data.__setitem__(x, kwargs[x])
        if 'isOffline' in kwargs:
            data['isOffline'] = "true" if kwargs['isOffline'] else "false"
        if '_from' in kwargs:
            data['from'] = kwargs['_from']
        resp = requests.post(url=url, headers=self.get_header(), data=data)
        return resp.json()


if __name__ == '__main__':
    APPKEY = "APPKEY"
    APP_SECRET = "APP_SECRET"
    msg = Msg(APPKEY, APP_SECRET)
    print("-" * 30)
    print('sendMsg:')
    response = msg.sendMsg('test3', 0, 'test2', 0, msg.text_msg_body('hello world'))
    print(response)

    print("-" * 30)
    print('sendBatchMsg:')
    response = msg.sendBatchMsg('test3', json.dumps(['test1', 'test2']), 0, msg.text_msg_body('test batch msg'))
    print(response)

    print("-" * 30)
    print('sendAttachMsg:')
    response = msg.sendAttachMsg('test3', 0, 'test2', 'test system msg')
    print(response)

    print("-" * 30)
    print('sendBatchAttachMsg:')
    response = msg.sendBatchAttachMsg('test3', json.dumps(['test1', 'test2']), 'test batch system msg')
    print(response)
