from decimal import Decimal

from django.db.models import Q
from django.forms import TextInput
import django_filters

from support.models import Support


class SupportFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method="universal_search",
        label="",
        widget=TextInput(attrs={"placeholder": "Search..."}),
    )

    class Meta:
        model = Support
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Support.objects.filter(Q(extension=value) | Q(status=value))

        return Support.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value) | Q(assigned__icontains=value) | Q(status__icontains=value)
        )