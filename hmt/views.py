from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import CreateView

from hmt.forms import NewEventCreateForm, ValueSetForm
from hmt.models import Event


class EventCreateView(CreateView):
    # http_method_names = ['post']
    model = Event
    form_class = NewEventCreateForm
    # success_url = "http://127.0.0.1:8000/"
    # template_name = 'new_event_form.html'

    def render_new_event(self, request, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return HttpResponseBadRequest()

#
#
#
class ValueSetView(CreateView):
    http_method_names = ['post']
    model = Event
    form_class = ValueSetForm
    success_url = "http://127.0.0.1:8000/"


