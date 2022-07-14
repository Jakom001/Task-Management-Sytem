from django.contrib import admin
from .models import Support


class SupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'category', 'summary', 'assigned', 'solution', 'extension', 'status')

    def admin_action(self, request, queryset):
        actions = ["export_as_csv"]

        def export_as_csv(self, request, queryset):
            pass

            export_as_csv.short_description = "Export Selected"

    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        url = 'templates/admin/?pks=' + ','.join(str([q.pk for q in queryset]))

    actions = [generatePDF]


admin.site.register(Support, SupportAdmin)
