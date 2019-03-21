import re
import os
import random

import requests
from django.conf import settings
from django.core.cache import cache

from swiper import config
from libs.qncloud import qn_upload
from worker import celery_app
from common import keys


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
    print('->', vcode)
    response = send_sms(phonenum, vcode)  # 发送验证码

    # 检查发送状态是否成功
    if response.status_code == 200:
        result = response.json()
        if result.get('code') == '000000':
            # 将验证码添加到缓存
            key = keys.VCODE_KEY % phonenum
            cache.set(key, vcode, 180)
            return True

    return False


def save_upload_file(uid, upload_file):
    '''保存上传的文件'''
    filename = 'Avatar-%s' % uid
    fullpath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(fullpath, 'wb') as fp:
        for chunk in upload_file.chunks():
            fp.write(chunk)
    return fullpath, filename


@celery_app.task
def save_avatar(user, avatar_file):
    '''上传用户头像'''
    # 将文件保存到本地
    fullpath, filename = save_upload_file(user.id, avatar_file)
    # 将文件上传到七牛云
    _, avatar_url = qn_upload(filename, fullpath)
    # 将 URL 保存到 UserModel
    user.avatar = avatar_url
    user.save()
