from .models import WeatherStats
from django.db.models import QuerySet


class CalculateAverageWeather:
    def __init__(
        self,
        weather_type: str,
        station: str,
        city: str,
        start_date: str = None,
        end_date: str = None,
        years: list = None,
        months: list = None,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.weather_type = weather_type
        self.station = station
        self.city = city
        self.years = years
        self.months = months

    def calculate_average_weather_by_day_of_month(self) -> list[dict]:
        items = WeatherStats.objects.filter(
            fecha__range=[self.start_date, self.end_date],
            indicativo=self.station,
            provincia=self.city,
        )
        scope = [dictionary.__dict__ for dictionary in items]
        return self.calculate_average_value(scope=scope, items=items)

    def calculate_average_weather_by_months(self):
        pass

    def calculate_average_weather_by_years(self):
        items = WeatherStats.objects.filter(
            fecha__year__in=self.years,
            fecha__month__in=self.months,
            indicativo=self.station,
            provincia=self.city,
        )
        scope = [dictionary.__dict__ for dictionary in items]
        return self.calculate_average_value(scope=scope, items=items)

    def calculate_average_value(self, scope: list, items: QuerySet) -> list[dict]:
        all_values = 0
        for x in scope:
            for key, value in x.items():
                if key == self.weather_type:
                    all_values += value

        average_value = all_values / len(items)
        return [
            {
                "start_date": self.start_date,
                "end_date": self.end_date,
                "city": self.city,
                "weather_type": self.weather_type,
                "months": self.months,
                "years": self.years,
                "average_value": round(average_value, 2),
            }
        ]
