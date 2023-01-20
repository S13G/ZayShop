# Generated by Django 4.1.5 on 2023-01-20 12:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_newsletter_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=300, null=True, unique=True)),
                ('subject', models.CharField(max_length=500, null=True)),
                ('message', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
