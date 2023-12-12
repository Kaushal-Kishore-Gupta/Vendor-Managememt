from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from datetime import datetime



class Vendors(APIView):
    def get(self,request):
        vendor = Vendor.objects.all()
        serializer = vendorSerializer(vendor,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer = vendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            HistoricalPerformance.objects.create(vendor=serializer.instance)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class VendorDetailView(APIView):
    def get(self,request,vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = vendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self,request,vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = vendorSerializer(vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PurchaseOrders(APIView):
    def get(self,request):
        purchase_order = PurchaseOrder.objects.all()
        serializer = purchaseOrderSerializer(purchase_order,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer = purchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PurchaseOrderDetailView(APIView):
    def get(self,request,po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = purchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    
    def calculate_on_time_delivery_rate(self, purchase_order):
        new_status = purchase_order.status
        total_completed_orders = PurchaseOrder.objects.filter(vendor=purchase_order.vendor, status='completed').count()
        old_on_time_delivery_rate = purchase_order.vendor.on_time_delivery_rate

        if new_status == 'completed':
            if datetime.now() <= purchase_order.delivery_date:
                new_on_time_delivery_rate = (old_on_time_delivery_rate * total_completed_orders + 1) / (total_completed_orders + 1)
            else:
                new_on_time_delivery_rate = old_on_time_delivery_rate * total_completed_orders / (total_completed_orders + 1)
            
            purchase_order.vendor.on_time_delivery_rate = new_on_time_delivery_rate
            purchase_order.vendor.save()

            historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=purchase_order.vendor)
            historical_performance.on_time_delivery_rate = new_on_time_delivery_rate
            historical_performance.date = datetime.now()
            historical_performance.save()

    def calculate_quality_rating_avg(self, purchase_order, quality_rating):
        old_quality_rating_avg = purchase_order.vendor.quality_rating_avg
        total_ratings=PurchaseOrder.objects.filter(vendor=purchase_order.vendor).exclude(quality_rating=None).count()
        new_quality_rating_avg = (old_quality_rating_avg * total_ratings + quality_rating) / (total_ratings + 1)
        purchase_order.vendor.quality_rating_avg = new_quality_rating_avg
        purchase_order.vendor.save()
        HistoricalPerformance.objects.filter(vendor=purchase_order.vendor).update(quality_rating_avg=new_quality_rating_avg)

    
    def put(self, request, po_id):
        purchase_order = self.get_purchase_order(po_id)

        if not purchase_order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)

        if serializer.is_valid():
            old_status = purchase_order.status
            serializer.save()

            new_status = serializer.validated_data.get('status', old_status)

            if old_status != 'completed' and new_status == 'completed':
                self.calculate_on_time_delivery_rate(purchase_order)

            #check if quality rating is present
            quality_rating = serializer.validated_data.get('quality_rating', None)
            if quality_rating:
                self.calculate_quality_rating_avg(purchase_order, quality_rating)

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VendorPerformance(APIView):
    pass



