from django.contrib import admin
from django.urls import include, path
from .views import AboutPageView, HomePageView, SnackListView, SnackDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('snack/', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
]
