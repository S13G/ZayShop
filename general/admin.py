from django.contrib import admin
from general.models import Newsletter, Contact

# Register your models here.

admin.site.register([Newsletter, Contact])