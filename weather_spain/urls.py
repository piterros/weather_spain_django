from django.urls import path, include
from rest_framework.routers import DefaultRouter
from get_stats import views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("show_data/", views.show_data),
    path("show_average_data/", views.show_average_data),
    path("insert_data/", views.insert_data),
]
