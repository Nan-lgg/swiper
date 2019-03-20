from django.core.cache import cache

from common import errors
from common import keys
from libs.http import render_json
from user import logics
from user.models import User


def get_vcode(request):
    '''获取验证码'''
    phonenum = request.POST.get('phonenum')
    # 检查手机号是否合法
    if logics.is_phonenum(phonenum):
        # 发送验证码
        logics.send_vcode(phonenum)
        return render_json()
    else:
        return render_json(code=errors.PHONENUM_ERR)


def check_vcode(request):
    '''检查验证码'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    # 检查手机号是否合法
    if logics.is_phonenum(phonenum):
        cached_vcode = cache.get(keys.VCODE_KEY % phonenum)  # 从缓存获取验证码
        if cached_vcode == vcode:
            try:
                user = User.objects.get(phonenum=phonenum)
            except User.DoesNotExist:
                # 如果账号不存在，直接创建出来
                user = User.objects.create(phonenum=phonenum, nickname=phonenum)

            # 在 session 中记录登录状态
            request.session['uid'] = user.id
            return render_json(data=user.to_dict())
        else:
            return render_json(code=errors.VCODE_ERR)
    else:
        return render_json(code=errors.PHONENUM_ERR)


def get_profile(request):
    '''获取用户个人资料'''
    profile_dict = request.user.profile.to_dict()
    return render_json(profile_dict)
