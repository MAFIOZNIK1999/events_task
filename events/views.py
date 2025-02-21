from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from events.filters import EventFilter
from events.models import Event, EventRegistration
from events.serializers import EventSerializer, EventRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter


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
