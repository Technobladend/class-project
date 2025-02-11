from rest_framework.generics import ListAPIView
from .models import PersonData
from .serializers import PersonDataSerializer


class PersonDataListView(ListAPIView):
    queryset = PersonData.objects.all()
    serializer_class = PersonDataSerializer