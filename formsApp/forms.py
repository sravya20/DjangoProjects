from django import forms


class UserRegistrationForm(forms.Form):
    GENDER = [('Male', 'Male'), ('Female', 'Female')]
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                required=False)
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField()  #widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    gender = forms.CharField(widget=forms.Select(choices=GENDER, attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    ssn = forms.IntegerField()  #widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SSN'}))

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        firstName = cleaned_data.get('firstName')
        if len(firstName) > 20:
            raise forms.ValidationError('First Name must be less than 20 characters')
        email = cleaned_data.get('email')
        if email.find('@') == -1:
            raise forms.ValidationError('Email must contain @')

    # def clean_firstName(self):
    #     inputFirstName = self.cleaned_data['firstName']
    #     if len(inputFirstName) > 20:
    #         raise forms.ValidationError('First Name must be less than 20 characters')
    #     return inputFirstName
    #
    # def clean_email(self):
    #     inputEmail = self.cleaned_data['email']
    #     if inputEmail.find('@') == -1:
    #         raise forms.ValidationError('Email must contain @')
    #     return inputEmail
    #
    # def clean_ssn(self):
    #     inputSsn = self.cleaned_data['ssn']
