from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myapp.models import customer,order
from apiapp.serializers import CustomerSerializer,OrderSerializer

class CustomerList(APIView):
	"""
	List all customer, or create a new customer
	"""

	def get(self, request, format=None):
		customers = customer.objects.all()
		serializer = CustomerSerializer(customers, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CustomerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,
							status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
	"""
	Retrieve, update or delete a customer instance
	"""
	def get_object(self, id):
		# Returns an object instance that should
		# be used for detail views.
		try:
			return customer.objects.get(id=id)
		except customer.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		customers = self.get_object(id)
		serializer = CustomerSerializer(customers)
		return Response(serializer.data)

	def put(self, request, id, format=None):
		customers = self.get_object(id)
		serializer = CustomerSerializer(customers, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	

	def delete(self, request, id, format=None):
		customers = self.get_object(id)
		customers.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class OrderList(APIView):
	"""
	List all order, or create a new order
	"""

	def get(self, request, format=None):
		orders = order.objects.all()
		serializer = OrderSerializer(orders, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,
							status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
	"""
	Retrieve, update or delete a order instance
	"""
	def get_object(self, id):
		# Returns an object instance that should
		# be used for detail views.
		try:
			return order.objects.get(id=id)
		except order.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		orders = self.get_object(id)
		serializer = OrderSerializer(orders)
		return Response(serializer.data)

	def put(self, request, id, format=None):
		orders = self.get_object(id)
		serializer = OrderSerializer(orders, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	

	def delete(self, request, id, format=None):
		orders = self.get_object(id)
		orders.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

