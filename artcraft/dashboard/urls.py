from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('index/', views.dashboardView.as_view(), name="dashboard_view"),
    path('artist/', views.artistView.as_view(), name="artist_view"),
    path('artwork/', views.artworkView.as_view(), name="artwork_view"),
    path('customer/', views.customerView.as_view(), name="customer_view"),
    path('order/', views.orderView.as_view(), name="order_view"),
]
