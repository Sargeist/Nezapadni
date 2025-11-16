# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.html import format_html
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email")
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('parent', 'Parent')],
        required=True,
        label="Role"
    )

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            login_url = reverse_lazy("login")
            raise ValidationError(
                format_html(
                    "This email is already registered. <a href='{}'>Log in</a>.",
                    login_url,
                ),
                code="email_in_use",
            )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["email"]  # если username обязателен

        if commit:
            user.save()
        return user