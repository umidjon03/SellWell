from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email*',
            'type':  'email',
            'class': 'border p-3 w-100 my-2',
            })

        # self.fields['username'].widget.attrs.update({
        #     'placeholder': 'Username',
        #     'type':  'text',
        #     'class': 'border p-3 w-100 my-2',
        #     })

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



class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            "type":  "text",
            "class": "form-control", 
            "id":    "first-name",
        })

        self.fields['last_name'].widget.attrs.update({
            "type":  "text",
            "class": "form-control", 
            "id":    "last_name",
        })

        self.fields['avatar'].widget.attrs.update({
            "type":  "file", 
            "class": "form-control-file mt-2 pt-1",
            "id":    "input-file"
        })
        
        self.fields['community_name'].widget.attrs.update({
            "type":  "text",
            "class": "form-control", 
            "id":    "comunity-name",
        })

        self.fields['zip_code'].widget.attrs.update({
            "type":  "text",
            "class": "form-control", 
            "id":    "zip-code",
        })
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'community_name', 'zip_code']



# class EmailChangeform(ModelForm):
#     model = User
#     field = [email]