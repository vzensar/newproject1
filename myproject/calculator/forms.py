from django.core import validators
from django import  forms
from .models import  Cal

class calculator(forms.ModelForm):
    class Meta:
        model = Cal
        fields = ['first_value', 'second_value', 'result']
        widgets = {
            'first_value': forms.TextInput(attrs={'class': 'form-control'}),
            'second_value': forms.TextInput(attrs={'class': 'form-control'}),
            'result': forms.TextInput(attrs={'class': 'form-control'}),

        }