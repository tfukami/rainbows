from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser
from allauth.account.adapter import DefaultAccountAdapter

GENDER_CHOICES = ((0, '男性'), (1, '女性'))
OCCUPATION_CHOICES = (
    (0, '会社員'), (1, '主婦'), (2, '学生'), (3, 'その他')
)


class CustomSignupForm(SignupForm):
    nick_name = forms.CharField(
        label='ニックネーム'
    )
    gender = forms.ChoiceField(
        label='性別',
        choices=GENDER_CHOICES
    )
    barth_date = forms.DateField(
        label='生年月日',
        required=True,
        input_formats=[
            '%Y-%m-%d',  # 2010-01-01
            '%Y/%m/%d',  # 2010/01/01
        ])
    occupation = forms.ChoiceField(
        label='職業',
        choices=OCCUPATION_CHOICES
    )
    has_child_num = forms.IntegerField(
        label='子供の数',
        min_value=1,
        max_value=10
    )

    class Meta:
        model = CustomUser

    def signup(self, request, user):
        user.nickname = self.cleaned_data['nick_name']
        user.gender = self.cleaned_data['gender']
        user.barth_date = self.cleaned_data['barth_date']
        user.occupation = self.cleaned_data['occupation']
        user.has_child_num = self.cleaned_data['has_child_num']

        user.save()
        return user
