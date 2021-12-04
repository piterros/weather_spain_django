from .models import WeatherStats
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import WeatherStatsSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .get_data_from_api import get_data
from rest_framework import generics, mixins


# class WeatherStatsView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = WeatherStats.objects.all()
#     serializer_class = WeatherStatsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


# class MalagaViewSet(viewsets.ModelViewSet):
#     queryset = Malaga.objects.all()
#     serializer_class = MalagaSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # def get(self, request, format=None):
    #     snippets = Malaga.objects.all()
    #     serializer = MalagaSerializer(snippets, many=True)
    #     return Response(serializer.data)

@api_view(['GET',])
def show_data(request):
    # items = WeatherStats.objects.all()
    items = WeatherStats.objects.filter(fecha__range=[request.query_params.get("start_date"), request.query_params.get("end_date")], indicativo=request.query_params.get("station"), provincia=request.query_params.get("city"))
    serializer = WeatherStatsSerializer(items, many=True)
    # print('request.data', request.data, flush=True)
    # print('kwargs', kwargs, flush=True)
    # print('params', request.query_params.get('test'), flush=True)


    return Response(serializer.data)


@api_view(['POST',])
def insert_data(request):
    # print('request:', request)
    # print('request type', type(request))
    # # serializer = MalagaSerializer(data=request.data, context={'request': request})
    # # serializer.is_valid(raise_exception=True)
    # # serializer.save()
    get_data(start_date=request.query_params.get("start_date"), end_date=request.query_params.get("end_date"), station=request.query_params.get("station"), city=request.query_params.get("city"))
    # get_data(start_date=request.data["start_date"],
    #          end_date=request.data["end_date"],
    #          station=request.data["station"],
    #          city=request.data["city"])
    data = {"data": request.data}
    return Response(data)



# class MalagaMonthAverage(viewsets.ModelViewSet):
#     queryset = Malaga.objects.all()
#     serializer_class = MalagaSerializer