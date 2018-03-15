from django.forms import ModelForm

from hmt.models import Event


class NewEventCreateForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_type']

class ValueSetForm(ModelForm):
    class Meta:
        model = Event
        fields = ['value']