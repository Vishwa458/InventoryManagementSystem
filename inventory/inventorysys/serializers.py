from rest_framework import serializers
from .models import *

class LaptopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = laptop
        fields = (
            'type',
            'price',
            'company',
            'status',
        )







