import json

from django.http import HttpResponse

from common.errors import OK


def render_json(data=None, code=OK):
    '''将结果渲染成一个 Json 数据的 HttpResponse'''
    result = {
        'code': code,
        'data': data
    }

    json_result = json.dumps(result, ensure_ascii=False, separators=(',', ':'))

    return HttpResponse(json_result)
