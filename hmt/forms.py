from django.forms import ModelForm

from hmt.models import Event, EventType


# class NewEventTypeCreateForm(ModelForm):
#     class Meta:
#         model = EventType
#         fields = ['event_name']

class ValueSetForm(ModelForm):
    class Meta:
        model = Event
        fields = ['value']