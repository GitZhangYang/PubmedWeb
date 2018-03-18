from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="用户名")
    time = models.DateTimeField(default=datetime.now, verbose_name="时间", )
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(
        ("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True,
                              blank=True, verbose_name="手机号码")
    image = models.ImageField(
        upload_to="image/%Y/%m", default="", max_length=100, verbose_name="头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name