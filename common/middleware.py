from django.utils.deprecation import MiddlewareMixin

from common import errors
from libs.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    AUTH_URL_WHITE_LIST = [
        '/api/user/get_vcode',
        '/api/user/check_vcode',
    ]

    def process_request(self, request):
        # 检查当前的 URL 是否在白名单内
        if request.path in self.AUTH_URL_WHITE_LIST:
            # 白名单内的 URL 直接跳出
            return

        # 检查用户是否登录
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                return render_json(code=errors.USER_NOT_EXIST)
        else:
            return render_json(code=errors.LOGIN_REQIRED)
