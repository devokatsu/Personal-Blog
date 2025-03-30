from django import forms
from . models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'img')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Article Title'}),
            'content': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Article Content...'}),
            'img': forms.FileInput(attrs={'class': "form-control"}),
        }