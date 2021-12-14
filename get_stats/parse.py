from .models import WeatherStats
import time


def parse_data_from_api(entry: dict, city: str, station: str) -> dict:
    for key, value in entry.items():
        if (
            WeatherStats._meta.get_field(key).get_internal_type() == "FloatField"
            or WeatherStats._meta.get_field(key).get_internal_type() == "IntegerField"
        ):
            try:
                value = float(value.replace(",", "."))
                entry.update({key: value})
            except ValueError:
                value = None
                entry.update({key: value})
        elif WeatherStats._meta.get_field(key).get_internal_type() == "TimeField":
            try:
                time.strptime(value, "%H:%M")
            except ValueError:
                value = None
                entry.update({key: value})

    entry.update({"city": city, "station": station})
    return entry
