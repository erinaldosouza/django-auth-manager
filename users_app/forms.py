from django import forms

from users_app.models import UserApp


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserApp
        fields = ('login', 'name', 'last_name', 'password')
