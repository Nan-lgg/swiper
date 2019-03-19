import re
import random

import requests

from swiper import config


def is_phonenum(phonenum):
    '''检查是否是一个正常的手机号'''
    if re.match(r'1[3456789]\d{9}$', phonenum):
        return True
    else:
        return False


def gen_random_code(length=4):
    '''产生一个指定长度的随机码'''
    rand_num = random.randrange(0, 10 ** length)
    template = '%%0%sd' % length
    vcode = template % rand_num
    return vcode


def send_sms(phonenum, vcode):
    '''发送短信'''
    args = config.YZX_SMS_ARGS.copy()  # 原型模式
    args['param'] = vcode
    args['mobile'] = phonenum

    response = requests.post(config.YZX_SMS_API, json=args)
    return response


def send_vcode(phonenum):
    '''发送验证码'''
    vcode = gen_random_code(4)  # 产生一个随机的验证码
    response = send_sms(phonenum, vcode)  # 发送验证码

    # 检查发送状态是否成功
    if response.status_code == 200:
        result = response.json()
        if result.get('code') == '000000':
            return True

    return False
