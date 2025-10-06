# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, get_user_model
from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from .models import Profile
import logging

logger = logging.getLogger(__name__)

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('student', 'Student'), ('parent', 'Parent')], required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'role', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()
        self.fields.pop('username', None)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CustomUser.objects.filter(email=email).exists():
            login_url = reverse_lazy('login')
            error_message = format_html(
                "This email is already in use. Please use a different email or <a href='{}'>log in</a> here.",
                login_url
            )
            raise ValidationError(error_message, code='email_in_use')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            logger.debug(f"Saving user: {user.email}")
            user.save()
            logger.debug(f"User saved with ID: {user.id}")
        return user

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        logger.debug("Form is valid, processing...")
        user = form.save()
        logger.debug(f"User after form.save(): {user.email}, ID: {user.id}")
        profile, created = Profile.objects.get_or_create(user=user)
        logger.debug(f"Profile created: {created}, Role before: {profile.role}")
        profile.role = form.cleaned_data['role']
        profile.save()
        logger.debug(f"Profile after save: {profile.role}")
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        logger.debug("User logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.debug("Form is invalid, errors: %s", form.errors)
        return super().form_invalid(form)

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your email'})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy('home')  # Замените 'home' на нужный маршрут

def google_login(request):
    pass

def facebook_login(request):
    pass