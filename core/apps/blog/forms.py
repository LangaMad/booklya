from django import forms
from .models import *


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)