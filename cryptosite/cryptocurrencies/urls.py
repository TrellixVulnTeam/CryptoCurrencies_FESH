from django.urls import path
from . import views


app_name = 'cryptocurrencies'
urlpatterns = [
    # ex: /cryptocurrencies/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /cryptocurrencies/1
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]