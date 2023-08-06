from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from magazine.models import Profile, comment_of_comment, Comment, BlogPost
from django.db.models import Sum, Count


def get_total_comments_of_profile(profile):
    comments_cnt = profile.user.user_comments.all().count()
    sub_coms_cnt = profile.user.user_sub_comments.all().count()
    total_comments_count = comments_cnt + sub_coms_cnt
    return total_comments_count

def get_total_likes_given_to_profile(profile):
    coms = profile.user.user_comments.all()
    likes_cnt = 0
    for com in coms:
        likes_cnt += com.likes.exclude(id = profile.user.id).count()
    sub_coms = profile.user.user_sub_comments.all()

    for sub_com in sub_coms:
        likes_cnt += sub_com.likes.exclude(id = profile.user.id).count()

    posts = profile.user.author_posts.all()

    for post in posts:
        likes_cnt += post.likes.exclude(id = profile.user.id).count()

    return likes_cnt


def get_total_dislikes_given_to_profile(profile):
    coms = profile.user.user_comments.all()
    dislikes_cnt = 0
    for com in coms:
        dislikes_cnt += com.dislikes.exclude(id = profile.user.id).count()
    sub_coms = profile.user.user_sub_comments.all()

    for sub_com in sub_coms:
        dislikes_cnt += sub_com.dislikes.exclude(id = profile.user.id).count()

    posts = profile.user.author_posts.all()

    for post in posts:
        dislikes_cnt += post.dislikes.exclude(id = profile.user.id).count()

    return dislikes_cnt


def get_total_likes_profile_gave(profile):
    likes_for_posts = profile.user.post_likes.all().count()
    likes_for_coms = profile.user.likes_com.all().count()
    likes_for_subcoms = profile.user.likes_com_of_com.all().count()

    total = likes_for_posts + likes_for_coms + likes_for_subcoms
    return total

def get_total_dislikes_profile_gave(profile):
    dislikes_for_posts = profile.user.post_dislikes.all().count()
    dislikes_for_coms = profile.user.dislikes_com.all().count()
    dislikes_for_subcoms = profile.user.dislikes_com_of_com.all().count()

    total = dislikes_for_posts + dislikes_for_coms + dislikes_for_subcoms
    return total


def get_total_coms_given_to_profile(profile):

    coms_given_to_sub_coms_cnt = comment_of_comment.objects.filter(to_sub_comment__comment_of_comment_usr = profile.user).exclude(comment_of_comment_usr = profile.user).count()
    coms = profile.user.user_comments.all()

    sub_coms_for_main_coms_cnt = 0

    for com in coms:
        sub_coms_for_main_coms_cnt += com.comments_of_comment.all().exclude(comment_of_comment_usr = profile.user).count()

    total_comments_given_to_profile = coms_given_to_sub_coms_cnt + sub_coms_for_main_coms_cnt
    return total_comments_given_to_profile
