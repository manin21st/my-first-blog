from rest_framework import serializers
from .models import *

class LoginTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginT
        fields = '__all__'

class SalesPvsrCySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPvsrCy
        fields = '__all__'

class SalesPvsrCymSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPvsrCym
        fields = '__all__'

class SalesPvsrYmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPvsrYm
        fields = '__all__'

class SumLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SumLog
        fields = '__all__'
