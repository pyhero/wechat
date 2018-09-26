# coding=utf-8
import itchat


def wechat(user, msg):
    itchat.auto_login(True, enableCmdQR=2)
    friend = itchat.search_friends(name=user)
    itchat.send_msg(msg=msg, toUserName=friend[0]['UserName'])

    # itchat.logout()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', action='store', dest='username', default=None, help='wechat remark name')
    parser.add_argument('-m', action='store', dest='msg', default=None, help='message')
    args = parser.parse_args()

    wechat(args.username, args.msg)
