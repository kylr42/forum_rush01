from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug:pk>/', views.Detail.as_view(), name='articles_detail'),
    path('register/', views.Register.as_view(), name='register'),
]