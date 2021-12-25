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
        'publishstatus',
        'author',
        ]

        widgets = {
        'title': forms.TextInput(attrs = {'class' : 'posttitle nicetxtbox', 'placeholder' : 'עד 100 תווים'}),
        'author': forms.TextInput(attrs = {'id' : 'author', 'value':'', 'type':'hidden'}),
        'subtitle': forms.TextInput(attrs = {'class' : 'posttitle nicetxtbox',  'placeholder' : 'עד 200 תווים'}),
        'content' : forms.Textarea(attrs = { 'class' : 'nicetxtbox', 'id':'richtext'}),
        'thumb'   : forms.ClearableFileInput(attrs = {'class': 'upload-img'}),
        'publishstatus': forms.Select(attrs = {'class' :  'choices'})
        }
