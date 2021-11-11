from .models import Malaga, Murcia, Sevilla, Valencia
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import MalagaSerializer


class MalagaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Malaga.objects.all()
    serializer_class = MalagaSerializer
    # permission_classes = [permissions.IsAuthenticated]