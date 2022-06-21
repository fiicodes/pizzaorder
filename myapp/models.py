from django.db import models

# Create your models here.
class customer(models.Model):
    customer_name=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    address=models.CharField(max_length=200,default="")
    def __str__(self):
        return self.customer_name
   
   
class order(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    order_datetime= models.CharField(max_length=200,default="")

    
