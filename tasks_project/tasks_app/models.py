from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """
    This the task class
    """
    class Priority(models.TextChoices):
        high = "high", "High"
        medium = "medium", "Medium"
        low = "low", "Low"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.medium)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.priority}"

