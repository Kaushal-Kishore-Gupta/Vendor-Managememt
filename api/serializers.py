from rest_framework import serializers
from .models import *

class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'



class purchaseOrderSerializer(serializers.ModelSerializer):
    vendor=vendorSerializer()
    
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    
    def create(self, validated_data):
        vendor_data = validated_data.pop('vendor')
        vendor = Vendor.objects.get(**vendor_data)
        purchase_order = PurchaseOrder.objects.create(vendor=vendor, **validated_data)
        return purchase_order
    


class historicalPerformanceSerializer(serializers.ModelSerializer):
    vendor=vendorSerializer()
    
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'

    def create(self, validated_data):
        vendor_data = validated_data.pop('vendor')
        vendor = Vendor.objects.get_or_create(**vendor_data)
        historical_performance = HistoricalPerformance.objects.create(vendor=vendor, **validated_data)
        return historical_performance