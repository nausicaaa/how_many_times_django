from django.shortcuts import render
from django.views.generic import CreateView

from hmt.forms import NewEventCreateForm, ValueSetForm
from hmt.models import Event


class EventCreateView(CreateView):
    http_method_names = ['post']
    model = Event
    form_class = NewEventCreateForm
    success_url = "http://127.0.0.1:8000/"
    # template_name = 'new_event_form.html'

class ValueSetView(CreateView):
    http_method_names = ['post']
    model = Event
    form_class = ValueSetForm
    success_url = "http://127.0.0.1:8000/"
