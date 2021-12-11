# WeatherSpain
based on Django REST Framework, running in Docker Compose

Application gathers data from AEMET OpenData API (Spanish Meteo Agency), inserts data into database and calculates average values of weather.

How to start:

1. Obtain API key: https://opendata.aemet.es/centrodedescargas/altaUsuario?

2. In root of project create .env file. Fill it with following values:

DB_USER=<db_user>

DB_PASS=<db_pass>

DB_NAME=<db_name>

API_KEY=<api_key>

3. Get ID of weather station from field "Datos de observación. Último elaborado" on https://opendata.aemet.es/centrodedescargas/productosAEMET?

4. There are 3 endpoints:

show_data/ - required parameters: start_date, end_date, station, city

show_average_data/ - required parameters: start_date, end_date, station, city, weather_type, by

insert_data / - required parameters: start_date, end_date, station, city



Example endpoints usage on localhost:

1. Insert weather stats to database:

http://127.0.0.1:8000/insert_data/?start_date=2016-04-01&end_date=2016-04-30&station=7178I&city=MURCIA

2. Show all weather data:

http://127.0.0.1:8000/show_data/?start_date=2016-04-01&end_date=2016-04-30&station=7178I&city=MURCIA

3. Show average maximum temperature on April 2016 in city of Murcia:

http://127.0.0.1:8000/show_average_data/?start_date=2016-04-01&end_date=2016-04-30&station=7178I&city=MURCIA&by=days&weather_type=tmax


