from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from .forms import MyUserCreationForm, UserForm
from django.utils.translation import gettext as _
from products.models import Product

# Create your views here.
def signupUser(request):
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
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
            messages.error(request, _('Your email was not logged in'))
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
    form_personal = UserForm(instance=user)
    if request.method == 'POST':
        if request.POST.get('form_type') == 'form_personal':
            form_personal = UserForm(request.POST, request.FILES, instance=user)
            if form_personal.is_valid():
                request.user.avatar = request.FILES['file']
                form_personal.save()
                return redirect('user-edit')
        elif request.POST.get('form_type') == 'form_email':
            if request.POST.get('email1') == user.email:
                user.email = request.POST.get('email2')
                user.save()
                return redirect('user-edit')
        elif request.POST.get('form_type') == 'form_password':
            if user.check_password(request.POST.get('password1')) and request.POST.get('password2') == request.POST.get('password3'):
                user.set_password(request.POST.get('password3'))
                user.save()
    return render(request, 'user/user-edit.html', {'form_personal': form_personal})


@login_required(login_url='login')
def myProfile(request):
    products = Product.objects.all()
    user = request.user
    return render(request, 'user/my-profile.html', {'user': user, 'products': products})


def logoutUser(request):
    logout(request)
    return redirect('/')