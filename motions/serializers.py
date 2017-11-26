from rest_framework import serializers

from .models import Motion


class MotionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Motion
        fields = '__all__'
        read_only_fields = ('sn', )
