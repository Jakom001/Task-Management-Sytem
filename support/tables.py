import django_tables2 as tables
from .models import Support


class SupportTable(tables.Table):
    class Meta:
        model = Support
        template_name = "django_tables2/bootstrap4.html"


class SupportHTMxTable(tables.Table):
    class Meta:
        model = Support
        template_name = "tables/bootstrap_htmx_full.html"
