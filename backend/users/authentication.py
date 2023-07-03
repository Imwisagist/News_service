from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header,
)
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()
        if (
                not auth_header or
                auth_header[0].lower() != b'token' or
                len(auth_header) != 2
        ):
            raise AuthenticationFailed(
                ('Authentication failed. '
                 'Specify the keyword token as value in the begining.'
                 'Header must looks like following template. '
                 'Headers - Key: Authorization, Value: Token <your_token>')
            )
        try:
            token = auth_header[1].decode('utf-8')
        except UnicodeError:
            raise AuthenticationFailed(
                ('Invalid token header. '
                 'Token string should not contain invalid characters.')
            )
        token_obj = Token.objects.filter(key=token)
        if not token_obj:
            raise AuthenticationFailed("Such token doesn't exists.")

        return token_obj.first().user, None
