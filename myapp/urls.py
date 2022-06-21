from django.urls import path

from myapp import views

urlpatterns = [
  
    path("saveorder/",views.saveorder,name="saveorder")
]