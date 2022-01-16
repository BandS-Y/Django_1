from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from django.conf import settings
from django.core import cache

import json
import os

from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.


# Комментировать для локального сервра на Винде
def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key,link_category)
        return link_category
    else:
        return ProductCategory.objects.all()

# Комментировать для локального сервра на Винде
def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key,link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')

# Комментировать для локального сервра на Винде
def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key,product)
        return product
    else:
        return Product.objects.get(id=pk)

def index(request):
    context = {
        'title': 'MyShop', }
    return render(request, 'mainapp/index.html', context)


# def products(request, is_active, id_category=None):
def products(request, id_category=None, page=1):
    context = {
        'title': 'MyShop | Каталог',
    }
    if id_category:
        # products= Product.objects.filter(category_id=id_category).select_related('category')
        # products = Product.objects.filter(category_id=id_category).select_related()
        products = Product.objects.filter(category_id=id_category).select_related('category')
    else:
        products = Product.objects.all().select_related('category')
    # if is_active:
    #     context['categories'] = ProductCategory.objects.filter(id=id_category)

    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator

    # Подключаеи для кэширвоания на сервере
    context['categories'] = get_link_category()

    # работаем без кэширования
    # context['categories'] = ProductCategory.objects.all()

    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context

