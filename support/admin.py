from django.contrib import admin
from .models import Support


class SupportAdmin(admin.ModelAdmin):
    fields = (
    ('name', 'extension'), 'date_created', 'summary', 'assigned', 'category', 'solution', 'department', 'status')
    list_display = ('name', 'date_created', 'summary', 'assigned', 'category', 'status')
    ordering = ('name',)
    readonly_fields = ('date_created',)
    list_filter = ('date_created', 'category', 'status')
    search_fields = ('name','date_created', 'extension', 'category', 'status')


admin.site.register(Support, SupportAdmin)
