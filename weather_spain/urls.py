from django.urls import include, path
from rest_framework import routers
from get_stats import views

router = routers.DefaultRouter()
router.register(r'malaga', views.MalagaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('get_stats/', include('rest_framework.urls', namespace='rest_framework'))
]

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
