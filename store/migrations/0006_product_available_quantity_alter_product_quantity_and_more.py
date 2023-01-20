# Generated by Django 4.1.5 on 2023-01-19 21:54

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_subcategory_gender_product_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]