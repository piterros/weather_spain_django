from .models import WeatherStats
from typing import Union


class CalculateAverageWeather:
    """Calculating average weather data"""

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
        """
        Calculate average data by day in range of specified date
        """
        items = WeatherStats.objects.filter(
            fecha__range=[self.start_date, self.end_date],
            indicativo=self.station,
            provincia=self.city,
        )
        scope = [dictionary.__dict__ for dictionary in items]
        return self.calculate_average_value(scope=scope, items=len(items))

    def calculate_average_weather_by_months(self):
        """
        #TODO
        """
        pass

    def calculate_average_weather_by_years(self) -> list[dict]:
        """
        Calculate average data by day in range of specified years and months
        """
        items = WeatherStats.objects.filter(
            fecha__year__in=self.years,
            fecha__month__in=self.months,
            indicativo=self.station,
            provincia=self.city,
        )
        scope = [dictionary.__dict__ for dictionary in items]
        return self.calculate_average_value(scope=scope, items=len(items))

    def calculate_average_value(
        self, scope: list, items: int
    ) -> Union[list[dict], bool]:
        """
        Calculate average value for specified weather data
        Parameters:
            - all values to be calculated (scope)
            - number of values in scope
        Returns:
            - average value for specified data and additional data, which calculation was based on
            - False if number of values in scope is 0
        """
        try:
            average_values = [
                value
                for x in scope
                for key, value in x.items()
                if key == self.weather_type and value is not None
            ]
            return [
                {
                    "start_date": self.start_date,
                    "end_date": self.end_date,
                    "city": self.city,
                    "weather_type": self.weather_type,
                    "months": self.months,
                    "years": self.years,
                    "average_value": round(sum(average_values) / items, 2),
                }
            ]
        except ZeroDivisionError:
            return False
