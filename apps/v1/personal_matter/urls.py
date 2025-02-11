from django.urls import path
from .views import PersonDataListView

urlpatterns = [
    path('', PersonDataListView.as_view(), name='person_data'),
]
