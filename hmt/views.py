from django.views.generic import CreateView

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from hmt.models import Event, EventType


class EventCreateView(CreateView):
    model = Event
    success_url = "http://127.0.0.1:8000"
    fields = ['value']

    # def create_event(self):
    #     event_types = EventType.objects.all()
    #     for event_type in event_types:
    #         event = self.model(event_type=event_type, value=self.fields[0])


class EventTypeCreateView(CreateView):
    model = EventType
    fields = ['event_name', 'calculation_type']
    success_url = "http://127.0.0.1:8000/"


class EventTypeDetailView(DetailView):
    model = EventType


class EventTypesListView(ListView):
    model = EventType