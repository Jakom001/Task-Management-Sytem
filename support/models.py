from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date
from django.db import models


class Support(models.Model):
    Status = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Review', 'Review'),
    )
    Category = (
        ("Network", 'Network'),
        ("Printer", 'Printer'),
        ("Computer", 'Computer'),
        ("Software", 'Software'),
        ("Data/Files", 'Data/Files'),

    )
    Priority = (
        ("High", 'High'),
        ("Medium", 'Medium'),
        ("Low", 'Low')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField('Name (User)', max_length=255)
    date_created = models.DateTimeField('Date_created', auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    extension = models.IntegerField('Extension')
    department = models.CharField('Department', max_length=255)
    category = models.CharField(choices=Category, max_length=120, default='Network')
    summary = models.TextField('Summary/Issue', max_length=255)
    solution = models.TextField('Solution/Remarks', max_length=500, default="")
    status = models.CharField(choices=Status, max_length=120, default='New')
    priority = models.CharField(choices=Priority, max_length=120, default='Medium')
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='assigned_tasks', default='')


    class Meta:
        verbose_name_plural = 'Tasks'
        db_table = 'support'

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Support, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
