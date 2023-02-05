# Generated by Django 4.1.5 on 2023-02-05 12:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_customer_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart', to='store.customer')),
                ('order_items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart', to='store.orderitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
