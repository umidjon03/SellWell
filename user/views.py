from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User
from .forms import MyUseerCreationForm
from django.utils.translation import gettext_lazy as _

# Create your views here.
def signupUser(request):
    form = MyUseerCreationForm()
    
    if request.method == 'POST':
        form = MyUseerCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('/')
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
            messages.error(request, _('User does not exist'))
    return render(request, 'user/login.html')

def profileUser(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'user/user-profile.html')


def logoutUser(request):
    logout(request)
    return redirect('/')