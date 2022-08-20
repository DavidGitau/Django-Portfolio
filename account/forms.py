from attr import field
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from eduback.forms import ButtonLayout
from crispy_forms.layout import (
    Div,
    Field,
    Layout,
    Reset,
    Submit,
)

class EditForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper

        self.helper.layout = Layout(
            Field('username', placeholder='Enter preffered unique username'),
            Field('first_name', placeholder='Enter First name'),
            Field('last_name', placeholder='Last name'),
            Field('email', placeholder='Enter your emaail'),
            Field('password1', placeholder='Enter password'),
            Field('password2', placeholder='Confirm password'),
            ButtonLayout(),
        )
class ResetForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.user = User.objects.get(id=1)