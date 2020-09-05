from django.db import models


# Create your models here.


class AllPlacesInfo(models.Model):
    place_name = models.CharField(max_length=50, null=True)
    distance = models.IntegerField(blank=False)

    def __str__(self):
        return self.place_name


class AgentsInfo(models.Model):
    agent_id = models.IntegerField(blank=False)
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    zip_code = models.IntegerField(blank=False)
    state = models.CharField(max_length=50, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
