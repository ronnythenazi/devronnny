from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpFrm(UserCreationForm):
    email = forms.EmailField(required=False, widget = forms.EmailInput(attrs = {'class':'signfield en'}))
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
