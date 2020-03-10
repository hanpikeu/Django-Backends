from django.contrib import admin

from covidic.models.thread_item import ThreadItem


@admin.register(ThreadItem)
class AdminInterfaceThreadItem(admin.ModelAdmin):
    list_display = ['thread_item_id', 'create_user', 'created_time', 'modified_time']

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = []
        if obj is not None:
            read_only_fields += ['create_user', 'parent_thread']
        return read_only_fields
