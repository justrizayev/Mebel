from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

# Create your views here.
from dashboard.models import User
from sayt.models import Category


def index(requests):
    user = requests.user

    if user.is_anonymous:
        return redirect('dashboard_login')
    ctx = {
        'home': True
    }
    if not user.is_staff:
        ctx['staff'] = False

    else:
        ctx['staff'] = True

    return render(requests, 'dashboard/base.html', ctx)


def dash_register(requests):
    if requests.POST:
        username = requests.POST.get('username')
        name = requests.POST.get('name')
        password = requests.POST.get('password')
        password_conf = requests.POST.get('password_conf')

        if password != password_conf:
            return redirect('dashboard_register')

        user = User()
        user.name = name
        user.username = username
        user.set_password(password)
        user.save()

        login(requests, user)
        authenticate(requests)
        return redirect('dashboard')

    return render(requests, 'dashboard/register.html')


def dash_login(requests):
    if requests.POST:
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        user = User.objects.filter(username=username).first()
        if not user:
            raise ValueError('User Topilmadi')

        if not user.check_password(password):
            raise ValueError('Parol Topilmadi')
        login(requests, user)
        return redirect('dashboard')

    return render(requests, 'dashboard/login.html')


def dash_logout(requests):
    logout(requests)

    return redirect("dashboard_login")
