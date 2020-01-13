from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)

        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        user.nick_name = form.cleaned_data.get('nick_name')
        user.gender = form.cleaned_data.get('gender')
        user.barth_date = form.cleaned_data.get('barth_date')
        user.occupation = form.cleaned_data.get('occupation')
        user.has_child_num = form.cleaned_data.get('has_child_num')
        user.save()
