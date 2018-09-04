from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
from utils import mvImageFromTmp


class UserProfile(models.Model):
    username = models.CharField(max_length=20,
                                verbose_name='用户名')
    password = models.CharField(max_length=50,
                                verbose_name='密码')
    email = models.CharField(max_length=50,
                             verbose_name='邮箱')
    phone = models.CharField(max_length=12,
                             verbose_name='手机号')

    photo =models.CharField(max_length=100,
                            verbose_name='头像',
                            null=True,
                            blank=True)

    # 对密码进行加密
    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
            print('****')
            self.photo = mvImageFromTmp(self.photo)
        super().save()

    class Meta:
        db_table = ''
        verbose_name = '用户表'
        verbose_name_plural = verbose_name