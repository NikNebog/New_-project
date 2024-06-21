from.models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields= ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class':'form-control',
                'placeholder': 'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)