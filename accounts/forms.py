from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile
from common.BootstrapFormMixin import BootstrapFormMixin


class SignUpForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'email')

    # def clean_email(self):
    #     email = self.cleaned_data.get('email', False)
    #     if not email:
    #         raise forms.ValidationError('Email is required')
    #     return email
