from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def SignUp(request):
    if(request.method == "POST"):
        form = NewUserForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            messages.success(request, "Successfully Infiltrated")
            return redirect("/registration/success")
    else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})


def Login(request):
    if(request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})

def Logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("/registration/login/")

def SignUpSuccess(request):
    return render(request, 'registration/signUpSuccess.html')





# if(request.method == 'POST'):
#         form = NewUserForm(request.POST)
#         if(form.is_valid):
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration Successful.")
#             return redirect('main:homepage')
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
    