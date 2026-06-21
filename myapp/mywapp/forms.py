from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ExtendedRegisterForm(forms.ModelForm):
    email = forms.EmailField(
        required=True, 
        label="Электронная почта",
        widget=forms.TextInput() 
    )
    
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже зарегистрирован.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data["email"].lower()
        if commit:
            user.save()
        return user