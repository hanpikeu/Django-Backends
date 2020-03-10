from django.contrib import admin

from covidic.models.archive import Archive


@admin.register(Archive)
class AdminInterfaceArchive(admin.ModelAdmin):
    list_display = ['archive_id', 'typeof', 'tags', 'link']
    readonly_fields = ['tags']
