from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUseerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email*',
            'type':  'email',
            'class': 'border p-3 w-100 my-2',
            })
        
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'type':  'password',
            'class': 'border p-3 w-100 my-2',
            })
        
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'type':  'password',
            'class': 'border p-3 w-100 my-2',
            })


    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
    #     widgets = {
    #     'email': forms.TextInput(attrs={
    #         'placeholder': 'Email*',
    #         'type':  'email',
    #         'class': 'border p-3 w-100 my-2',
    #     })
    # }    sililar to (9:13)th rows