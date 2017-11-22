from rest_framework import viewsets

from .serializers import MotionSerializer
from .models import Motion


class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer

    def get_queryset(self):
        # user_team = self.request.user.member.current_team
        user_team = self.request.user.member.teams.first()
        queryset = Motion.objects.filter(teams__team=user_team)
        return queryset
