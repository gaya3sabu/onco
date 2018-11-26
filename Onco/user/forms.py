from django import forms
from .import models



class UserRegForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='name',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})


    )

    age = forms.IntegerField(
        required=True,
        label='age',

    )

    place = forms.CharField(
        required=True,
        label='place',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )

    city = forms.CharField(
        required=True,
        label='city',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )


    username = forms.CharField(
        required=True,
        label='username',
        max_length=32

    )

    password = forms.CharField(
        required=True,
        label='password',
        max_length=32

    )


    class Meta:
        model = models.User
        fields = ['name', 'gender', 'age', 'place', 'city', 'district', 'phone', 'email', 'username', 'password']