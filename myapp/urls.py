from django.urls import path

from myapp import views
from .views import *

urlpatterns = [
    path("",index.as_view()),
  
    path("saveorder/",OrderView.as_view()),
    path("savecustomer/",CustomerView.as_view()),
    path("savetopping/",ToppingView.as_view()),
    path("savesize/",SizeView.as_view()),
    path("savebase/",BaseView.as_view()),
    path("savepizza/",PizzaView.as_view()),
    path("savepizzaorder/",PizzaOrderView.as_view()),




]