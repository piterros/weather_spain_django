from .models import WeatherStats


class CalculateAverageWeather:
    def __init__(
        self, start_date: str, end_date: str, weather_type: str, station: str, city: str
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.weather_type = weather_type
        self.station = station
        self.city = city

    def calculate_average_weather_by_day_of_month(self) -> list[dict]:
        items = WeatherStats.objects.filter(
            fecha__range=[self.start_date, self.end_date],
            indicativo=self.station,
            provincia=self.city,
        )
        scope = [dictionary.__dict__ for dictionary in items]
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
                "average_value": round(average_value, 2)
            }
        ]

    def calculate_average_weather_by_months(self):
        pass
