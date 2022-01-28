import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_show_data_query_params_exist_empty_result():
    client = APIClient()
    response = client.get(
        path="/show_data/?start_date=1000-01-01&end_date=2000-01-01&station=xxxx&city=xxx",
        format="json",
    )
    assert response.status_code == 204


@pytest.mark.django_db
def test_show_data_query_params_do_not_exist():
    client = APIClient()
    response = client.get(path="/show_data/?", format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_show_average_data_query_params_exist_empty_result():
    client = APIClient()
    response = client.get(
        path="/show_average_data/?start_date=1000-01-01&end_date=2000-01-01&station=xxxx&city=xxx&by=days&weather_type=tmax",
        format="json",
    )
    assert response.status_code == 204


@pytest.mark.django_db
def test_show_average_data_query_params_do_not_exist():
    client = APIClient()
    response = client.get(path="/show_average_data/?", format="json")
    assert response.status_code == 400
