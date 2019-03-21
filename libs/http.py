import json

from django.conf import settings
from django.http import HttpResponse

from common.errors import OK


def render_json(data=None, code=OK):
    '''将结果渲染成一个 Json 数据的 HttpResponse'''
    result = {
        'code': code,
        'data': data
    }

    if settings.DEBUG:
        json_result = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_result = json.dumps(result, ensure_ascii=False, separators=(',', ':'))

    return HttpResponse(json_result)
