from django.db import models


class Vip(models.Model):
    '''会员表'''
    name = models.CharField(max_length=10, unique=True, verbose_name='Vip 的名字')
    level = models.IntegerField(verbose_name='会员等级')
    price = models.FloatField(verbose_name='会员的价格')

    def perms(self):
        '''查看当前会员拥有的所有权限'''
        perm_id_list = VipPermRelation.objects.filter(vip_id=self.id) \
                                              .values_list('perm_id', flat=True)
        return Permission.objects.filter(id__in=perm_id_list)


class Permission(models.Model):
    '''权限表'''
    name = models.CharField(max_length=10, unique=True, verbose_name='权限名称')
    description = models.TextField(verbose_name='权限详情介绍')


class VipPermRelation(models.Model):
    '''会员、权限的关系表'''
    vip_id = models.IntegerField(verbose_name='Vip 的 ID')
    perm_id = models.IntegerField(verbose_name='Permission 的 ID')
