import uuid
from django.db import models

class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    summary = models.TextField(blank=False, null=False, max_length=100)
    description = models.TextField(blank=True, null=False, max_length=500)
    creation_date = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)