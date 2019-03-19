from common import errors
from libs.http import render_json
from user import logics


def get_vcode(request):
    phonenum = request.POST.get('phonenum')
    # 检查手机号是否合法
    if logics.is_phonenum(phonenum):
        # 发送验证码
        logics.send_vcode(phonenum)
        return render_json()
    else:
        return render_json(code=errors.PHONENUM_ERR)


def check_vcode(request):
    return
