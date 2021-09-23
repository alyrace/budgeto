from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import SET_NULL
from django.template.defaultfilters import slugify, title
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Client(models.Model):
    PROVINCES = [
        ('AL', 'Alabama'),
        ('CA', 'Califonia'),
        ('FL', 'Florida'),
        ('IL', 'Illinois')
    ]

    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(blank=True, null=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, null=True, max_length=100)
    postalCode = models.CharField(blank=True, null=True, max_length=11)
    phone = models.CharField(blank=True, null=True, max_length=20)
    email = models.CharField(blank=True, null=True, max_length=100)
    #utility
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.clientName, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
                self.slug = slugify('{} {}'.format(self.clientName, self.uniqueId))

            self.slug = slugify('{} {}'.format(self.clientName, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())

            super(Client, self).save(*args, **kwargs)

class Product(models.Model):
    CURRENCY=[
        ('$', 'USD/AUD/NZD'),
        ('€', 'EUR'),
        ('£', 'GBP'),
        ('¥', 'CNY'),
        ('¥', 'JPY'),
        ('Kr', 'NOK'),
        ('Fr', 'CHF'),
        ('₩', 'KRW')
    ]
    title = models.CharField(null=True, blank=True, max_length=500)
    description = models.TextField(null=True, blank=True)
    quanitity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='$', max_length=100)

    #utility
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
                self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())

            super(Product, self).save(*args, **kwargs)

class Invoice(models.Model):
    TERMS =[
        ('14 days', '14 days'),
        ('30 days', '30 days'),
        ('60 days', '60 days'),
        ('today', 'today'),
        ('1 day', '1 day'),
        ('TBD', 'TDB')
    ]

    STATUS = [
        ('CURRENT', 'Current'),
        ('PENDING', 'Pending'),
        ('OVERDUE', 'Overdue'),
        ('PAID', 'Paid')   
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    dueDate = models.DateTimeField(blank=True, null=True)
    paymentTerms = models.CharField(choices=TERMS, default='TBD', max_length=100)
    status = models.CharField(choices=STATUS, default='PENDING', max_length=100)
    notes = models.TextField(null=True, blank=True)

    client = models.ForeignKey(Client, blank=True, null=True, on_delete=SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=SET_NULL)
    #utility
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
                self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())

            super(Invoice, self).save(*args, **kwargs)

class Settings(models.Model):
    PROVINCES = [
        ('AL', 'Alabama'),
        ('CA', 'Califonia'),
        ('FL', 'Florida'),
        ('IL', 'Illinois')
    ]

    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(blank=True, null=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, null=True, max_length=100)
    postalCode = models.CharField(blank=True, null=True, max_length=11)
    phone = models.CharField(blank=True, null=True, max_length=20)
    email = models.CharField(blank=True, null=True, max_length=100)

    client = models.ForeignKey(Client, blank=True, null=True, on_delete=SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=SET_NULL)
    #utility
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.clientName, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
                self.slug = slugify('{} {}'.format(self.clientName, self.uniqueId))

            self.slug = slugify('{} {}'.format(self.clientName, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())

            super(Settings, self).save(*args, **kwargs)