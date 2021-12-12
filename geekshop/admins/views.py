from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin, ProductsForm, ProductUpdate
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product
from mainapp.models import ProductCategory

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView

class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'

#Users
class UserListView(ListView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Администрирование | Пользователи'

class UserCreateView(CreateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Администрирование | Создание пользователя'

class UserUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Администрирование | Обновление пользователя'

class UserDeleteView(DeleteView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Администрирование | Удаление пользователя'

    def delete(self, request, *args, **kwargs):
        self.object =self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# Category
class CategoryListView(ListView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'Администрирование | Список категорий'


    def get_queryset(self):
        if self.kwargs:
           return ProductCategory.objects.filter(id=self.kwargs.get('pk'))
        else:
           return ProductCategory.objects.all()

class CategoryDeleteView(DeleteView,CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class CategoryUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryUpdateFormAdmin
    title = 'Администрирование | Обновление категории'
    success_url = reverse_lazy('admins:admin_category')

class CategoryCreateView(CreateView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category')
    form_class = CategoryUpdateFormAdmin
    title = 'Администрирование | Создание категории'

# Product
class ProductListView(ListView,BaseClassContextMixin,CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'Администрирование | Обновление категории'

class ProductsUpdateView(UpdateView, BaseClassContextMixin,CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductsForm
    title = 'Администрирование | Обновление продукта'
    success_url = reverse_lazy('admins:admins_product')

class ProductsCreateView(CreateView, BaseClassContextMixin,CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductsForm
    title = 'Администрирование | Создание продукта'
    success_url = reverse_lazy('admins:admins_product')

class ProductsDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    success_url = reverse_lazy('admins:admins_product')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# class CategoryDeleteView(DeleteView,BaseClassContextMixin,CustomDispatchMixin):
#     model = ProductCategory
#     template_name = 'admins/admin-category-update-delete.html'
#     success_url = reverse_lazy('admins:admin_category')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_active = False if self.object.is_active else True
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'admins/admin.html')
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request,'admins/admin-users-read.html',context)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'MyShop - Админ | Регистрация',
#         'form':form
#     }
#     return render(request,'admins/admin-users-create.html',context)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request,pk):
#
#     user_select = User.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#         'title': 'MyShop - Админ | Обновление',
#         'form':form,
#         'user_select':user_select
#     }
#     return render(request, 'admins/admin-users-update-delete.html',context)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request,pk):
#     if request.method == 'POST':
#         user = User.objects.get(pk=pk)
#         user.is_active=False
#         user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))
#
#
# def admin_category(request):
#     context = {
#         'category': ProductCategory.objects.all()
#     }
#     return render(request, 'admins/admin-category-read.html', context)
#
# def admin_category_create(request):
#     if request.method == 'POST':
#         form = CategoryUpdateFormAdmin(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category'))
#     else:
#         form = CategoryUpdateFormAdmin()
#     context = {
#         'title': 'MyShop - Админ | Создание категории',
#         'form': form
#     }
#     return render(request, 'admins/admin-category-create.html', context)
#
# def admin_category_update(request,pk):
#     category_select = ProductCategory.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = CategoryUpdateFormAdmin(data=request.POST, instance=category_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category'))
#     else:
#         form = CategoryUpdateFormAdmin(instance=category_select)
#     context = {
#         'title': 'MyShop - Админ | Изменение категории',
#         'form': form,
#         'category_select': category_select
#     }
#     return render(request, 'admins/admin-category-update-delete.html', context)
#
# def admin_category_delete(request,pk):
#     if request.method == 'POST':
#         user = ProductCategory.objects.get(pk=pk)
#         user.is_active = False
#         user.save()
#     return HttpResponseRedirect(reverse('admins:admin_category'))
#
#
# def admins_product(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'admins/admin-product-read.html', context)
#
# def admins_product_create(request):
#     if request.method == 'POST':
#         form = ProductsForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admins_product'))
#     else:
#         form = ProductsForm()
#     context = {
#         'title': 'MyShop - Админ | Создание категории',
#         'form': form
#     }
#     return render(request, 'admins/admin-products-create.html', context)
#
# def admins_product_update(request,pk):
#     product_select = Product.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProductUpdate(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admins_product'))
#     else:
#         form = ProductUpdate(instance=product_select)
#     context = {
#         'title': 'MyShop - Админ | Изменение товара',
#         'form': form,
#         'product_select': product_select
#     }
#     return render(request, 'admins/admin-products-update-delete.html', context)
#
# def admins_product_delete(request,pk):
#     if request.method == 'POST':
#         user = Product.objects.get(pk=pk)
#         user.is_active = False
#         user.save()
#     return HttpResponseRedirect(reverse('admins:admins_product'))
