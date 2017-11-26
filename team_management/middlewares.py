from django.contrib.auth.models import AnonymousUser

from .models import Member


class MemberMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not isinstance(request.user, AnonymousUser):
            try:
                member = Member.objects.get(user=request.user)
                request.member = member
                team = member.teams.first()
                request.team = team.team
            except Member.DoesNotExist:
                pass

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
