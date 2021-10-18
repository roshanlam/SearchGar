import jwt
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import datetime
import json

User = get_user_model()


class JWTAuthentication(object):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')

        if not auth:
            return None
        try:
           payload = jwt.decode(json.dumps(auth), 'secreta', algorithms=['HS256'], verify=False)
           print(payload)
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid  characters.')
            raise exceptions.AuthenticationFailed(msg)
        return self.authenticate_credentials(payload)

    def authenticate_credentials(self, payload):
        email = payload['username']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        return (user)

    def authenticate_header(self, request):
        return 'Token'