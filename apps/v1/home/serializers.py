from rest_framework import serializers
from .models import HeaderModel, FooterModel, Wise_quotes


class WiseQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wise_quotes
        fields = ('quote', 'author')


class HeaderSerializer(serializers.ModelSerializer):
    wise_quote = serializers.SerializerMethodField()

    class Meta:
        model = HeaderModel
        fields = ('title', 'description', 'wise_quote')

    def get_wise_quote(self, obj):
        quote = Wise_quotes.objects.order_by('?').first()
        if quote:
            return {"quote": quote.quote, "author": quote.author}
        return None

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = ('address',)