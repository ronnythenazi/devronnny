from .models import BlogPost, Comment, comment_of_comment
from django.db.models import Q
from .dates import omit_time_from_datetime
from general.general import get_article_rel_path


def get_search_result(search, start_from=0, max_per_page=10):
    to = start_from + max_per_page
    print('from ' + str(start_from) )
    print('to ' + str(to))
    res = BlogPost.objects.filter(Q(title__icontains=search) | Q(subtitle__icontains=search)).order_by('-datepublished')[start_from:to]
    return res


def get_seach_result_qs_in_lst(qs):
    lst = []
    for item in qs:
        id = item.id
        href = get_article_rel_path() + str(id)
        title = str(item.title)
        subtitle = str(item.subtitle)
        date_ = str(omit_time_from_datetime(item.datepublished))
        author = str(item.author.username)
        thumb = str(item.thumb.url)
        avatar = str(item.author.profile.profile_img.url)
        lst.append({'title':title, 'subtitle':subtitle, 'date_':date_, 'author':author, 'thumb':thumb, 'avatar':avatar, 'href':href})
    return lst
