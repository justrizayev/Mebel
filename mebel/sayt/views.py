from django.shortcuts import render
from .models import *
# Create your views here.


def index(requests):
    pro = Product.objects.all()

    ctx = {
        'pro': pro
    }
    return render(requests, 'sayt/index.html', ctx)