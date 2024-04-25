from django.shortcuts import render

from . import forms


# Create your views here.
def userLogin(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
    return render(request,"userFormsApp/userLoginForm.html", {'form':form})