# Generated by Django 4.1.5 on 2023-01-20 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_alter_newsletter_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='updated',
        ),
    ]
