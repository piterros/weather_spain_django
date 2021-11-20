from .models import Malaga, Murcia, Sevilla, Valencia
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import MalagaSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .get_data_from_api import get_data


# class MalagaViewSet(viewsets.ModelViewSet):
#     queryset = Malaga.objects.all()
#     serializer_class = MalagaSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # def get(self, request, format=None):
    #     snippets = Malaga.objects.all()
    #     serializer = MalagaSerializer(snippets, many=True)
    #     return Response(serializer.data)

@api_view(['GET',])
def get_data_list(request):
    # if request.method == 'GET':
    items = Malaga.objects.all()
    # items_serializer = Malaga(items, many=True)
    return Response(items)

# @api_view(['POST',])
# def create(request):
#     serializer = MalagaSerializer(data=request.data, context={'request': request})
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)


@api_view(['POST',])
def create(request):
    print('request:', request)
    print('request type', type(request))
    # serializer = MalagaSerializer(data=request.data, context={'request': request})
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    get_data(start_date=request.data["start_date"], end_date=request.data["end_date"], station=request.data["station"], city=request.data["city"])
    data = {"data_name": "data_val", "data2": request.data}
    return Response(data)



# class MalagaMonthAverage(viewsets.ModelViewSet):
#     queryset = Malaga.objects.all()
#     serializer_class = MalagaSerializer