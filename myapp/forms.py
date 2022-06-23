from dataclasses import field
from pyexpat import model
from django import forms
from .models import *


class orderForm(forms.ModelForm):
    class Meta:
        model=order
        fields=["customer_id","order_datetime"]