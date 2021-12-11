from .models import WeatherStats
from .get_data_from_api import get_data


def add_to_database(start_date: str, end_date: str, city: str, station: str) -> None:
    data = get_data(start_date=start_date, end_date=end_date, station=station)
    for entry in data:
        for key, value in entry.items():
            try:
                value = float(value.replace(",", "."))
                entry.update({key: value})
            except:
                pass
            if isinstance(value, str) and value.lower() == "varias":
                value = None
                entry.update({key: value})
        entry.update({"city": city, "station": station})
        WeatherStats.objects.update_or_create(**entry)
