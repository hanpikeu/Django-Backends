from django.contrib import admin

from covidic.models.thread import Thread
from covidic.models.thread_item import ThreadItem


class ThreadItemInline(admin.TabularInline):
    model = ThreadItem


@admin.register(Thread)
class AdminInterfaceThread(admin.ModelAdmin):
    list_display = ['thread_id', 'title', 'create_user', 'created_time', 'modified_time']
    inlines = [
        ThreadItemInline
    ]
