from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from .forms import MyUseerCreationForm
from django.utils.translation import gettext as _

# Create your views here.
def signupUser(request):
    form = MyUseerCreationForm()
    
    if request.method == 'POST':
        form = MyUseerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, _('An error occured during registration'))
    context = {'form': form}
    return render(request, 'user/signup.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get('email')
        except:
            pass
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, _('Email or password is given wrong'))
    return render(request, 'user/login.html')


@login_required(login_url='login')
def editUser(request):
    user = request.user
    form = MyUseerCreationForm(instance=user)
    context = {'user': user, 'form': form}
    return render(request, 'user/user-edit.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')