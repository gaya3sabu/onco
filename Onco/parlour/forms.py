from django import forms
from .import models


class ParlourRegForm(forms.ModelForm):
    parlour_id = forms.CharField(
        required=True,
        label='district',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )

    name = forms.CharField(
        required=True,
        label='name',
        max_length=20,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+'})
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

    district = forms.CharField(
        required=True,
        label='district',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )

    class Meta:
        model = models.Parlour
        fields = ['parlour_id', 'name', 'place', 'city', 'district', 'email', 'phone']