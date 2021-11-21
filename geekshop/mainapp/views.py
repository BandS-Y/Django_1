from django.shortcuts import render
from .models import ProductCategory, Product

import json
import os

MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title' : 'myshop',
        'naviname': 'myshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    products = Product.objects.all()
    # file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title' : 'myshop - Каталог',
        'naviname': 'myshop',
        'products': products,
        # 'products':[
        #     {'name' : 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
        #      'about' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      'image' : 'vendor/img/products/Adidas-hoodie.png'},
        #     {'name': 'Синяя куртка The North Face', 'price': 23725,
        #      'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
        #      'image' : 'vendor/img/products/Blue-jacket-The-North-Face.png'},
        #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
        #      'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      'image' : 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
        #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
        #      'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      'image' : 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
        #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
        #      'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      'image' : 'vendor/img/products/Black-Dr-Martens-shoes.png'},
        #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
        #      'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      'image' : 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        # ],
        # 'menu' : [
        #     {'point': 'Новинки'},
        #     {'point': 'Одежда'},
        #     {'point': 'Обувь'},
        #     {'point': 'Аксессуары'},
        #     {'point': 'Подарки'},
        # ],
    }
    # context['products'] = json.load(open(file_path, encoding='utf-8'))

    return render(request, 'mainapp/products.html', context)

def base(request):
    context = {
        'naviname' : 'myshop',
        'pagehead_store' : 'myshop',
    }
    return render(request, 'mainapp/base.html', context)
