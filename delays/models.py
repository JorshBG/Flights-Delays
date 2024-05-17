from django.db import models


class Airlines(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=50)


class Airports(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)


class Flights(models.Model):
    airline = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    flight = models.BigIntegerField()
    airportFrom = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="airportFrom", null=True)
    airportTo = models.ForeignKey(Airports, on_delete=models.CASCADE, null=True)
    dayOfTheWeek = models.IntegerField()
    time = models.BigIntegerField()
    length = models.IntegerField()
    delay = models.BooleanField(default=False)
