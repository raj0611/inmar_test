

from django.db import models

class Emp(models.Model):
    ''' emp model'''
    location = models.CharField(max_length = 60)
    department = models.CharField(max_length = 60)
    category = models.CharField(max_length = 60)
    subcategory = models.CharField(max_length = 60)


    def __str__(self):
        return self.location