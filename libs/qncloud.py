from urllib.parse import urljoin

from qiniu import Auth, put_file

from swiper import config


def qn_upload(filename, filepath):
    '''将文件上传到七牛云'''
    qn = Auth(config.QN_ACCESS_KEY, config.QN_SECRET_KEY)  # 构建鉴权对象
    token = qn.upload_token(config.QN_BUCKET, filename, 3600)  # 生成上传 Token，并指定过期时间
    ret, info = put_file(token, filename, filepath)  # 文件上传
    if info.ok():
        url = urljoin(config.QN_BASEURL, filename)
        return True, url
    else:
        return False, ''
