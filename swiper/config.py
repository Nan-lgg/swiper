'''
程序逻辑的配置，以及第三方平台的配置
'''

# 每天反悔次数上限
REWIND_LIMIT = 3

# 滑动积分规则
SWIPE_SCORE = {
    'like': +5,
    'superlike': +7,
    'dislike': -5,
}

# 云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_ARGS = {
    "sid": "e749e99071ee277991c27cf9eb62fc8d",
    "token": "bdcacd327c23b7c6a55adf2955e93c43",
    "appid": "081502fffccd4313bdf6369d36802fd0",
    "templateid": "421727",
    "param": None,
    "mobile": None,
}


# 七牛云配置
QN_ACCESS_KEY = 'kEM0sRR-meB92XU43_a6xZqhiyyTuu5yreGCbFtw'
QN_SECRET_KEY = 'QxTKqgnOb_UVldphU261qu9IdzmjkgGHh6GQVPPy'
QN_BUCKET = 'sh1808'
QN_BASEURL = 'http://pop1y3942.bkt.clouddn.com'
