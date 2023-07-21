from django.contrib import admin
from .models import Category,Brand,Color,Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','brand','status')
    
admin.site.register(Product,ProductAdmin)


# Register your models here.
