from django import forms
from django.forms import TextInput
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    full_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество'}))
    phone = PhoneNumberField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': '+79123454321'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))
