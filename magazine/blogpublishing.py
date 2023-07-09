from django import forms
from .models import BlogPost, Profile, Comment, comment_of_comment, Album
from django.contrib.auth.models import User, Group






class UsrToGroupForm(forms.Form):
    users = Profile.objects.all() #User.objects.values_list('username', flat = True)
    members = forms.ModelMultipleChoiceField(queryset = users, widget=forms.SelectMultiple(attrs={'class':'signfield select-box'}))
    groups = Group.objects.all() #Group.objects.all('name', flat = True)
    group = forms.ModelChoiceField(queryset=groups, widget=forms.Select(attrs={'class':'signfield select-box'}))


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
        #fields =  ['name', 'body']
        fields =  ['body']


        widgets ={
        #'post': forms.TextInput(attrs = {'value':'', 'type':'hidden'}),
        'body' : forms.Textarea(attrs = { 'class' : 'comment-text-field comment-field'}),
        #'name' : forms.TextInput(attrs = {'class' : 'comment-char-field comment-field'}),
        }

class comment_of_comment_frm(forms.ModelForm):
    class Meta:
        model = comment_of_comment
        fields =  ['body']
        #fields =  ['name', 'body']


        widgets ={
        'body' : forms.Textarea(attrs = { 'class' : 'comment-text-field comment-field'}),
        #'name' : forms.TextInput(attrs = {'class' : 'comment-char-field comment-field'}),
        }


class frmProfile(forms.ModelForm):
    class Meta:
        model = Profile

        #birthDate=forms.DateField(input_formats=['%d%m%Y'])
        #-up is acronyms for Update Profile
        fields =  ['bio',
        'profile_img',
         'nick',
         'sex',
         'first_name',
         'last_name',
         'race',
         'y_dna',
         'mtdna',
         'birthDate',
         'politic_views',
          'religion',
          'education',
          'slogan',
          'familial_status',
          'hobby',
          'skills',
          'profession',
          'hate',
          'love',
          'nightmare',
          'profession',
          'fantasy',

          'bestEvent',
          'worstEvent',




        ]


        widgets ={
        'bio' : forms.Textarea(attrs = {'class': 'bio'}),
        'nick' : forms.TextInput(attrs = {'class': 'nick-up signfield-v2', 'placeholder' : 'כינוי'}),
        'sex' : forms.Select(attrs = {'class' :  'sex-up signfield-v2 select-box', 'id':'sex-up'}),
        'profile_img' : forms.ClearableFileInput(attrs = {'class': 'upload-img'}),

        'first_name' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'שם פרטי'}),
        'last_name' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'שם משפחה'}),
        'race' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'גזע/מוצא'}),
        'y_dna' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'Y-dna'}),
        'mtdna' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'mtDNA'}),
        'politic_views' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'השקפה פוליטית'}),
        'religion' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'דת/אמונה'}),
         'slogan' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'משפט מחץ'}),

         'familial_status': forms.Select(attrs = {'class' :  'in-up signfield select-box', 'id':'familial-status-up'}),

         'birthDate':forms.DateInput(attrs={'class': 'in-up signfield-v2', 'type':'date'}),



         'education' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'השכלה'}),
         'hobby' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'תחביבים'}),
         'skills' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'כישורים'}),
         'profession' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'מקצוע'}),


          'hate' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'רשום מה הכי שנוא עליך'}),
          'love' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'מה אתה הכי אוהב'}),
          'nightmare' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'הסיוט הכי גדול שלך'}),
          'fantasy' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'הפנטזיה שלך'}),

          'bestEvent' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'הדבר הכי טוב שארע לי בחיים'}),
          'worstEvent' : forms.TextInput(attrs = {'class': 'in-up signfield-v2', 'placeholder' : 'החוויה הכי קשה שעברתי'}),
        }




    def __init__(self, *args, **kwargs):
        super(frmProfile, self).__init__(*args, **kwargs)
        self.fields['profile_img'].label =""
