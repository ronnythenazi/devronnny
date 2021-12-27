from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpFrm(UserCreationForm):
    email = forms.EmailField(required=False, widget = forms.EmailInput(attrs = {'class':'signfield'}))
    first_name = forms.CharField(required=False, max_length = 100, widget = forms.TextInput(attrs = {'class':'signfield'}))
    last_name = forms.CharField(required=False, max_length = 100, widget = forms.TextInput(attrs = {'class':'signfield'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpFrm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'signfield en'
        self.fields['password1'].widget.attrs['class'] = 'signfield en'
        self.fields['password2'].widget.attrs['class'] = 'signfield en'

        self.fields['username'].label ="שם משתמש"
        self.fields['password1'].label ="סיסמה"
        self.fields['password2'].label ="הזן סיסמה שוב"
        self.fields['email'].label ="מייל/דואר אלקטרוני"
        self.fields['first_name'].label ="שם"
        self.fields['last_name'].label ="כינוי"


class UsrUpdateFrm(UserChangeForm):
    email = forms.EmailField(required=False, widget = forms.EmailInput(attrs = {'class':'signfield'}))
    first_name = forms.CharField(required=False, max_length = 100, widget = forms.TextInput(attrs = {'class':'signfield'}))
    last_name = forms.CharField(required=False, max_length = 100, widget = forms.TextInput(attrs = {'class':'signfield'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UsrUpdateFrm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'signfield en'
        #self.fields['password1'].widget.attrs['class'] = 'signfield en'
        #self.fields['password2'].widget.attrs['class'] = 'signfield en'

        self.fields['username'].label ="שם משתמש"
        #self.fields['password1'].label ="סיסמה"
        #self.fields['password2'].label ="הזן סיסמה שוב"
        self.fields['email'].label ="מייל/דואר אלקטרוני"
        self.fields['first_name'].label ="שם"
        self.fields['last_name'].label ="כינוי"


class UpdatePasswordFrm(PasswordChangeForm):
    old_password = forms.CharField(required=False, widget = forms.PasswordInput(attrs = {'class':'signfield en', 'type' : 'password'}))
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
