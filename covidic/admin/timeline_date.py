from django.contrib import admin

from covidic.models.timeline_date import TimelineDate


@admin.register(TimelineDate)
class AdminInterfaceTimelineDate(admin.ModelAdmin):
    list_display = ['date_id', 'date']

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = []
        if obj is not None:
            read_only_fields.append('data')
        return read_only_fields
