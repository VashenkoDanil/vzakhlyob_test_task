from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.account.models import User
from apps.account.tokens import account_activation_token


def send_activate_account_email(user_id: int, site_domain: str) -> None:
    user = User.objects.get(id=user_id)

    mail_subject = 'Активируйте свой аккаунт.'
    message = render_to_string(
        'account/account_active_email.html',
        {
            'username': user.username,
            'domain': site_domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }
    )
    email = EmailMessage(
        mail_subject, message, to=[user.email]
    )
    email.send()
