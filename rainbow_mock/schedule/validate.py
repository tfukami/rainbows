from django.core.exceptions import ValidationError


def valid_gender(value):
    if value not in (0, 1):
        raise ValidationError('想定外の値が代入されています．{男性/女性}から選んでください．')


def valid_occupation(value):
    if value not in (0, 1, 2, 3):
        raise ValidationError('想定外の値が代入されています．{会社員/専業主婦/学生/その他}から選んでください．')

