from rest_framework import serializers

from events.models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):
    organizer_name = serializers.CharField(source="organizer.username", read_only=True)

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "location", "organizer", "organizer_name"]


class EventRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = EventRegistration
        fields = ["id", "event", "user", "username", "registered_at"]
        read_only_fields = ["registered_at"]
