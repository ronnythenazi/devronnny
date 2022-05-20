from django import template
from magazine.models import Notification

register = template.Library()
@register.inclusion_tag('social/show_notification.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    path = context['request'].build_absolute_uri()
    notifications = Notification.objects.filter(to_user = request_user).exclude(user_has_seen = True).order_by('-date')
    return {'notifications' : notifications, 'path' : path}
