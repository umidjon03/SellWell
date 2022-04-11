from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('signup/', signupUser, name='signup'),
    path('profile/<str:pk>', profileUser, name='profile'),
    path('logout/', logoutUser, name='logout')
]