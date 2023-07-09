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

        birthDate=forms.DateField(input_formats=['%d%m%Y'])
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
        'nick' : forms.Textarea(attrs = {'class': 'nick-up signfield', 'placeholder' : 'כינוי'}),
        'sex' : forms.Select(attrs = {'class' :  'sex-up signfield select-box', 'id':'sex-up'}),
        'profile_img' : forms.ClearableFileInput(attrs = {'class': 'upload-img'}),

        'first_name' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'שם פרטי'}),
        'last_name' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'שם משפחה'}),
        'race' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'גזע/מוצא'}),
        'y_dna' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'Y-dna'}),
        'mtdna' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'mtDNA'}),
        'politic_views' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'השקפה פוליטית'}),
        'religion' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'דת/אמונה'}),
         'slogan' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'משפט מחץ'}),

         'familial_status': forms.Select(attrs = {'class' :  'in-up signfield select-box', 'id':'familial-status-up'}),

         'birthDate':forms.DateInput(attrs={'class': 'in-up signfield', 'type':'date'}, format=['%d/%m/%Y']),



         'education' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'השכלה'}),
         'hobby' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'תחביבים'}),
         'skills' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'כישורים'}),
         'profession' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'מקצוע'}),


          'hate' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'רשום מה הכי שנוא עליך'}),
          'love' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'מה אתה הכי אוהב'}),
          'nightmare' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'הסיוט הכי גדול שלך'}),
          'fantasy' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'הפנטזיה שלך'}),

          'bestEvent' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'הדבר הכי טוב שארע לי בחיים'}),
          'worstEvent' : forms.Textarea(attrs = {'class': 'in-up signfield', 'placeholder' : 'החוויה הכי קשה שעברתי'}),
        }




    def __init__(self, *args, **kwargs):
        super(frmProfile, self).__init__(*args, **kwargs)
        self.fields['profile_img'].label =""
