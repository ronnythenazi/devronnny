from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User, Group, Permission
from django import forms

from django.contrib.auth import (authenticate, get_user_model, login, logout,)

User = get_user_model()
"""
class SignInFrm(forms.Form):
    username = forms.CharField(required=True, widget = forms.TextInput(attrs = {'class':'signfield'}))
    password = forms.CharField(required=True, widget = forms.PasswordInput(attrs = {'class':'signfield'}))


"""
class SignInFrm(forms.ModelForm):
    username = forms.CharField(required=True, widget = forms.TextInput(attrs = {'class':'signfield'}))
    password = forms.CharField(required=True, widget = forms.PasswordInput(attrs = {'class':'signfield'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        user=None


        try:
            user_obj = User.objects.filter(email=username)[0]
            username2 = user_obj.username
            user = authenticate(username=username2, password=password)
        except:
            user = authenticate(username=username, password=password)

        #if not user or not user.is_active:
        #    raise forms.ValidationError("מצטער, שם משתמש או סיסמה אינם נכונים, נסה שוב")
        if not user:
            raise forms.ValidationError("מצטער, שם משתמש או סיסמה אינם נכונים, נסה שוב")
        if not user.is_active:
            raise forms.ValidationError("חשבונך טרם הופעל, נא לחץ על הלינק שנשלח לך לתיבת המייל, בכדי שחשבונך יופעל")
        return self.cleaned_data

class SignUpFrm(forms.ModelForm):

    email = forms.EmailField(required=True, widget = forms.EmailInput(attrs = {'class':'signfield'}))
    email2 = forms.EmailField(required=True, widget = forms.EmailInput(attrs = {'class':'signfield'}))
    username = forms.CharField(required=True, widget = forms.TextInput(attrs = {'class':'signfield'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs = {'class':'signfield'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs = {'class':'signfield'}))


    class Meta:
        model = User
        fields =[
         'username',
         'email',
         'email2',
         'password',
         'password2',
         ]


    def clean_email2(self):
        if self.data['email'] != self.data['email2']:
            raise forms.ValidationError("מיילים חייבים להיות זהים")

        return self.data['email']

    def clean_email(self):
        email_qs = User.objects.filter(email = self.data['email'])
        if email_qs.exists():
            raise forms.ValidationError("המייל שבחרת תפוס")
        return self.data['email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username = username)
        if username_qs.exists():
            raise forms.ValidationError("השם משתמש שבחרת תפוס")

        elif '@' in str(username):
             raise forms.ValidationError("אסור @ בשם משתמש")

        return self.data['username']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("סיסמה שהזנת לצורך אימות שונה מהסיסמה שהזנת בשדה מעל")
        elif len(str(password)) < 8:
            raise forms.ValidationError("סיסמא חייבת להכיל לפחות 8 תוים")

        return self.data['password']



class mail_for_password_recovery_frm(forms.Form):

    email = forms.EmailField(required=True, widget = forms.EmailInput(attrs = {'class':'signfield'}))


    def clean_email(self):
        email_qs = User.objects.filter(email = self.data['email'])
        if not email_qs.exists():
            raise forms.ValidationError("המייל שבחרת לא קיים במערכת")
        if not email_qs[0].is_active:
            raise forms.ValidationError("מייל זה שייך למשתמש שחשבונו הושבת")
        return self.data['email']


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("סיסמה שהזנת לצורך אימות שונה מהסיסמה שהזנת בשדה מעל")
        elif len(str(password)) < 8:
            raise forms.ValidationError("סיסמא חייבת להכיל לפחות 8 תוים")

        return self.data['password']






class UsrUpdateFrm(UserChangeForm):
    #email = forms.EmailField(required=False, widget = forms.EmailInput(attrs = {'class':'signfield'}))
    first_name = forms.CharField(required=False, max_length = 100, widget = forms.TextInput(attrs = {'class':'signfield'}))
    last_name = forms.CharField(required=False, max_length = 100, widget = forms.TextInput(attrs = {'class':'signfield'}))

    class Meta:
        model = User
        #fields = ['username', 'first_name', 'last_name', 'email']
        fields = ['username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UsrUpdateFrm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'signfield'
        #self.fields['password1'].widget.attrs['class'] = 'signfield en'
        #self.fields['password2'].widget.attrs['class'] = 'signfield en'

        self.fields['username'].label ="שם משתמש"
        #self.fields['password1'].label ="סיסמה"
        #self.fields['password2'].label ="הזן סיסמה שוב"
        #self.fields['email'].label ="מייל/דואר אלקטרוני"
        self.fields['first_name'].label ="שם"
        self.fields['last_name'].label ="כינוי"

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username = username)
        if username_qs.exists():
            raise forms.ValidationError("השם משתמש שבחרת תפוס")

        elif '@' in str(username):
             raise forms.ValidationError("אסור @ בשם משתמש")

        return self.data['username']

class CreatePasswordFrm(forms.Form):
    new_password1 = forms.CharField(required=False, max_length = 100, widget = forms.PasswordInput(attrs = {'class':'signfield', 'type' : 'password'}))
    new_password2 = forms.CharField(required=False, max_length = 100, widget = forms.PasswordInput(attrs = {'class':'signfield', 'type' : 'password'}))

    def __init__(self, *args, **kwargs):
        super(CreatePasswordFrm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label ="סיסמה חדשה"
        self.fields['new_password2'].label = "סיסמה חדשה שוב"

    def clean_new_password2(self):
        password = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password != password2:
            raise forms.ValidationError("סיסמה שהזנת לצורך אימות שונה מהסיסמה שהזנת בשדה מעל")
        elif len(str(password)) < 8:
            raise forms.ValidationError("סיסמא חייבת להכיל לפחות 8 תוים")

        return self.data['new_password2']


class UpdatePasswordFrm(PasswordChangeForm):
    old_password = forms.CharField(required=False, widget = forms.PasswordInput(attrs = {'class':'signfield', 'type' : 'password'}))
    new_password1 = forms.CharField(required=False, max_length = 100, widget = forms.PasswordInput(attrs = {'class':'signfield', 'type' : 'password'}))
    new_password2 = forms.CharField(required=False, max_length = 100, widget = forms.PasswordInput(attrs = {'class':'signfield', 'type' : 'password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordFrm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = "סיסמה נוכחית"
        self.fields['new_password1'].label ="סיסמה חדשה"
        self.fields['new_password2'].label = "סיסמה חדשה שוב"

    def clean_new_password2(self):
        password = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password != password2:
            raise forms.ValidationError("סיסמה שהזנת לצורך אימות שונה מהסיסמה שהזנת בשדה מעל")
        elif len(str(password)) < 8:
            raise forms.ValidationError("סיסמא חייבת להכיל לפחות 8 תוים")

        return self.data['new_password2']
