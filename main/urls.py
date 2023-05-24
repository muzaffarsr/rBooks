from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('book/<bid>/', views.book, name='book'),
    path('filter/<cid>', views.filter, name='filter'),
]
