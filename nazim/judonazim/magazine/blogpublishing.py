from django import forms
from .models import BlogPost, Profile, Comment
from django.contrib.auth.models import User, Group



class UsrToGroupForm(forms.Form):
    users = Profile.objects.all() #User.objects.values_list('username', flat = True)
    members = forms.ModelMultipleChoiceField(queryset = users, widget=forms.SelectMultiple(attrs={'class':'signfield'}))
    groups = Group.objects.all() #Group.objects.all('name', flat = True)
    group = forms.ModelChoiceField(queryset=groups, widget=forms.Select(attrs={'class':'signfield'}))


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

class CommentFrm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =  ['name', 'body']


        widgets ={
        #'post': forms.TextInput(attrs = {'value':'', 'type':'hidden'}),
        'body' : forms.Textarea(attrs = { 'class' : 'comment-text-field comment-field'}),
        'name' : forms.TextInput(attrs = {'class' : 'comment-char-field comment-field'}),
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
