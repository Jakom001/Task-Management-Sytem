from django.db import models


class Support(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1, 'New'
        COMPLETED = 2, 'Completed'
        ARCHIVED = 3, 'Review'

    class Category(models.TextChoices):
        NETWORK = 1, 'Network'
        PRINTER = 2, 'Printer'
        COMPUTER = 3, 'Computer'
        CCTV = 4, 'CCTV'
        SOFTWARE = 5, 'Software'
        Data = 6, 'Data/Files'

    name = models.CharField('Name (User)', max_length=255)
    date_created = models.DateTimeField('Date', auto_now_add=True, null=True)
    extension = models.IntegerField('Extension')
    department = models.CharField('Department', max_length=255)
    category = models.CharField(choices=Category.choices, max_length=24, default=1)
    summary = models.TextField('Summary/Issue', max_length=255)
    assigned = models.CharField('Assigned To', max_length=255)
    solution = models.TextField('Solution/Remarks', max_length=500, default="")
    status = models.PositiveSmallIntegerField(choices=Status.choices, default='1')

    class Meta:
        verbose_name_plural = 'Tasks'
    def __str__(self):
        return self.name
