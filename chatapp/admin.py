from django.contrib import admin
from .models import OnePlace, UserDetail , UserOnePlace

# Register your models here.

admin.site.register(OnePlace)
admin.site.register(UserDetail)
admin.site.register(UserOnePlace)
