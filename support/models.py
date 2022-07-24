from django.contrib.auth.models import User
from django.db import models


class Support(models.Model):
    Status = (
        (u"New", u'New'),
        (u"Completed", u'Completed'),
        (u"Review", u'Review'),
    )
    Category = (
        (u"Network", u'Network'),
        (u"Printer", u'Printer'),
        (u"CCTV", u'CCTV'),
        (u"Software", u'Software'),
        (u"Data/Files", u'Data/Files'),

    )

    # class Category(models.TextChoices):
    #     NETWORK = 1, 'Network'
    #     PRINTER = 2, 'Printer'
    #     COMPUTER = 3, 'Computer'
    #     CCTV = 4, 'CCTV'
    #     SOFTWARE = 5, 'Software'
    #     Data = 6, 'Data/Files'

    name = models.CharField('Name (User)', max_length=255)
    date_created = models.DateTimeField('Date', auto_now_add=True, null=True)
    extension = models.IntegerField('Extension')
    department = models.CharField('Department', max_length=255)
    category = models.CharField(choices=Category, max_length=120, default='Network')
    summary = models.TextField('Summary/Issue', max_length=255)
    assigned = models.CharField('Assigned To', max_length=255)
    solution = models.TextField('Solution/Remarks', max_length=500, default="")
    status = models.CharField(choices=Status, max_length=120, default='New')

    class Meta:
        verbose_name_plural = 'Tasks'
        db_table = 'support'

    def __str__(self):
        return self.name

