import requests
import json
import os
from dotenv import load_dotenv
from .database import add_to_database


def get_data(start_date, end_date, station, city) -> bool:
    print('run get_data:', flush=True)
    # station = '6156X'
    # start_date = '2019-01-01T00:00:00UTC'
    # end_date = '2021-09-30T23:59:59UTC'
    load_dotenv("./.env")
    url_correct = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{start_date}/fechafin/{end_date}/estacion/{station}/"
    querystring = {"api_key": os.environ["API_KEY"]}
    headers = {"cache-control": "no-cache"}

    response = requests.request("GET", url_correct, headers=headers, params=querystring)

    data = json.loads(response.text)

    url_data = data["datos"]

    response_data = requests.request("GET", url_data)
    data_final = json.loads(response_data.text)
    add_to_database(data=data_final, city=city, station=station)
    return True