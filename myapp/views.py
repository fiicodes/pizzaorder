from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def saveorder(request):
    c=customer.objects.all()
    if request.method == 'POST':
        orderdatetime = request.POST["datetime"]

        cid=request.POST.get('customers')
        customers=customer.objects.get(id=cid)
        add = order(customer_id=customers,order_datetime=orderdatetime)
        
        add.save()
        return HttpResponseRedirect('/saveorder/')
    else:
        return render(request, "saveorder.html",{"customer":c})