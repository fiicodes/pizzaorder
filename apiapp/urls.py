from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiapp import views

urlpatterns = [
	path('customers/', views.CustomerList.as_view()),
	path('customers/<int:id>/', views.CustomerDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
	path('orders/<int:id>/', views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
