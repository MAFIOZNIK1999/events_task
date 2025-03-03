from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from events.filters import EventFilter
from events.models import Event, EventRegistration
from events.serializers import EventSerializer, EventRegistrationSerializer, EventListSerializer, EventDetailSerializer, \
    EventRegistrationListSerializer, EventRegistrationDetailSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        if self.action == "retrieve":
            return EventDetailSerializer
        return self.serializer_class


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        user = request.user
        event_id = request.data.get("event")

        if self.queryset.filter(event_id=event_id, user=user).exists():
            return Response({"error": "You have already registered on this event"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("event", "user")
        return queryset


    def get_serializer_class(self):
        if self.action == "list":
            return EventRegistrationListSerializer
        if self.action == "retrieve":
            return EventRegistrationDetailSerializer
        return self.serializer_class
