from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'full_name', 'placeholder': 'Фамилия Имя'}))
    phone = PhoneNumberField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'type': 'tel', 'placeholder': '+79123454321'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'example@example.com'}))
    wishes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'message-text', 'placeholder': 'Пожелания к заказу'})),
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address', 'placeholder': 'Адрес'}))
