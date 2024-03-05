from rest_framework import serializers
from .models import WatchList

class WatchListserializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'