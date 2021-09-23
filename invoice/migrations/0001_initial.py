# Generated by Django 3.2.7 on 2021-09-23 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, choices=[('AL', 'Alabama'), ('CA', 'Califonia'), ('FL', 'Florida'), ('IL', 'Illinois')], max_length=100, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=11, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quanitity', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('$', 'USD/AUD/NZD'), ('€', 'EUR'), ('£', 'GBP'), ('¥', 'CNY'), ('¥', 'JPY'), ('Kr', 'NOK'), ('Fr', 'CHF'), ('₩', 'KRW')], default='$', max_length=100)),
                ('uniqueId', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, choices=[('AL', 'Alabama'), ('CA', 'Califonia'), ('FL', 'Florida'), ('IL', 'Illinois')], max_length=100, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=11, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.client')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.product')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('dueDate', models.DateTimeField(blank=True, null=True)),
                ('paymentTerms', models.CharField(choices=[('14 days', '14 days'), ('30 days', '30 days'), ('60 days', '60 days'), ('today', 'today'), ('1 day', '1 day'), ('TBD', 'TDB')], default='TBD', max_length=100)),
                ('status', models.CharField(choices=[('CURRENT', 'Current'), ('PENDING', 'Pending'), ('OVERDUE', 'Overdue'), ('PAID', 'Paid')], default='PENDING', max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.client')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.product')),
            ],
        ),
    ]
