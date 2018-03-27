from django.db import models


class EventType(models.Model):
    INC = 0
    THREE_POINTS = 3
    FIVE_POINTS = 5
    TEN_POINTS = 10
    CHOICES = ((INC, "incremental"), (THREE_POINTS, "three_points"), (FIVE_POINTS, "five_points"),
               (TEN_POINTS, "ten_points"))
    event_name = models.CharField(max_length=255)
    calculation_type = models.IntegerField(choices=CHOICES, default=INC)


class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    value = models.IntegerField()

    #TODO
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)
