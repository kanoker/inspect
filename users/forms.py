# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if hasattr(user, 'userprofile'):
                # If UserProfile exists, update its fields
                user.userprofile.role = self.cleaned_data['role']
                user.userprofile.phone_number = self.cleaned_data['phone_number']
                user.userprofile.address = self.cleaned_data['address']
                user.userprofile.save()
            else:
                # If UserProfile does not exist, create a new one
                UserProfile.objects.create(
                    user=user,
                    role=self.cleaned_data['role'],
                    phone_number=self.cleaned_data['phone_number'],
                    address=self.cleaned_data['address'],
                )
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'role']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
