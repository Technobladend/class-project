from rest_framework import serializers
from .models import PersonData


class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonData
        fields = (
            'image',
            'first_name',
            'last_name',
            'hobby',
            'gender',
            'height',
            'weight',
            'skin_color',
            'email',
            'phone',
            'address',
            'date_of_birth',
        )
