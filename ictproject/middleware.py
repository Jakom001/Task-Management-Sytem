from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from ictproject import settings



class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings by setting a tuple of routes to ignore
    """
    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')):
            return None
        assert hasattr(request, 'user'), """
        The Login Required middleware needs to be after AuthenticationMiddleware.
        Also make sure to include the template context_processor:
        'django.contrib.auth.context_processors.auth'."""

        if not request.user.is_authenticated:
            current_route_name = resolve(request.path_info).url_name

            if not current_route_name in settings.AUTH_EXEMPT_ROUTES:
                return HttpResponseRedirect(reverse(settings.AUTH_LOGIN_ROUTE))

class ExcludeResetTokensMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.pattern = re.compile(r'^/reset/\w+/\w+/$')

    def __call__(self, request):
        if not request.user.is_authenticated and self.pattern.match(request.path):
            # Redirect to login page if user is not authenticated
            return redirect(reverse('login'))
        
        response = self.get_response(request)
        return response