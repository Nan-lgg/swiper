import logging

from django.utils.deprecation import MiddlewareMixin

from common import errors
from libs.http import render_json
from user.models import User

err_log = logging.getLogger('err')


class AuthMiddleware(MiddlewareMixin):
    AUTH_URL_WHITE_LIST = [
        '/api/user/get_vcode',
        '/api/user/check_vcode',
        '/api/vip/show_vip',
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
                request.user = User.get(id=uid)
                return
            except User.DoesNotExist:
                err_log.error('%s : %s' % (errors.UserNotExist.code, errors.UserNotExist()))
                return render_json(code=errors.UserNotExist.code)
        else:
            err_log.error('%s : %s' % (errors.LoginReqired.code, errors.LoginReqired()))
            return render_json(code=errors.LoginReqired.code)


class LogicErrMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, errors.LogicError):
            data = exception.data or str(exception)
            err_log.error('%s : %s' % (exception.code, data))
            return render_json(data=data, code=exception.code)
