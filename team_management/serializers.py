from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        # fields = '__all__'
        exclude = ('user', )
        read_only_fields = ('sn',)
