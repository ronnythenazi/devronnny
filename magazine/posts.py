from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from .models import BlogPost, Labels
from django.db.models import Q

#update_label_name, remove_label

def update_label_name(id, txt):
    label = Labels.objects.get(id = id)
    label.text = txt
    label.save()

def remove_label(id):
    label = Labels.objects.get(id = id)
    label.delete()

def create_new_label_for_post(post_id, txt, cblist_of_what):
    post = BlogPost.objects.get(id = post_id)
    label = Labels.objects.create(text = txt)
    label.articles.add(post)
    return {'label_id', str(label.id)}

def update_post_labels(post_id, is_checked, label_id, cblist_of_what):
    post =  BlogPost.objects.get(id = post_id)
    label = Labels.objects.get(id = label_id)

    if(is_checked == 'true'):
        label.articles.add(post)
    else:
        label.articles.remove(post)



def get_all_labels_not_belong_to_post(post_id):
    return list(Labels.objects.filter(~Q(articles = post_id)).order_by('text'))

def get_labels_belong_to_post(post_id):
    return list(Labels.objects.filter(articles = post_id).order_by('text'))

def get_post_labels(post_id, cblist_of_what):
    not_belong_labels= get_all_labels_not_belong_to_post(post_id)
    post_labels = get_labels_belong_to_post(post_id)
    lst = []
    for item in post_labels:
        info = {}
        info['item_name'] = str(cblist_of_what)
        info['id'] = str(item.id)
        info['txt'] = str(item.text)
        info['checked'] = 'true'
        lst.append(info)

    for item in not_belong_labels:
        info = {}
        info['item_name'] = str(cblist_of_what)
        info['id'] = str(item.id)
        info['txt'] = str(item.text)
        info['checked'] = 'false'
        lst.append(info)

    return lst

    #context['main_post']   = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[0]
