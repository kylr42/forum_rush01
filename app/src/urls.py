from django.urls import path
from .views.detail import Detail
from .views.index import Index
from .views.register import Register

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<slug:pk>/', Detail.as_view(), name='articles_detail'),
    path('register/', Register.as_view(), name='register'),
    # path('logout/', views.logout_Us, name='logout'),
]