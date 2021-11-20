from django.urls import include, path
from rest_framework import routers
from get_stats import views

# router = routers.DefaultRouter()
# router.register(r'list', views.get_data_list)
# router.register(r'post_val', views.post_data)

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('get_stats/', include('rest_framework.urls', namespace='rest_framework')),
#     # path('malaga/', views.MalagaViewSet.as_view()),
# ]

urlpatterns = [
    # path('', include(router.urls)),
    path('list/', views.get_data_list, name='list'),
    path('post_val/', views.create, name='post_val'),
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
