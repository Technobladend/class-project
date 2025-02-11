from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.routers import DefaultRouter
from .models import HeaderModel, FooterModel, Wise_quotes
from .serializers import HeaderSerializer, FooterSerializer, WiseQuoteSerializer


class HeaderViewSet(ReadOnlyModelViewSet):
    queryset = HeaderModel.objects.all()
    serializer_class = HeaderSerializer


class FooterViewSet(ReadOnlyModelViewSet):
    queryset = FooterModel.objects.all()
    serializer_class = FooterSerializer


router = DefaultRouter()
router.register('header', HeaderViewSet)
router.register('footer', FooterViewSet)


