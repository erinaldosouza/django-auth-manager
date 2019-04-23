from django import forms
from bcrypt import hashpw, gensalt
from users_app.models import UserApp


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserApp
        fields = ('login', 'name', 'last_name', 'password')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.password = hashpw(self.cleaned_data["password"].encode('utf-8'), gensalt(10, b"2a"))
        if commit:
            user.save()

        return user
