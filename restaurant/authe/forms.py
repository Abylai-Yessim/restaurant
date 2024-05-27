from django.contrib.auth.forms import UserCreationForm
from django import forms
from back.models import CustomUser


class SignUpUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-input'}))

    def __init__(self, *args, **kwargs):
        super(SignUpUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1' )
        labels = {
            'username': 'Имя',
            'email': 'Эмайл',
            'password1': 'Пароль',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

        help_texts = {
            'username': '',
            'password1': 'Ваш пароль должен содержать как минимум 8 символов.',
        }

class SignInUserForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
