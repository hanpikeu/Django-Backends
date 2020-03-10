from django.contrib import admin

from covidic.models.log import Log


@admin.register(Log)
class AdminInterfaceLog(admin.ModelAdmin):
    list_display = ['log_id', 'log_time', 'log_id']

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = []
        if obj is not None:
            read_only_fields.append('typeof')
        return read_only_fields
