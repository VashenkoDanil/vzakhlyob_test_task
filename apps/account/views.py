from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .tokens import account_activation_token
from .tasks import send_activate_account_email


class CreateUserViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            send_activate_account_email.delay(
                user_id=response.data.get('id'),
                site_domain=get_current_site(request).domain
            )
            return Response('Пожалуйста, подтвердите свой адрес электронной почты, чтобы завершить регистрацию')
        return response


class ActivateUsersView(APIView):
    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        user = self._get_user(kwargs.get('uidb64'))

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(
                'Благодарим вас за подтверждение по электронной почте. Теперь вы можете войти в свою учетную запись.'
            )
        return Response('Ссылка для активации недействительна!')

    def _get_user(self, uidb64):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None
