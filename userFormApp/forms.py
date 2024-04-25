from django import forms


def validate_password_contains_uppercase(password):
    if not any(char.isupper() for char in password):
        raise forms.ValidationError("Password must have at least one uppercase character")


def validate_password_atleast_8chars(password):
    if len(password) < 8:
        raise forms.ValidationError("Password must be at least 8 characters")
class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), validators=[validate_password_contains_uppercase,validate_password_atleast_8chars])

    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     password = cleaned_data.get("password")
    #     if len(password) < 8 or not any(char.isupper() for char in password):
    #         raise forms.ValidationError("Password must be at least 8 characters")
    #     if not any(char.isupper() for char in password):
    #         raise forms.ValidationError("Password must have at least one uppercase character")




