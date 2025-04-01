from django.db import models

# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]

    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'Pending')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title