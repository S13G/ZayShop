# Generated by Django 4.1.5 on 2023-02-02 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_featured_alter_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
