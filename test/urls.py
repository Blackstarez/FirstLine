from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enroll', views.saveTest, name='enroll'),
]
