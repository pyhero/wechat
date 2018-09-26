# coding=utf-8
import sys
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from wechat import wechat

msg = [
    '晨曦卷帘妆容罢,含笑福问道安康',
    '浮世三千，吾爱有三，此时日为朝，几时后月为暮，唯有你，是我朝朝暮暮',
    '早安呀~',
    '早起的鸟儿有虫吃，早起的虫儿被鸟吃，早安~',
    'Morning~',
    '太阳晒屁股啦~'
]

wechat('F', random.choice(msg))
