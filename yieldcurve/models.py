from django.db import models

# Create your models here.
class Yield_curve(models.Model):
    number1 = models.CharField(max_length=30)
    number2 = models.CharField(max_length=30)
    # name = models.CharField(max_length=50)
    # pub_date = models.DateField()