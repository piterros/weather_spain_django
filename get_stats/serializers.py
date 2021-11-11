from .models import Malaga, Murcia, Sevilla, Valencia
from rest_framework import serializers


class MalagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Malaga
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