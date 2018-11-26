from django import forms
from .import models


class BduserRegForm(forms.ModelForm):
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



    class Meta:
        model = models.Bduser
        fields = ['name', 'gender', 'age', 'place', 'city', 'district', 'phone', 'email', 'bloodgroup', 'username', 'password']