from django.contrib import admin
from .models import Inspection, Answer, Complete

# Register your models here.


class InspectionAdmin(admin.ModelAdmin):
    list_display = ("store", "inspector",
                    "uuid", "date_created", )
    list_filter = ()
    readonly_fields = ('store', 'inspector', 'uuid', 'date_created',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "body", "timestamp", 'inspection')
    list_filter = ("timestamp", )
    # readonly_fields = ('inspection', 'question', 'body', 'timestamp', )


class CompleteAdmin(admin.ModelAdmin):
    list_display = ("inspection", "score", "completed")
    list_filter = ("completed", "inspection__store__state")
    readonly_fields = ('inspection', 'score', 'completed',)


admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Complete, CompleteAdmin)
