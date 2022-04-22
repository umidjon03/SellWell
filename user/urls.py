from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('signup/', signupUser, name='signup'),
    path('user-edit/', editUser, name='user-edit'),
    path('logout/', logoutUser, name='logout'),
    path('my-profile/', myProfile, name='my-profile'),
]