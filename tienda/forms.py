from django import forms

class registroForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=10,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username'

    }))

    email = forms.EmailField(required=True,
    widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'example@gmail.com'

    }))
    password = forms.CharField(required=True, min_length=6,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'placeholder' : 'password'

    }))