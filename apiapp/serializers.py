
from rest_framework import serializers
from myapp.models import customer,order
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields='__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'

