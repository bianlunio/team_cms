from rest_framework import serializers

from .models import Motion


class MotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Motion
        fields = '__all__'
