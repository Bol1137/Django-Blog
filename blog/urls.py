from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('about/', views.about, name='about'),
    
]
