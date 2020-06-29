from django import forms


class ContactUsForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '5'}))

    # # for non field errors
    # def clean(self):
    #     cleaned_data = super().clean()
    #     if not (cleaned_data.get("email") or cleaned_data.get("phone_number")):
    #         raise forms.ValidationError("Please Enter Email or Phone Number")

    # # for specific field errors
    # def clean_email(self):

    #     email = self.cleaned_data.get("email")
    #     if "@edyoda.com" not in email:
    #         raise forms.ValidationError("Invalid domain")
    #     return email
