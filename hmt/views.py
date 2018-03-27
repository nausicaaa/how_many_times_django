import json

from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import viewsets

from hmt.models import Event, EventType
from hmt.serializers import EventTypeSerializer


class EventTypeCreateView(CreateView):
    model = EventType
    fields = ['event_name', 'calculation_type']
    success_url = "http://127.0.0.1:8000/"
    template_name = "new_event_type_form.html"


class EventTypeDetailView(DetailView):
    model = EventType


class EventTypesListView(ListView):
    model = EventType
    template_name = "list_event_types.html"


def create_event(request):
    event_type_id = int(request.POST['event_type_id'])
    event = Event.objects.create(event_type_id=event_type_id, value=request.POST['value'])
    return HttpResponse(json.dumps({'id': event.id, 'status': 'OK'}))


class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all().order_by('-date_joined')
    serializer_class = EventTypeSerializer
