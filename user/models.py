from django.db import models

from social.models import Friend
from vip.models import Vip


class User(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性'),
    )
    LOCATION = (
        ('bj', '北京'),
        ('sh', '上海'),
        ('gz', '广州'),
        ('sz', '深圳'),
        ('wh', '武汉'),
        ('xa', '西安'),
        ('cd', '成都'),
    )
    phonenum = models.CharField(max_length=14, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=20, unique=True, verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象的URL')
    location = models.CharField(max_length=8, choices=LOCATION, verbose_name='常居地')

    vip_id = models.IntegerField(verbose_name='用户对应的 VIP ID')

    @property
    def profile(self):
        '''用户的个人资料'''
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.get_or_create(id=self.id)
        return self._profile

    @property
    def vip(self):
        '''用户的 VIP 数据'''
        if not hasattr(self, '_vip'):
            self._vip = Vip.get(id=self.vip_id)
        return self._vip

    @property
    def friends(self):
        '''所有的好友'''
        fid_list = Friend.friends_id_list(self.id)
        return User.objects.filter(id__in=fid_list)


class Profile(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性'),
    )
    LOCATION = (
        ('bj', '北京'),
        ('sh', '上海'),
        ('gz', '广州'),
        ('sz', '深圳'),
        ('wh', '武汉'),
        ('xa', '西安'),
        ('cd', '成都'),
    )
    location = models.CharField(max_length=8, choices=LOCATION, verbose_name='目标城市')
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')
