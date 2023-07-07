from .models import PageVisitor, UserSession, SiteVisitor
from magazine.models import BlogPost
from .utils  import get_session_key, get_client_ip
from users.members import get_profile_info_nick_or_user
from general.time import get_miniutes_passed
from operator import itemgetter
from django.utils import timezone
import math



def get_anonymous_visitors():

    all_visitors = SiteVisitor.objects.all()

    anonymous_visitors = all_visitors.filter(session_key__isnull = True).order_by('-LastTimeWasActive')[:100000]
    result = []

    for visitor in anonymous_visitors:

        miniutes_passed = get_miniutes_passed(visitor.LastTimeWasActive)
        if(miniutes_passed>10):
            continue
        visitor_details = {}
        visitor_details['last_time_active'] = miniutes_passed
        visitor_details['ip_address'] = visitor.ip_address
        result.append(visitor_details)
    return result

def get_anonymous_visitors_for_post(page_id):

    page = BlogPost.objects.get(id=page_id)
    all_visitors = PageVisitor.objects.filter(page = page)

    anonymous_visitors = all_visitors.filter(session_key__isnull = True).order_by('-LastTimeWasActive')[:100000]
    result = []

    for visitor in anonymous_visitors:

        miniutes_passed = get_miniutes_passed(visitor.LastTimeWasActive)
        if(miniutes_passed>10):
            continue
        visitor_details = {}
        visitor_details['last_time_active'] = miniutes_passed
        visitor_details['ip_address'] = visitor.ip_address
        result.append(visitor_details)
    return result




def get_member_visitors():

    all_visitors = SiteVisitor.objects.all()
    member_visitors = all_visitors.filter(session_key__in = UserSession.objects.all().values_list('session_key'))[:1000]

    lst = []

    for visitor in member_visitors:

        miniutes_passed = get_miniutes_passed(visitor.LastTimeWasActive)

        if(miniutes_passed>10):
            continue
        member_details = {}
        member_details['last_time_active'] = miniutes_passed

        users_qs  = UserSession.objects.filter(session_key = visitor.session_key)
        if not users_qs.exists():
            continue
        member = users_qs.first()


        #dictionary , keys are name, avatar
        member_details.update(get_profile_info_nick_or_user(member.user))
        member_details['ip_address'] = member.ip_address
        member_details['user_id'] =  member.user.id
        lst.append(member_details)

    #reverse = True meaning descending order
    result = sorted(lst, key=itemgetter('name'), reverse=False)
    return result


def get_member_visitors_for_post(page_id):

    page = BlogPost.objects.get(pk=page_id)
    all_visitors = PageVisitor.objects.filter(page = page)
    member_visitors = all_visitors.filter(session_key__in = UserSession.objects.all().values_list('session_key'))[:1000]

    lst = []

    for visitor in member_visitors:

        miniutes_passed = get_miniutes_passed(visitor.LastTimeWasActive)
        if(miniutes_passed>10):
            continue
        member_details = {}
        member_details['last_time_active'] = miniutes_passed

        users_qs  = UserSession.objects.filter(session_key = visitor.session_key)
        if not users_qs.exists():
            continue
        member = users_qs.first()


        #dictionary , keys are name, avatar
        member_details.update(get_profile_info_nick_or_user(member.user))
        member_details['ip_address'] = member.ip_address
        member_details['user_id'] =  member.user.id
        lst.append(member_details)

    #reverse = True meaning descending order
    result = sorted(lst, key=itemgetter('name'), reverse=False)
    return result


def set_visitor_date_for_post(request, page_id):

    page = BlogPost.objects.get(id=page_id)
    ip_address = get_client_ip(request)

    session_key = None

    if request.user.is_authenticated:
        session_key = get_session_key(request)

    if session_key == None:
        visitors = PageVisitor.objects.filter(ip_address = ip_address, page = page, session_key__isnull = True)
    else:
        visitors = PageVisitor.objects.filter(ip_address = ip_address, page = page, session_key = session_key)

    if visitors.exists():
        visitor = visitors.first()
        visitor.LastTimeWasActive = timezone.now()
        visitor.save()

    else:
        PageVisitor.objects.create(page = page, ip_address = ip_address, session_key = session_key)




def set_visitor_date(request):

    ip_address = get_client_ip(request)

    session_key = None

    if request.user.is_authenticated:
        session_key = get_session_key(request)

    if session_key == None:
        visitors = SiteVisitor.objects.filter(ip_address = ip_address, session_key__isnull = True)
    else:
        visitors = SiteVisitor.objects.filter(ip_address = ip_address, session_key = session_key)


    if visitors.exists():
        visitor = visitors.first()
        visitor.LastTimeWasActive = timezone.now()
        visitor.save()
    else:
        SiteVisitor.objects.create(session_key = session_key , ip_address = ip_address)
