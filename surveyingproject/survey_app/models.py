from django.db import models

class MarkedPosition(models.Model):
    Latitude = models.DecimalField(max_digits=15, decimal_places=7)
    Longitude = models.DecimalField(max_digits=15, decimal_places=7)
    Notes = models.CharField(max_length=2000)
    
