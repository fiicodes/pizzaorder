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
   


class topping(models.Model):
    topping_description=models.CharField(max_length=200,default="")

class size(models.Model):
    size_description=models.CharField(max_length=200,default="")

class base(models.Model):
    base_description=models.CharField(max_length=200,default="")

class pizza(models.Model):
    base_id=models.ForeignKey(base,on_delete=models.CASCADE,null=True)
    size_id=models.ForeignKey(size,on_delete=models.CASCADE,null=True)
    topping_id=models.ForeignKey(topping,on_delete=models.CASCADE,null=True)
    price=models.IntegerField()



class pizzaorder(models.Model):
    pizza_id=models.ForeignKey(pizza,on_delete=models.CASCADE,null=True)
    order_id=models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    quantity=models.CharField(max_length=200,default="")



    
