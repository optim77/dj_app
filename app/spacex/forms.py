from django import forms


class SingUp(forms.Form):
    username = forms.CharField(label="Username", max_length=20, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class Contact(forms.Form):

    username = forms.CharField(label="Username", max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','cols':'70'}))