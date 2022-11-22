from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from api.v1.dashboard.user.services import ctg_list_by_api
from dashboard.Category.forms import CategoryForm
from sayt.models import Category


def ctg_list(requests):
    user = requests.user
    if user.is_anonymous:
        return redirect('dashboard')

    ctgs = ctg_list_by_api()

    ctx = {
        "ctgs": ctgs.get('items', [])
    }

    return render(requests, 'dashboard/Category/list.html', ctx)


def ctg_detail(requests, pk):
    ctg = Category.objects.get(pk=pk)
    user = requests.user
    if user.is_anonymous:
        return redirect('dashboard')

    ctx = {
        "ctg": ctg
    }

    return render(requests, 'dashboard/Category/detail.html', ctx)


@staff_member_required(login_url="dashboard")
def ctg_delete(requests, pk):
    ctg = Category.objects.get(pk=pk)
    ctg.delete()
    return redirect('dashboard-ctg-list')


@staff_member_required(login_url="dashboard")
def ctg_add(requests):
    forms = CategoryForm()
    if requests.POST:
        form = CategoryForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-ctg-list')

    ctx = {
        "forms": forms
    }
    return render(requests, 'dashboard/category/forms.html', ctx)


@staff_member_required(login_url="dashboard")
def ctg_edit(requests, pk):
    root = Category.objects.get(pk=pk)
    forms = CategoryForm(instance=root)

    if requests.POST:
        form = CategoryForm(requests.POST, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dashboard-ctg-list')

    ctx = {
        "forms": forms
    }
    return render(requests, 'dashboard/category/forms.html', ctx)


@staff_member_required(login_url="dashboard")
def ctg_confirm(requests, pk):
    root = Category.objects.get(pk=pk)
    ctx = {
        "root": root
    }

    return render(requests, 'dashboard/category/confirm.html', ctx)
