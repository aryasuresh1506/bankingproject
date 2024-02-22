from django.contrib import admin
from .models import Forum,Branches,Register

# Register your models here.
admin.site.register(Forum)
admin.site.register(Branches)
admin.site.register(Register)