from re import template
from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic.edit import View
from django.views.generic.base import TemplateView
from django.views import View
from  myapp.forms import orderForm


# Create your views here.

class index(TemplateView):
    template_name = 'index.html'
class CustomerView(View):
    
    def get(self,request):
        
        return render(request, "customer.html")
    def post(self,request):
        customer_name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        
        add = customer(customer_name=customer_name,phone=phone,address=address)
                
        add.save()
        return HttpResponseRedirect('/')

       
                
        
           


class OrderView(View):
    
    def get(self,request):
        c=customer.objects.all()
        return render(request, "saveorder.html",{"customer":c})
    def post(self,request):
        orderdatetime = request.POST["datetime"]

        cid=request.POST.get('customers')
        customers=customer.objects.get(id=cid)
        add = order(customer_id=customers,order_datetime=orderdatetime)
                
        add.save()
        return HttpResponseRedirect('/')

           


class PizzaView(View):
    
    def get(self,request):
        b=base.objects.all()
        s=size.objects.all()
        t=topping.objects.all()


        return render(request, "savepizza.html",{"base":b,"size":s,"topping":t})
    def post(self,request):
       

        baseid=request.POST.get('bases')
        bases=base.objects.get(id=baseid)
        sizeid=request.POST.get('sizes')
        sizes=size.objects.get(id=sizeid)
        toppingid=request.POST.get('toppings')
        toppings=topping.objects.get(id=toppingid)
        price = request.POST["price"]
        add = pizza(base_id=bases,topping_id=toppings,size_id=sizes,price=price)
                
        add.save()
        return HttpResponseRedirect('/')


class PizzaOrderView(View):
    
    def get(self,request):
        p=pizza.objects.all()
        o=order.objects.all()
       


        return render(request, "savepizzaorder.html",{"pizza":p,"order":o})
    def post(self,request):
       

        pizzaid=request.POST.get('pizzas')
        pizzas=pizza.objects.get(id=pizzaid)
        orderid=request.POST.get('orders')
        orders=order.objects.get(id=orderid)
       
        quantity = request.POST["quantity"]
        add = pizzaorder(pizza_id=pizzas,order_id=orders,quantity=quantity)
                
        add.save()
        return HttpResponseRedirect('/')






class ToppingView(View):
    
    def get(self,request):
       
        return render(request, "savetopping.html")
    def post(self,request):
        topping_description = request.POST["description"]
        check=topping.objects.filter(topping_description=topping_description)
        if check:
            return render("savetopping.html",{"msg":'Already added'})
        else:


        
            add = topping(topping_description=topping_description)
                    
            add.save()
            return HttpResponseRedirect('/')







       
class SizeView(View):
    
    def get(self,request):
       
        return render(request, "savesize.html")
    def post(self,request):
        size_description = request.POST["description"]
        check=size.objects.filter(size_description=size_description)
        if check:
            
            return render("savesize.html")
        else:


            
            add = size(size_description=size_description)
                    
            add.save()
            return HttpResponseRedirect('/')

class BaseView(View):
    
    def get(self,request):
       
        return render(request, "savebase.html")
    def post(self,request):
        base_description = request.POST["description"]
        check=base.objects.filter(base_description=base_description)
        if check:
            
            return render("savebase.html")
        else:


            
            add = base(base_description=base_description)
                    
            add.save()
            return HttpResponseRedirect('/')

       
               
        
           
     

