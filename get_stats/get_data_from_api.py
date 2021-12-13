import requests
import json
import os
from dotenv import load_dotenv


def get_data(start_date: str, end_date: str, station: str) -> list:
    load_dotenv("./.env")
    url_correct = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{start_date}T00:00:00UTC/fechafin/{end_date}T23:59:59UTC/estacion/{station}/"
    querystring = {"api_key": os.environ["API_KEY"]}
    headers = {"cache-control": "no-cache"}
    response = requests.request("GET", url_correct, headers=headers, params=querystring)
    data = json.loads(response.text)
    url_data = data["datos"]
    response_data = requests.request("GET", url_data)
    data_final = json.loads(response_data.text)
    return data_final
