from django.db import models

class WeatherStats(models.Model):
    fecha = models.DateField(blank=True, null=True)
    indicativo = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100,blank=True, null=True)
    provincia = models.CharField(max_length=100,blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    tmed = models.FloatField(blank=True, null=True)
    prec = models.FloatField(blank=True, null=True)
    tmin = models.FloatField(blank=True, null=True)
    horatmin = models.TimeField(blank=True, null=True)
    tmax = models.FloatField(blank=True, null=True)
    horatmax = models.TimeField(blank=True, null=True)
    dir = models.IntegerField(blank=True, null=True)
    velmedia = models.FloatField(blank=True, null=True)
    racha = models.FloatField(blank=True, null=True)
    horaracha = models.TimeField(blank=True, null=True)
    presMax = models.FloatField(blank=True, null=True)
    horaPresMax = models.CharField(max_length=100, blank=True, null=True)
    presMin = models.FloatField(blank=True, null=True)
    horaPresMin = models.IntegerField(blank=True, null=True)
    sol = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    station = models.CharField(max_length=100, blank=True, null=True)



# class BaseWeatherStats(models.Model):
#     fecha = models.DateField(blank=True, null=True)
#     indicativo = models.CharField(max_length=100, blank=True, null=True)
#     nombre = models.CharField(max_length=100,blank=True, null=True)
#     provincia = models.CharField(max_length=100,blank=True, null=True)
#     altitud = models.IntegerField(blank=True, null=True)
#     tmed = models.FloatField(blank=True, null=True)
#     prec = models.FloatField(blank=True, null=True)
#     tmin = models.FloatField(blank=True, null=True)
#     horatmin = models.TimeField(blank=True, null=True)
#     tmax = models.FloatField(blank=True, null=True)
#     horatmax = models.TimeField(blank=True, null=True)
#     dir = models.IntegerField(blank=True, null=True)
#     velmedia = models.FloatField(blank=True, null=True)
#     racha = models.FloatField(blank=True, null=True)
#     horaracha = models.TimeField(blank=True, null=True)
#     presMax = models.FloatField(blank=True, null=True)
#     horaPresMax = models.CharField(max_length=100, blank=True, null=True)
#     presMin = models.FloatField(blank=True, null=True)
#     horaPresMin = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         abstract=True
#
# class Malaga(BaseWeatherStats):
#     pass
#
# class Murcia(BaseWeatherStats):
#     pass
#
# class Sevilla(BaseWeatherStats):
#     pass
#
# class Valencia(BaseWeatherStats):
#     pass
