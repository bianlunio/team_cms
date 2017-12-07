from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Motion, TeamMotion
from .serializers import MotionSerializer


class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        team = self.request.user.member.team
        queryset = Motion.objects.filter(teams__team=team)
        return queryset

    def perform_create(self, serializer):
        team = self.request.user.member.team
        motion = serializer.save()
        TeamMotion.objects.create(motion=motion, team=team)
