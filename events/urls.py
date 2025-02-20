from django.urls import include, path
from rest_framework import routers

from events.views import EventViewSet, EventRegistrationViewSet

app_name = "events"

router = routers.DefaultRouter()

router.register("events", EventViewSet)
router.register("events-register", EventRegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
