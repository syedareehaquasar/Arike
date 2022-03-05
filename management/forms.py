from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["password1"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["email"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["phone"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["role"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta:
        model = MyUser
        fields = ("full_name", "email", "phone", "is_verified", "role")

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUser
        fields = ("full_name", "email", "phone", "is_verified", "role")