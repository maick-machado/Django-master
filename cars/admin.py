from django.contrib import admin
from cars.models import Cars, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')
    
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'year', 'value')
    search_fields = ('model',)

admin.site.register(model_or_iterable=Brand, admin_class=BrandAdmin)
admin.site.register(model_or_iterable=Cars, admin_class=CarAdmin)
