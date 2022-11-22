from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from dashboard.Product.forms import ProductForm
from sayt.models import Product


def pro_list(requests):
    user = requests.user
    if user.is_anonymous:
        return redirect('dashboard')

    pro = Product.objects.all()

    ctx = {
        "pro": pro
    }

    return render(requests, 'dashboard/product/list.html', ctx)


def pro_detail(requests, pk):
    user = requests.user
    if user.is_anonymous:
        return redirect('dashboard')

    pro = Product.objects.get(pk=pk)

    ctx = {
        "pro": pro
    }

    return render(requests, 'dashboard/product/detail.html', ctx)


@staff_member_required(login_url="dashboard")
def pro_delete(requests, pk):
    pro = Product.objects.get(pk=pk)
    pro.delete()
    return redirect('dashboard-pro-list')


@staff_member_required(login_url="dashboard")
def product_add(requests):
    forms = ProductForm()
    if requests.POST:
        form = ProductForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-pro-list')

    ctx = {
        "forms": forms
    }
    return render(requests, 'dashboard/product/forms.html', ctx)


@staff_member_required(login_url="dashboard")
def pro_edit(requests, pk):
    root = Product.objects.get(pk=pk)
    forms = ProductForm(instance=root)

    if requests.POST:
        form = ProductForm(requests.POST, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dashboard-pro-list')

    ctx = {
        "forms": forms
    }
    return render(requests, 'dashboard/product/forms.html', ctx)


@staff_member_required(login_url="dashboard")
def pro_confirm(requests, pk):
    root = Product.objects.get(pk=pk)
    ctx = {
        "root": root
    }

    return render(requests, 'dashboard/product/confirm.html', ctx)
