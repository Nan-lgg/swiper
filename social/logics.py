import datetime

from user.models import User
from social.models import Swiped
from social.models import Friend


def get_rcmd_list(user, limit):
    '''获取推荐列表'''
    # 计算出出生年的范围
    curr_year = datetime.date.today().year  # 当前年份
    max_birth_year = curr_year - user.profile.min_dating_age
    min_birth_year = curr_year - user.profile.max_dating_age

    # 取出需要排出的用户 ID 列表
    sid_list = Swiped.objects.filter(uid=user.id).values_list('sid', flat=True)

    # 执行过滤
    rcmd_users = User.objects.filter(
        sex=user.profile.dating_sex,
        location=user.profile.location,
        birth_year__gt=min_birth_year,
        birth_year__lt=max_birth_year,
    ).exclude(id__in=sid_list)[:limit]

    return rcmd_users


def like_someone(user, sid):
    # 添加滑动记录
    Swiped.swipe(user.id, sid, 'like')

    # 检查对方是否喜欢过自身, 如果喜欢过，建立好友关系
    if Swiped.is_liked(sid, user.id):
        Friend.make_friends(user.id, sid)
        return True
    else:
        return False


def superlike_someone(user, sid):
    # 添加滑动记录
    Swiped.swipe(user.id, sid, 'superlike')

    # 检查对方是否喜欢过自身, 如果喜欢过，建立好友关系
    if Swiped.is_liked(sid, user.id):
        Friend.make_friends(user.id, sid)
        return True
    else:
        return False
