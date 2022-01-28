from .models import WeatherStats
from rest_framework import status
from .serializers import WeatherStatsSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .database import add_to_database
from .calculate import CalculateAverageWeather


@api_view(
    [
        "GET",
    ]
)
def show_data(request: Request) -> Response:
    if (
        request.query_params.get("start_date")
        and request.query_params.get("end_date")
        and request.query_params.get("station")
        and request.query_params.get("city")
    ):
        items = WeatherStats.objects.filter(
            fecha__range=[
                request.query_params.get("start_date"),
                request.query_params.get("end_date"),
            ],
            indicativo=request.query_params.get("station"),
            provincia=request.query_params.get("city"),
        )
        serializer = WeatherStatsSerializer(items, many=True)
        if serializer.data:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(
            data={"result": "No data for specified parameters"},
            status=status.HTTP_204_NO_CONTENT,
        )
    return Response(
        data={"result": "Incorrect query params"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(
    [
        "GET",
    ]
)
def show_average_data(request: Request) -> Response:
    result = None
    if (
        request.query_params.get("station")
        and request.query_params.get("city")
        and request.query_params.get("weather_type")
        and request.query_params.get("by")
        and request.query_params.get("start_date")
        and request.query_params.get("end_date")
    ):
        calculate_average_weather = CalculateAverageWeather(
            start_date=request.query_params.get("start_date"),
            end_date=request.query_params.get("end_date"),
            weather_type=request.query_params.get("weather_type"),
            station=request.query_params.get("station"),
            city=request.query_params.get("city"),
            months=request.query_params.getlist("months"),
            years=request.query_params.getlist("years"),
        )
        if request.query_params.get("by") == "days":
            result = (
                calculate_average_weather.calculate_average_weather_by_day_of_month()
            )
        elif (
            request.query_params.get("by") == "years"
            and request.query_params.getlist("years")
            and request.query_params.getlist("months")
        ):
            result = calculate_average_weather.calculate_average_weather_by_years()
        if result:
            return Response(result, status=status.HTTP_200_OK)
        return Response(
            data={"result": "No data for specified parameters"},
            status=status.HTTP_204_NO_CONTENT,
        )
    return Response(
        data={"result": "Incorrect query params"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(
    [
        "POST",
    ]
)
def insert_data(request: Request) -> Response:
    if (
        request.query_params.get("start_date")
        and request.query_params.get("end_date")
        and request.query_params.get("station")
        and request.query_params.get("city")
    ):
        add_to_database(
            start_date=request.query_params.get("start_date"),
            end_date=request.query_params.get("end_date"),
            station=request.query_params.get("station"),
            city=request.query_params.get("city"),
        )
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
