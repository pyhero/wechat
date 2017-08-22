# coding=utf-8
import sys
import itchat
import time

chatroomName = 'FriendTest'

def getChatroomUserName(chatroomName=chatroomName):
    chatroom = itchat.search_chatrooms(name=chatroomName)
    if len(chatroom) == 0:
        sys.exit('Not find group: {}'.format(chatroomName))
    else:
        chatroomUserName = chatroom[0]['UserName']
    return chatroomUserName

def TestFriends(friend, chatroomUserName):
    req = itchat.add_member_into_chatroom(chatroomUserName, [friend], useInvitation=True)
    if req['BaseResponse']['ErrMsg'] == u'请求成功':
        status = req['MemberList'][0]['MemberStatus']

        print(
            '{}: {}'.format(
                (friend['DisplayName'] or friend['NickName']),
                {3: u'该好友已经将你加入黑名单', 4: u'该好友已经将你删除'}.get(status, u'该好友仍旧与你是好友关系')
            )
        )
    else:
        print('{}: {}'.format((friend['DisplayName'] or friend['NickName']), req))

    itchat.delete_member_from_chatroom(chatroomUserName, [friend])

itchat.auto_login(True)

chatroomUserName = getChatroomUserName()

for friend in itchat.get_friends():
    TestFriends(friend, chatroomUserName)
    time.sleep(5)
