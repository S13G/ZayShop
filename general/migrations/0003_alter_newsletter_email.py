# Generated by Django 4.1.5 on 2023-01-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_alter_newsletter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=300, null=True, unique=True),
        ),
    ]
