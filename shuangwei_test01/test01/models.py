from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField("用户名", max_length=50)
    phone = models.IntegerField('手机号')
    email = models.EmailField('邮箱',max_length=20)
    password = models.CharField('用户密码', max_length=16)

    class Meta:
        db_table = 'userinfo'