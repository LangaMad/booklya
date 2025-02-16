from django import forms
from .models import Cart, CartItem

class CartAddFrom(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    update = forms.BooleanField(required=True, initial=False, widget=forms.HiddenInput)
