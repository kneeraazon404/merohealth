from .models import LabMember
from django.contrib.auth.forms import UserCreationForm


class LabMemberForm(UserCreationForm):
    model = LabMember

    class Meta:
        fields = ["__all__"]
