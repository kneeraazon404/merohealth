from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.db.models import fields

UserModel = get_user_model()
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Account, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Add a valid email address.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "required": True,
                "placeholder": "Enter a valid email address",
            },
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
                "placeholder": "Enter your first name",
            },
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
                "placeholder": "Enter your last name",
            },
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
                "placeholder": "Enter a phone number",
            },
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": True,
                "placeholder": "Enter your username",
            },
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "required": True,
                "placeholder": "Enter your password",
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "required": True,
                "placeholder": "Confirm your password",
            }
        ),
    )

    class Meta:
        model = UserModel
        fields = "__all__"

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
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "required": True,
                "placeholder": "Enter Your Password",
            }
        ),
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


class UserProfileUpdateForm(forms.ModelForm):
    #! Data Below
    smoking_choices = [
        ("yes", "Yes"),
        ("no", "No"),
        ("Sometimes", "Sometimes"),
        ("Prefer not to say", "Prefer not to say"),
    ]
    drink_choices = [
        ("yes", "Yes"),
        ("no", "No"),
        ("Sometimes", "Sometimes"),
        ("Prefer not to say", "Prefer not to say"),
    ]
    provience_choices = [
        ("provience 1", "Provience 1"),
        ("provience 2", "Provience 2"),
        ("provience 2", "Provience 3"),
        ("provience 4", "Provience 4"),
        ("provience 5", "Provience 5"),
        ("provience 6", "Provience 6"),
        ("provience 7", "Provience 7"),
        ("provience 8", "Provience 8"),
    ]
    district_choices = [
        ("pokhara", "pokhara"),
        ("lalitpur", "lalitpur"),
        ("kathmandu", "kathmandu"),
        ("bhaktapur", "bhaktapur"),
        ("Lalitpur", "Lalitpur"),
        ("Syanja", "Syanja"),
        ("palpa", "palpa"),
        ("Ramechhap", "Ramechhap"),
    ]
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
        ("Prefer not to say", "Prefer not to say"),
    ]
    origin_choices = [
        ("Nepali", "Nepali"),
        ("Indian", "Indian"),
        ("Americal", "kathmandu"),
    ]

    mun_choices = [
        ("Fulbari", "Fulbari"),
        ("Kadabari", "Kadabari"),
        ("Aiselu Ghari", "Aiselu Ghari"),
        ("Baghbazaar", "Baghbazaar"),
        ("Lamachaur", "Lamachaur"),
        ("Syanja", "Syanja"),
        ("palpa", "palpa"),
        ("Ramechhap", "Ramechhap"),
    ]

    drug_choices = [
        ("yes", "Yes"),
        ("no", "No"),
        ("Sometimes", "Sometimes"),
        ("Prefer not to say", "Prefer not to say"),
    ]

    blood_choices = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O-", "O-"),
        ("O+", "O+"),
    ]
    #! Data Above
    profile_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "id": "profileImage",
                "required": False,
                "id": "imageUpload",
                "type": "file",
                "name": "profile_photo",
                "placeholder": "Photo",
                "required": False,
            }
        )
    )
    birthday = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "Your Birthday",
                "class": "form-control",
                "id": "birthday",
                "required": False,
            }
        )
    )

    height = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Height (in Ft.In.)",
                "id": "username",
                "required": False,
            }
        )
    )
    weight = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Weight",
                "id": "username",
                "required": False,
            }
        )
    )

    blood_type = forms.ChoiceField(
        choices=blood_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )

    gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    origin = forms.ChoiceField(
        choices=origin_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    ward_no = forms.ChoiceField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        )
    )
    local_area = forms.ChoiceField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        )
    )
    municipality = forms.ChoiceField(
        choices=mun_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    provience = forms.ChoiceField(
        choices=provience_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "required": False,
            }
        ),
    )
    district = forms.ChoiceField(
        choices=district_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    smoking = forms.ChoiceField(
        choices=smoking_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    drinks = forms.ChoiceField(
        choices=drink_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    drugs = forms.ChoiceField(
        choices=drug_choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "type": "text",
                "required": False,
            }
        ),
    )
    social_links_fb = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "required": False,
            }
        )
    )
    social_links_tw = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "required": False,
            }
        )
    )
    social_links_ins = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "required": False,
            }
        )
    )
    social_links_yt = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "id": "fname",
                "placeholder": "Your Youtube Link",
                "required": False,
            }
        )
    )
    social_links_lnk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "id": "fname",
                "placeholder": "Your Youtube Link",
                "required": False,
            }
        )
    )
    social_links_pws = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "id": "fname",
                "placeholder": "Your Youtube Link",
                "required": False,
            }
        )
    )

    class Meta:
        model = Profile
        fields = "__all__"
