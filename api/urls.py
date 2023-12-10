from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('vendors/',views.Vendors.as_view()),
    path('vendors/<int:vendor_id>/', views.VendorDetailView.as_view(), name='vendor-detail'),
]
