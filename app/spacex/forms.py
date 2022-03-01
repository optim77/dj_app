from django import forms
from django.forms import ModelForm
from .models import Category, Item, ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100)

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class SingUp(forms.Form):
    username = forms.CharField(label="Username", max_length=20, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class Contact(ModelForm):

    class Meta:
        model = ContactMessage
        fields = ('__all__')
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class AddNewItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'image', 'category', 'price')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(AddNewItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})



