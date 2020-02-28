from django.db import models


# Create your models here.

class Shop(models.Model):
    id = models.IntegerField("商品编号", unique=True,primary_key=True)
    name = models.CharField('商品名称', max_length=10,unique=True)
    number = models.IntegerField('商品数量')
    price = models.DecimalField('商品单价',max_digits=7,decimal_places=2,default=9999)

    class Meta:
        db_table = 'shopinfo'
