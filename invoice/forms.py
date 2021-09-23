from django import forms 
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from .models import *
import json

class DateInput(forms.DateInput):
    input_type = 'date'

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['clientName', 'addressLine1', 'province', 'phone', 'postalCode', 'email']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'quantity', 'price', 'currency']

class InvoiceForm(forms.ModelForm):
    dueDate = forms.DateField(
        required =True,
        label= 'Invoice Due',
        widget = DateInput(attrs={'class': 'form-control' }),
    )    

    class Meta:
        model = Invoice
        fields = ['title', 'number', 'dueDate', 'paymentTerms', 'status', 'notes', 'client', 'product']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['clientName', 'addressLine1', 'province', 'phone', 'postalCode', 'email']