from django import forms
from .import models


class CandetRegForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='name',
        max_length=20,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+'})
    )

    symptom = forms.CharField(
        required=True,
        label='place',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})
    )
    cause = forms.CharField(
        required=True,
        label='city',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )

    test = forms.CharField(
        required=True,
        label='district',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )
    treatment = forms.CharField(
        required=True,
        label='district',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )

    class Meta:
        model = models.Cancerdet
        fields = ["name", "symptom", "cause", "test", "treatment"]