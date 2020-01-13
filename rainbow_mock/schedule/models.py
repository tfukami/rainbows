from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from .validate import valid_gender
from .validate import valid_occupation


# Create your models here.
class Prof(models.Model):
    GENDER_SELECTION = ((0, '男性'), (1, '女性'))
    OCCUPATION_SELECTION = ((0, '会社員'), (1, '専業主婦'), (2, '学生'), (3, 'その他'))

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    nick_name = models.CharField(verbose_name='ニックネーム', max_length=100, default='jack/peter/mike/etc..')
    gender = models.CharField(verbose_name='性別', max_length=3, validators=[valid_gender], choices=GENDER_SELECTION)
    barth_date = models.DateTimeField(verbose_name='生年月日', null=True)
    occupation = models.CharField(
        verbose_name='職業', max_length=10, validators=[valid_occupation], choices=OCCUPATION_SELECTION
    )
    hobby = models.TextField(verbose_name='趣味', blank=True, null=True)
    has_child_num = models.IntegerField(verbose_name='子供の数')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.user.username


class Children(models.Model):
    GENDER_SELECTION = ((0, '男性'), (1, '女性'))

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='子供の名前', max_length=100, null=True)
    gender = models.CharField(verbose_name='子供の性別', max_length=3, validators=[valid_gender], choices=GENDER_SELECTION)
    barth_date = models.DateTimeField(verbose_name='子供の生年月日', null=True)
    hobby = models.TextField(verbose_name='好きな遊び', blank=True, null=True)
    character = models.TextField(verbose_name='好きなキャラクター', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return self.user.username + ':' + self.name


class Partner(models.Model):
    OCCUPATION_SELECTION = ((0, '会社員'), (1, '専業主婦'), (2, '学生'), (3, 'その他'))

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='パートナーの名前', max_length=100, null=True)
    barth_date = models.DateTimeField(verbose_name='パートナーの生年月日', null=True)
    occupation = models.CharField(
        verbose_name='パートナーの職業', max_length=5, validators=[valid_occupation], choices=OCCUPATION_SELECTION
    )
    hobby = models.TextField(verbose_name='パートナーの趣味', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Partner'

    def __str__(self):
        return self.user.username + ':' + self.name


class Schedules(models.Model):
    SCHEDULE_SELECTION = ((0, '●'), (1, '▲'), (2, '×'))
    PERIOD_SELECTION = ((0, '午前'), (1, '正午'), (2, '午後'))

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    schedule_date = models.DateField(verbose_name='日付', default=timezone.now())
    status = models.IntegerField(verbose_name='状態', choices=SCHEDULE_SELECTION, default=1)
    period = models.IntegerField(verbose_name='時間帯', choices=PERIOD_SELECTION, default=0)

    def __show_period__(self):
        display_period = ''
        for p in self.PERIOD_SELECTION:
            if p[0] == self.period:
                display_period = p[1]
        return display_period

    class Meta:
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return self.user.username + ':' + str(self.schedule_date) + ' ' + self.__show_period__()


class Friends(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', related_name='user', on_delete=models.PROTECT)
    friend = models.ForeignKey(
        CustomUser, verbose_name='友人', related_name='friend', on_delete=models.PROTECT, null=True
    )
    group = models.CharField(verbose_name='グループ', max_length=100)

    class Meta:
        verbose_name_plural = 'Friends'

    def __str__(self):
        return self.user.username
