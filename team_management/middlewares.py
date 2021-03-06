from django.contrib.auth.models import AnonymousUser
from django.utils.functional import SimpleLazyObject

from .models import Member


class MemberMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        def get_member(user):
            return Member.objects.get(user=user)

        if not isinstance(request.user, AnonymousUser):
            try:
                request.member = SimpleLazyObject(lambda: get_member(request.user))
            except Member.DoesNotExist:
                pass

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
