from django.conf import settings
from magazine import models
from social import members_permissions, notifications

def RequestExposerMiddleware(get_response):
    def middleware(request):
        members_permissions.exposed_request = request
        notifications.exposed_request = request
        models.exposed_request = request
        response = get_response(request)
        return response

    return middleware
