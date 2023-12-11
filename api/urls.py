from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('vendors/',views.Vendors.as_view()),
    path('vendors/<int:vendor_id>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase-orders/',views.PurchaseOrders.as_view()),
    path('purchase-orders/<int:po_id>/', views.PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:vendor_id>/performance/', views.VendorPerformance.as_view(), name='vendor-performance'),
]
