import http

from .models import WeatherStats
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import WeatherStatsSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .get_data_from_api import get_data
from .calculate import calculate_average_weather_by_months, calculate_average_weather_by_day_of_month


@api_view(['GET',])
def show_data(request):
    items = WeatherStats.objects.filter(fecha__range=[request.query_params.get("start_date"), request.query_params.get("end_date")], indicativo=request.query_params.get("station"), provincia=request.query_params.get("city"))
    serializer = WeatherStatsSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def show_average_data(request):
# "tmed": 14.6,
# "prec": 0.0,
# "tmin": 8.1,
# "horatmin": "06:40:00",
# "tmax": 21.0,
# "horatmax": "14:20:00",
# "dir": 7,
# "velmedia": 1.4,
# "racha": 6.1,
# "horaracha": "15:30:00",
# "presMax": 1018.0,
# "horaPresMax": "10.0",
# "presMin": 1012.4,
# "horaPresMin": 24,
# "sol": 8.7

    # items = WeatherStats.objects.filter(fecha__range=[request.query_params.get("start_date"), request.query_params.get("end_date")], indicativo=request.query_params.get("station"), provincia=request.query_params.get("city"))
    if request.query_params.get("by") == "months":
        result = calculate_average_weather_by_months(start_date=request.query_params.get("start_date"), end_date=request.query_params.get("end_date"), type=request.query_params.get("type"), station=request.query_params.get("station"), city=request.query_params.get("city"))
        serializer = WeatherStatsSerializer(result, many=True)
        return Response(serializer.data)
    elif request.query_params.get("by") == "months":
        calculate_average_weather_by_day_of_month()
    return Response(http.HTTPStatus.BAD_REQUEST)

    # serializer = WeatherStatsSerializer(items, many=True)
    # return Response(serializer.data)


@api_view(['POST',])
def insert_data(request):
    get_data(start_date=request.query_params.get("start_date"), end_date=request.query_params.get("end_date"), station=request.query_params.get("station"), city=request.query_params.get("city"))
    data = {"data": request.data}
    return Response(data)
