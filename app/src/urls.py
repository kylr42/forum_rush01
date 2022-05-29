from django.urls import path
from .views.detail import PostDetailView
from .views.index import HomePageView
from .views.register import UserRegisterView, logout_Us

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout_Us, name='logout'),
    path('<slug:pk>/', PostDetailView.as_view(), name='articles_detail'),
]