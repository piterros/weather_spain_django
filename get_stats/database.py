from .models import WeatherStats
from .get_data_from_api import get_data
from .parse import parse_data_from_api


def add_to_database(start_date: str, end_date: str, city: str, station: str) -> None:
    data = get_data(start_date=start_date, end_date=end_date, station=station)
    for entry in data:
        parsed_data = parse_data_from_api(entry=entry, city=city, station=station)
        WeatherStats.objects.update_or_create(**parsed_data)
