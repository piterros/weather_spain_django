import requests
import json
import os
from .models import Malaga
from dotenv import load_dotenv


def prepare_data() -> list:
    load_dotenv("./.env")
    url_correct = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2019-01-01T00:00:00UTC/fechafin/2021-09-30T23:59:59UTC/estacion/6156X/"
    querystring = {"api_key": os.environ["API_KEY"]}
    headers = {"cache-control": "no-cache"}

    response = requests.request("GET", url_correct, headers=headers, params=querystring)

    data = json.loads(response.text)

    url_data = data["datos"]

    response_data = requests.request("GET", url_data)
    data_final = json.loads(response_data.text)

    return data_final

    # data_test = {'fecha': '2019-01-01', 'indicativo': '6156X', 'nombre': 'MÁLAGA, CENTRO METEOROLÓGICO', 'provincia': 'MALAGA', 'altitud': '54', 'tmed': '14,0', 'prec': '0,0', 'tmin': '6,1', 'horatmin': '05:00', 'tmax': '21,9', 'horatmax': '14:00', 'dir': '31', 'velmedia': '1,9', 'racha': '4,4', 'horaracha': '02:50', 'presMax': '1027,7', 'horaPresMax': 'Varias', 'presMin': '1024,0', 'horaPresMin': '14'}

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
