from django.urls import path, include
from rest_framework.routers import DefaultRouter
from get_stats import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'weather_stats', views.WeatherStatsView)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

# urlpatterns = [
#     path('snippets/', views.WeatherStatsView.as_view()),
#     # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# ]

# from django.urls import include, path
# from rest_framework import routers
#
# router.register(r'get_data', views.get_data)
# router.register(r'insert_data', views.insert_data)
#
urlpatterns = [
    path('', include(router.urls)),
    path('show_data/', views.show_data),
    path('insert_data/', views.insert_data),
]
#
# urlpatterns = [
#     # path('', include(router.urls)),
#     path('get_weather_stats/', views.get_weather_stats, name='get_weather_stats'),
#     path('insert_weather_stats/', views.create, name='insert_weather_stats'),
# ]

# from django.urls import include, path
# from rest_framework import routers
# import views
#
# router = routers.DefaultRouter()
# router.register(r'malaga', views.MalagaViewSet)
# #
# urlpatterns = [
#     path('', include(router.urls)),
#     path('malaga/', include('get_stats.urls'))
#     ]
#
# urlpatterns = [
#     path('malaga/', views.MalagaViewSet.as_view())
# ]

# router = routers.DefaultRouter()
# router.register(r'malaga', views.MalagaViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
