from django.db import models


class Todo(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    # Add a CharField to store comma-separated tags
    tags = models.CharField(max_length=255, blank=True, help_text='Enter tags separated by commas')

    def get_tags(self):
        if self.tags:
            return self.tags.split(',')
        return []

    def set_tags(self, tags):
        self.tags = ','.join(tags)
