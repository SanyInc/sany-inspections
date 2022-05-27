from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Business, Store

# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "vat", )
    list_filter = ("title", )
    prepopulated_fields = {"slug": ("title", )}

class StoreAdmin(admin.ModelAdmin):
    list_display = ("notify_number", "business", "category", "region", "address", "address_number",)
    list_filter = ("business__title", )
    prepopulated_fields = {"slug": ("notify_number", )}

admin.site.register(Business, BusinessAdmin)
admin.site.register(Store, StoreAdmin)