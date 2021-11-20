from .models import Malaga, Murcia, Sevilla, Valencia

def get_city_instance(city):
    print('city in get_vity_instance', city, flush=True)
    cities = {
        "malaga": Malaga,
        "murcia": Murcia,
        "sevilla": Sevilla,
        "valencia": Valencia
    }
    for city_name, city_instance in cities.items():
        print('iterating', city_name, city_instance, flush=True)
        if city_name == city:
            print('city is', city_name, flush=True)
            return city_instance
    return False

def add_to_database(data: list, city) -> None:
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
        get_city_instance(city).objects.update_or_create(**entry)
