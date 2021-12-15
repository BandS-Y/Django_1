from django.urls import path
from authapp.views import ProfileFormView,LoginListView,RegisterListView,Logout
# from authapp.views import login, register, logout, profile

app_name = 'authapp'
urlpatterns = [

    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),

    path('verify/<str:email>/<str:aktivate_key>', RegisterListView.verify, name='verify' )


    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # # path('profile/', profile, name='profile'),
    # path('logout/', logout, name='logout'),
]