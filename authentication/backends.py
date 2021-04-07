import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_date = authentication.get_authorization_header(request)
        if not auth_date:
            return None
        prefix, token = auth_date.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms= 'HS256')
            user = User.objects.get(username = payload['username'])
            return (user, token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Неверный токен', )
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Срок действия токена истёк', )