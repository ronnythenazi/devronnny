from django import forms
from .models import BlogPost, Profile

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
        'title': forms.TextInput(attrs = {'class' : 'posttitle nicetxtbox', 'placeholder' : 'עד 60 תווים'}),
        'author': forms.TextInput(attrs = {'id' : 'author', 'value':'', 'type':'hidden'}),
        'subtitle': forms.TextInput(attrs = {'class' : 'posttitle nicetxtbox',  'placeholder' : 'עד 200 תווים'}),
        'content' : forms.Textarea(attrs = { 'class' : 'nicetxtbox', 'id':'richtext'}),
        'thumb'   : forms.ClearableFileInput(attrs = {'class': 'upload-img'}),
        'publishstatus': forms.Select(attrs = {'class' :  'choices'})
        }


class frmProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['bio', 'profile_img']


        widgets ={
        'bio' : forms.Textarea(attrs = {'class': 'bio'}),
        'profile_img' : forms.ClearableFileInput(attrs = {'class': 'upload-img'}),
        }


    def __init__(self, *args, **kwargs):
        super(frmProfile, self).__init__(*args, **kwargs)
        self.fields['profile_img'].label =""
