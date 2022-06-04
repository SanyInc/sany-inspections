from django.contrib import admin
from .models import Activity, TypeOfActivity, Category, Choice, Question

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "order", )
    list_filter = ("title", )
    # prepopulated_fields = {"slug": ("title", )}

class TypeOfActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "activity", )
    list_filter = ("title", "activity",)
    # prepopulated_fields = {"slug": ("title", )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "activity",)
    list_filter = ("activity__title", )
    # prepopulated_fields = {"slug": ("title", )}

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "get_choices","is_important", )
    list_filter = ("category__activity__title",)
    # prepopulated_fields = {"slug": ("title", )}

admin.site.register(Activity, ActivityAdmin)
admin.site.register(TypeOfActivity, TypeOfActivityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
