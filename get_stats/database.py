
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
        city.objects.update_or_create(**entry)
