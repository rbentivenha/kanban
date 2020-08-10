# kanban.activitis.models
from django.db import models
import datetime

class Activity (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return self.name

    def is_delayed(self):
        return self.due_date < datetime.date.today()
