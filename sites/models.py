from django.db import models
from django.utils import timezone

class Sites(models.Model):
    site_name = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.site_name

class Values(models.Model):
    site = models.ForeignKey(Sites)
    valueA  = models.IntegerField(default=0)
    valueB = models.IntegerField(default=0)
    entry_date = models.DateField('date inserted')
    def __str__(self):              # __unicode__ on Python 2
        return str(self.entry_date)

        

        