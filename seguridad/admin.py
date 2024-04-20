from django.contrib import admin

# Register your models here.
from seguridad.models import ExtendUser, Provincia

admin.site.register(ExtendUser)
admin.site.register(Provincia)
