from django.urls import path
from . import views

urlpatterns = [
    path('signin/',views.login, name='login'),
    path('signup/'.views.signup, name='signup')
]