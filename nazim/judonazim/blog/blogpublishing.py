from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
        'title',
        'subtitle',
        'content',
        'thumb',
        ]

        widgets = {
        'title': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'עד 100 תווים'}),
        'subtitle': forms.TextInput(attrs = {'class' : 'form-control',  'placeholder' : 'עד 200 תווים'}),
        'content' : forms.TextInput(attrs = { 'class' : 'richtext', 'id':'richtext'}),

        }
