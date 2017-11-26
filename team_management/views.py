from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Member
from .serializers import MemberSerializer


class MemberViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated, )

    @list_route(permission_classes=[IsAuthenticated])
    def current_user(self, request):
        member = request.user.member
        serializer = MemberSerializer(member, context={'request': request})
        return Response(serializer.data)
