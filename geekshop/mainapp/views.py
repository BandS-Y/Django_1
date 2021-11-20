from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title' : 'myshop',
        'naviname': 'myshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title' : 'myshop - Каталог',
        'naviname': 'myshop',
        'products':[
            {'name' : 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'about' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': 23725,
             'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
        ]
    }
    return render(request, 'mainapp/products.html', context)

def base(request):
    context = {
        'naviname' : 'myshop',
        'pagehead_store' : 'myshop',
    }
    return render(request, 'mainapp/base.html', context)
