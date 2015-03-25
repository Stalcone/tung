from django.contrib import admin

from . import models


admin.site.register(models.Coll)
admin.site.register(models.Item)
