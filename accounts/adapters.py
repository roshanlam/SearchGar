from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_field
        user = super().save_user(request, user, form, False)
        user_field(user, 'first_name', request.data.get('first_name', ''))
        user_field(user, 'last_name', request.data.get('last_name', ''))
        user.save()
        return user