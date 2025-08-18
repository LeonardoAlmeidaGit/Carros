from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
# Registando o modelo carro
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

class BrandAmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAmin)
