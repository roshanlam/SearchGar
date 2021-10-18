from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.hashers import check_password

class BasicCustomBackend(object):
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            user_password = user.password
            if check_password(password,user_password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None