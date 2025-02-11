from django.urls import path
from .views import HeaderViewSet, FooterViewSet


urlpatterns = [
    path('header/', HeaderViewSet.as_view({'get': 'list'})),
    path('footer/', FooterViewSet.as_view({'get': 'list'})),
]