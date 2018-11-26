from django import forms
from bduser.models import Bduser


class login_forms(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        max_length=32
    )

    password = forms.CharField(
        required=True,
        label='password',
        max_length=36,
        widget=forms.PasswordInput()


    )


    class Meta:
        model = Bduser
        field = ['name']