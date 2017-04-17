from django.contrib import admin

from .models import Formulate,Category, Materials,FormulateDetails
# Register your models here.

#model CRUD 方便用法
admin.site.register(Formulate)
admin.site.register(Category)
admin.site.register(Materials)
admin.site.register(FormulateDetails)