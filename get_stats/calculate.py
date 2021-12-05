from .models import WeatherStats

def calculate_average_weather_by_months(start_date, end_date, type, station, city):
    items = WeatherStats.objects.filter(fecha__range=[start_date, end_date], indicativo=station, provincia=city)
    print('items', items, flush=True)
    for dictionary in items:
        print('dictionary', dictionary.__dict__, flush=True)
        for key, value in dictionary.__dict__.items():
            if key == type:
                print("key", key, "value", value, flush=True)
                return dictionary.__dict__

def calculate_average_weather_by_day_of_month():
    pass