from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'phone', 'text']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Phone"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Message"}),
        }