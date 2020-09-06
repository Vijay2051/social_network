from django import forms
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    """
        This is the Form model for updating the profile of the user
    """

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "bio", "country", "avatar")
