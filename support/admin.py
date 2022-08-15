from django.contrib import admin
from .models import Support


class SupportAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'extension'), 'date_created', 'summary', 'assigned', 'category', 'solution', 'department', 'date_modified', 'owner',
        'status')
    list_display = ('id', 'name', 'date_created', 'summary', 'assigned', 'category', 'status')
    ordering = ('-id',)
    readonly_fields = ('date_created', 'date_modified', 'owner')
    list_filter = ('date_created', 'category', 'status')
    search_fields = ('name', 'date_created', 'extension', 'category', 'status')
    list_per_page = 15


admin.site.register(Support, SupportAdmin)
