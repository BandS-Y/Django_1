from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin, ProductsForm, ProductUpdate
from authapp.models import User
from mainapp.models import Product
from mainapp.models import ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'admins/admin-users-read.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'MyShop - Админ | Регистрация',
        'form':form
    }
    return render(request,'admins/admin-users-create.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request,pk):

    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'MyShop - Админ | Обновление',
        'form':form,
        'user_select':user_select
    }
    return render(request, 'admins/admin-users-update-delete.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request,pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active=False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

def admin_category(request):
    context = {
        'category': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)

def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryUpdateFormAdmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryUpdateFormAdmin()
    context = {
        'title': 'MyShop - Админ | Создание категории',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)

def admin_category_update(request,pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryUpdateFormAdmin(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryUpdateFormAdmin(instance=category_select)
    context = {
        'title': 'MyShop - Админ | Изменение категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-category-update-delete.html', context)

def admin_category_delete(request,pk):
    if request.method == 'POST':
        user = ProductCategory.objects.get(pk=pk)
        user.is_active = False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_category'))


def admins_product(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-product-read.html', context)

def admins_product_create(request):
    if request.method == 'POST':
        form = ProductsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_product'))
    else:
        form = ProductsForm()
    context = {
        'title': 'MyShop - Админ | Создание категории',
        'form': form
    }
    return render(request, 'admins/admin-products-create.html', context)

def admins_product_update(request,pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductUpdate(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_product'))
    else:
        form = ProductUpdate(instance=product_select)
    context = {
        'title': 'MyShop - Админ | Изменение товара',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'admins/admin-products-update-delete.html', context)

def admins_product_delete(request,pk):
    if request.method == 'POST':
        user = Product.objects.get(pk=pk)
        user.is_active = False
        user.save()
    return HttpResponseRedirect(reverse('admins:admins_product'))
