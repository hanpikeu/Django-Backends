from django.contrib import admin

from covidic.models.tag_of_archive import TagOfArchive


@admin.register(TagOfArchive)
class AdminInterfaceTagOfArchive(admin.ModelAdmin):
    list_display = ['tag_of_archive_id', 'name']
    fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = []
        if obj is not None:
            read_only_fields.append('name')
        return read_only_fields
