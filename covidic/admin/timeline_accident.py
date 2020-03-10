from django.contrib import admin

from covidic.models.timeline_accident import TimelineAccident


@admin.register(TimelineAccident)
class AdminInterfaceTimelineAccident(admin.ModelAdmin):
    list_display = ['accident_id', 'date', 'typeof', 'title_en']
