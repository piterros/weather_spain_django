from .models import WeatherStats
from rest_framework import serializers


class WeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStats
        fields = '__all__'
        # fields = [
        #     fecha
        # indicativo
        # nombre
        # provincia
        # altitud
        # tmed
        # prec
        # tmin
        # horatmin
        # tmax
        # horatmax =
        # dir = model
        # velmedia =
        # racha = mod
        # horaracha =
        # presMax = m
        # horaPresMax
        # presMin = m
        # horaPresMin
        # ]