from django.db import models

# Create your models here.


class FantasyStat(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=5)
    points = models.FloatField()
    weekly_points = models.FloatField()



    def __str__(self):
        return self.name
