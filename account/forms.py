from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput())
    last_name = forms.CharField(max_length=150, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]
        help_texts = {
            'username': 'Letters, digits and @/./+/-/_ only.',
            'password2': 'Enter the same password as before, for verification.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "bio", "pic"]

    def clean_pic(self):
        pic = self.cleaned_data.get("pic")
        if pic and pic.size > (102400):  # 100 KB
            raise forms.ValidationError("Image size greater than 100 KB")
        return pic
