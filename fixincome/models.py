from django.db import models
import datetime

class Treasury_Yield(models.Model):
    asset_code = models.CharField(max_length=32)
    maturity = models.FloatField()
    issuedate = models.DateField(default=datetime.date.today, blank=True)
    couponrate = models.FloatField()
    price = models.FloatField()
    yeild = models.FloatField()