import os
import sys
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from requests_pro import Requests
from base_wechat import BaseWechat


class OfficialAccounts(BaseWechat):
    def __init__(self, logger=None, debug=True):
        super().__init__(logger, debug)
        self.corp_id = 'xxx'
        self.corp_secret = 'xxx'

    def get_access_token(self, corp_id, corp_secret):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(
            corp_id, corp_secret
        )
        response = Requests().get(url)
        data = response.json()

        return data.get('access_token', None)

    def send_message(self, msg, access_token):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(access_token)
        data = {
           "toparty": "1",
           "msgtype": "text",
           "agentid": 1000002,
           "text": {
               "content": msg
           },
        }

        response = Requests().post(url, data)
        return response.json()

    def generate_msg(self):
        msgs = [
            '尊敬的客户：现已到吃饭时间，你已较长时间没有进食了，请抓紧时间吃饭，逾期将收取滞纳期限！',
            '干饭人，干饭魂，干饭都是人上人',
            '你的胃来求我，让我告诉你，好好吃饭吧，别虐待我…',
            '按时吃饭，早睡早起，自律如昔，能扛大事。',
            '笨蛋，到时间吃饭啦，别逼我去喂你哦。',
            '我今天只吃了一只鸡翅，请你替我再吃另一只鸡翅，咱们比翼双飞呗！',
            '世间唯爱与美食不可辜负，不管多忙，都要记得按时吃饭。',
            '锄禾日当午，干饭真辛苦…',
            '当时有顿饭放在我面前，我没有珍惜…',
            'Dinner Time ~',
            '要有酒，要有肉，要有曲儿，知否？',
            '面包该有了，一切都该有了',
            '你就给我吃饭去吧…',
            ''
        ]

        return random.choice(msgs)

    def eat(self):
        msg = self.generate_msg()
        access_token = self.get_access_token(self.corp_id, self.corp_secret)

        self.send_message(msg, access_token)


if __name__ == '__main__':
    OfficialAccounts().eat()
