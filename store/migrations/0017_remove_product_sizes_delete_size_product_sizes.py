# Generated by Django 4.1.5 on 2023-02-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('F', 'Large'), ('XL', 'Xtra Large'), ('XXL', 'Xtra-Xtra Large')], default='S', max_length=3, null=True),
        ),
    ]
