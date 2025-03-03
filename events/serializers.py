from rest_framework import serializers

from events.models import Event, EventRegistration
from user.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "location", "organizer"]


class EventListSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "date", "location"]


class EventDetailSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "location", "organizer"]


class EventRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = EventRegistration
        fields = ["id", "event", "user", "username", "registered_at"]
        read_only_fields = ["registered_at"]


class EventRegistrationListSerializer(EventRegistrationSerializer):
    title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = EventRegistration
        fields = ["id", "title", "username", "registered_at"]


class EventRegistrationDetailSerializer(serializers.ModelSerializer):
    event = EventListSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = EventRegistration
        fields = ["id", "event", "user", "registered_at"]
