
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import index, products

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('mainapp.urls', namespace='mainapp')),
    path('users/', include('authapp.urls', namespace='authapp')),
    path('baskets/', include('baskets.urls', namespace='baskets')),
    path('admins/', include('admins.urls', namespace='admins')),

    path('orders/', include('ordersapp.urls', namespace='orders')),

    path('i18n/', include('django.conf.urls.i18n')),

    path('', include('social_django.urls', namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('debug/', include(debug_toolbar.urls))]
