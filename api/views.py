from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status




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