from django import forms
#from managers.models import Managers


class managerlogin_form(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        max_length=32
    )

    password = forms.CharField(
        required=True,
        label='password',
        max_length=32,
        widget=forms.PasswordInput()

    )

    class Meta:
        #model = Managers
       fields = ['mgr_name']
