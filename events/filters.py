import django_filters

from events.models import Event


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    date = django_filters.DateFilter()
    location = django_filters.CharFilter(lookup_expr="icontains")
    organizer = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Event
        fields = ["title", "date", "location", "organizer"]
