from django import forms
from .models import *

class MenuItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')

    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'image', 'category']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'image': 'Изображение',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = { 
            'text': 'Текст отзыва',
        }
        
class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['times', 'booking_button_text']
        
class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=20)