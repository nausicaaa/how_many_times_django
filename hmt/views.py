from django.views.generic import CreateView

from django.views.generic.detail import DetailView

from hmt.models import Event, EventType


class EventCreateView(CreateView):
    model = Event
    success_url = "http://127.0.0.1:8000/"
    # fields = ['event_type']


class EventTypeCreateView(CreateView):
    model = EventType
    fields = ['event_name']
    success_url = "http://127.0.0.1:8000/"


class EventTypeDetailView(DetailView):
    model = EventType