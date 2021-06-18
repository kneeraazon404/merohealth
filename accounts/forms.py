from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserModel

from django.contrib.auth import get_user_model

UserModel = get_user_model()
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Add a valid email address.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "required": True,
            },
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
            },
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
            },
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
            },
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
            },
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "required": True,
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "required": True,
            }
        ),
    )

    class Meta:
        model = UserModel
        fields = [
            "username",
            "phone",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_active",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(
                username=username
            )
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "passwprd",
                "placeholder": "Enter Password",
                "class": "form-control",
                "required": True,
            },
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Enter Your Email",
                "required": True,
            }
        )
    )

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "first_name",
            "last_name",
            "phone",
            "email",
            "profile_image",
            "hide_email",
        )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(
                username=username
            )
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data["username"]
        account.email = self.cleaned_data["email"].lower()
        account.profile_image = self.cleaned_data["profile_image"]
        account.hide_email = self.cleaned_data["hide_email"]
        if commit:
            account.save()
        return account


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["profile_image"]
