from django.db import models

class EventType(models.Model):
    CHOICES = ((0, "incremental"), (3, "three_points"), (5, "five_points"),
               (10, "ten_points"))
    event_name = models.CharField(max_length=255)
    calculation_type = models.IntegerField(choices=CHOICES, default=0)


class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    value = models.IntegerField()




