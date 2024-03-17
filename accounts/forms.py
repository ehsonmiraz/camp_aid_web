from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model=get_user_model()
        fields=['username', 'cgpa','branch','roll_no']