
from django.urls import path

# from admins.views import index,admin_users_create,admin_users_update,admin_users_delete,admin_users
# from admins.views import  admin_category, admin_category_update, admin_category_create, admin_category_delete
# from admins.views import admins_product, admins_product_update, admins_product_create, admins_product_delete
from admins.views import IndexTemplateView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, ProductListView, ProductsUpdateView, \
    ProductsCreateView, ProductsDeleteView

app_name = 'admins'
urlpatterns = [

    path('', IndexTemplateView.as_view(),name='index'),
    path('users/', UserListView.as_view(),name='admin_users'),
    path('users-create/', UserCreateView.as_view(),name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(),name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(),name='admin_users_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_delete'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    # path('category-detail/<int:pk>/', CategoryDetailView.as_view(), name='admin_category_detail'),

    path('product/', ProductListView.as_view(), name='admins_product'),
    path('products-update/<int:pk>/', ProductsUpdateView.as_view(), name='admins_product_update'),
    path('products-create/', ProductsCreateView.as_view(), name='admins_product_create'),
    path('products-delete/<int:pk>/', ProductsDeleteView.as_view(), name='admins_product_delete'),



    # path('', index,name='index'),
    # path('users/', admin_users,name='admin_users'),
    # path('users-create/', admin_users_create,name='admin_users_create'),
    # path('users-update/<int:pk>', admin_users_update,name='admin_users_update'),
    # path('users-delete/<int:pk>', admin_users_delete,name='admin_users_delete'),
    #
    # path('category/', admin_category, name='admin_category'),
    # path('category/update/<int:pk>', admin_category_update, name='admin_category_update'),
    # path('category-create/', admin_category_create, name='admin_category_create'),
    # path('category-delete/<int:pk>', admin_category_delete, name='admin_category_delete'),
    #
    # path('product/', admins_product, name='admins_product'),
    # path('products-update/<int:pk>', admins_product_update, name='admins_product_update'),
    # path('products-create/', admins_product_create, name='admins_product_create'),
    # path('products-delete/<int:pk>', admins_product_delete, name='admins_product_delete'),

]
