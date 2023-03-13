from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.mail import mail_managers

from allauth.account.forms import SignupForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):

    def save(self, request):
        user = super().save(request)

        mail_managers(
            subject='New user.',
            message=f'New user - {user.username} - registered at web market.'
        )

        # subject = 'Welcome to the web market!'
        # text = f'{user.username}, your registration is completed.'
        # html = (
        #     f'<b>{user.username}</b>, you successfully completed registration on our'
        #     f'<a href="http://127.0.0.1:8000/products">website.</a>'
        # )
        # msg = EmailMultiAlternatives(
        #     subject=subject,
        #     body=text,
        #     from_email=None,
        #     to=[user.email]
        # )
        # msg.attach_alternative(html, 'text/html')
        # msg.send()

        # common_users = Group.objects.get(name="common users")
        # user.groups.add(common_users)
        return user
