from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .validate import valid_gender
from .validate import valid_occupation

# Create your models here.


class CustomUser(AbstractUser):
    GENDER_SELECTION = ((0, '男性'), (1, '女性'))
    OCCUPATION_SELECTION = ((0, '会社員'), (1, '専業主婦'), (2, '学生'), (3, 'その他'))

    nick_name = models.CharField(verbose_name='ニックネーム', max_length=100, default='jack/peter/mike/etc..')
    gender = models.IntegerField(
        verbose_name='性別', validators=[valid_gender], choices=GENDER_SELECTION, null=True
    )
    barth_date = models.DateField(verbose_name='生年月日', null=True)
    occupation = models.IntegerField(
        verbose_name='職業', validators=[valid_occupation], choices=OCCUPATION_SELECTION, null=True
    )
    hobby = models.TextField(verbose_name='趣味', blank=True, null=True)
    has_child_num = models.IntegerField(verbose_name='子供の数', default=1)

    class Meta:
        verbose_name_plural = 'CustomUser'
