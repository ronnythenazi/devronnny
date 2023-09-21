from asgiref.sync import sync_to_async, async_to_sync
from magazine.models import Notification
from general.time import FriendlyTimePassedView
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from django.template.loader import get_template
from magazine.models import Comment, BlogPost, comment_of_comment




@sync_to_async
def get_last_notifications(username, maxNotificationsCnt=1000, startCnt=0):
    return getLastNotifications(username, maxNotificationsCnt, startCnt)

def getLastNotifications(username, maxNotificationsCnt, startCnt):
    endCnt = startCnt + maxNotificationsCnt
    qs = Notification.objects.filter(to_user__username = username).exclude(user_has_seen = True).exclude(from_user__username = username).order_by('-date')[startCnt:endCnt]
    notifications = notificationsToJson(qs)
    #notifications.reverse()
    return notifications


@sync_to_async
def get_num_of_notifications(username):
    return getNumOfNotifications(username)

def getNumOfNotifications(username):
    return Notification.objects.filter(to_user__username = username).exclude(user_has_seen = True).exclude(from_user__username = username).count()


def notificationsToJson(notifications):
    result = []
    for notification in notifications:
        result.append(notification_to_json(notification.id))
    #result.reverse()
    return result


'''
@sync_to_async
def notifications_to_json(notifications):
    result = []
    for notification in notifications:
        result.append(notification_to_json(notification.id))
    result.reverse()
    return result
'''

@sync_to_async
def notification_to_json_called_from_async(notificationId, currUsername):
    if(isAuthenticated(notificationId, currUsername) == False):
        return
    return notification_to_json(notificationId)


def isAuthenticated(notificationId, currUsername):

  notification = Notification.objects.get(id = notificationId)
  if(notification.to_user.username == currUsername):
      return True
  return False


@sync_to_async
def isAuthenticatedForNotifyForNotification(notificationId, currUsername):
    notification = Notification.objects.get(id = notificationId)
    if(notification.from_user.username == currUsername):
        return True
    return False



def getMagazineObj(objName, objId):
    obj = None
    if   objName == 'com':
         obj = Comment.objects.get(id = objId)
    elif objName == 'subcom':
         obj = comment_of_comment.objects.get(id = objId)
    elif objName == 'post':
         obj = BlogPost.objects.get(id = objId)
    return obj


@sync_to_async
def getTotalLikesforObj(objName, objId):
    obj = getMagazineObj(objName, objId)
    return str(obj.total_likes())


@sync_to_async
def getTotalDislikesforObj(objName, objId):
    obj = getMagazineObj(objName, objId)
    return str(obj.total_dislikes())



@sync_to_async
def getcomRateData(notificationId, notTrollKey):
    notification     = Notification.objects.get(id = notificationId)
    notificationType = notification.notification_type
    comId            = notification.comment.id
    total_likes         = str(notification.comment.total_likes())
    total_dislikes      = str(notification.comment.total_dislikes())

    comRateData = {
      'notificationType'   :str(notificationType),
      'comId'              :str(comId),
      'author'             :notification.from_user.username,
      'total_likes'        :total_likes,
      'total_dislikes'     :total_dislikes,
      'notTrollKey'        :notTrollKey,
    }
    return comRateData


@sync_to_async
def getsubComRateData(notificationId, notTrollKey):
    notification        = Notification.objects.get(id = notificationId)
    notificationType    = notification.notification_type
    subComId            = notification.com_of_com.id
    total_likes         = str(notification.com_of_com.total_likes())
    total_dislikes      = str(notification.com_of_com.total_dislikes())

    subComRateData = {
      'notificationType'   :str(notificationType),
      'subComId'           :str(subComId),
      'author'             :notification.from_user.username,
      'total_likes'        :total_likes,
      'total_dislikes'     :total_dislikes,
      'notTrollKey'        :notTrollKey,

    }
    return subComRateData


@sync_to_async
def getPostRateData(notificationId, notTrollKey):
    notification     = Notification.objects.get(id = notificationId)
    notificationType = notification.notification_type
    total_likes         = str(notification.post.total_likes())
    total_dislikes      = str(notification.post.total_dislikes())

    PostRateData = {
      'notificationType' :str(notificationType),
      'author'           :notification.from_user.username,
      'total_likes'        :total_likes,
      'total_dislikes'     :total_dislikes,
      'notTrollKey'        :notTrollKey,
    }
    return PostRateData





def notification_to_json(notificationId):
    notification = Notification.objects.get(id = notificationId)
    author = get_profile_info_nick_or_user(notification.from_user)

    authorUsername = str(notification.from_user.username)


    authorName = str(author['name'])

    authorAvatar = str(author['avatar'])

    timePassed   = FriendlyTimePassedView(notification.date)

    timePassed['cnt'] = str(timePassed['cnt'])

    UserHasSeen       = str(notification.user_has_seen)

    msg               = get_notification_msg(notification)

    content           = msg['content']
    contentPrefix     = msg['contentPrefix']

    thumb             = get_notification_thumb_src(notification)



    dict = {

    'author'        :authorUsername,
    'authorName'    :authorName,
    'authorAvatar'  :authorAvatar,
    'timePassed'    :timePassed,
    'notificationId':str(notificationId),
    'user_has_seen' :UserHasSeen,
    'content'       :content,
    'contentPrefix' :contentPrefix,
    'thumb'         :thumb,
    }
    return dict




def get_notification_msg(notification):
    template_prefix = "notifications/files/notifications_content/"
    template_name   = ""
    content         = ""
    if (notification.notification_type == 1 and notification.post):
        template_name = template_prefix + 'like_your_post.html'
        content = notification.post.title
    elif(notification.notification_type == 4 and notification.post):
        template_name = template_prefix + 'dislike_your_post.html'
        content = notification.post.title

    elif(notification.notification_type == 9 and notification.post):
        template_name = template_prefix + 'new_post.html'
        content = notification.post.title

    elif(notification.notification_type == 1 and notification.comment):
        template_name = template_prefix + 'like_your_com.html'
        content = notification.comment.body

    elif(notification.notification_type == 2 and notification.comment):
        template_name = template_prefix + 'respond_your_post.html'
        content = notification.comment.body

    elif(notification.notification_type == 4 and notification.comment):
        template_name = template_prefix + 'dislike_your_com.html'
        content = notification.comment.body

    elif(notification.notification_type == 5 and notification.comment):
        template_name = template_prefix + 'respond_to_post_you_are_follow.html'
        content = notification.comment.body

    elif(notification.notification_type == 1 and notification.com_of_com):
        template_name = template_prefix + 'like_your_com.html'
        content = notification.com_of_com.body

    elif(notification.notification_type == 2 and notification.com_of_com):
        template_name = template_prefix + 'respond_to_you_under_com.html'
        content = notification.com_of_com.body

    elif(notification.notification_type == 4 and notification.com_of_com):
        template_name = template_prefix + 'dislike_your_com.html'
        content = notification.com_of_com.body

    elif(notification.notification_type == 6 and notification.com_of_com):
        template_name = template_prefix + 'respond_under_com_you_are_follow.html'
        content = notification.com_of_com.body

    elif(notification.notification_type == 8 and notification.com_of_com):
        template_name = template_prefix + 'tag_you.html'
        content = notification.com_of_com.body

    elif(notification.notification_type == 8 and notification.comment):
        template_name = template_prefix + 'tag_you.html'
        content = notification.comment

    contentPrefix= get_template(template_name).render()

    return {'content':str(content), 'contentPrefix':contentPrefix}


def get_notification_thumb_src(notification):
    src = ""
    if(notification.post):
        src = notification.post.thumb.url
    if(notification.comment):
        src = notification.comment.post.thumb.url
    if(notification.com_of_com):
        src = notification.com_of_com.comment.post.thumb.url
    return str(src)

def getNotificationPredcesorsUris(notification):
    viewName = ''
    args = ''
    if (notification.notification_type == 1 and notification.post):
        viewName = 'magazine:anArticle'
        args     = [notification.post.pk]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.post.pk]

    elif(notification.notification_type == 4 and notification.post):
        viewName = 'magazine:anArticle'
        args     = [notification.post.pk]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.post.pk]

    elif(notification.notification_type == 9 and notification.post):
        viewName = 'magazine:anArticle'
        args     = [notification.post.pk]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.post.pk]

    elif(notification.notification_type == 1 and notification.comment):
        viewName = 'magazine:anArticle'
        args     = [notification.comment.post.pk, '-replace-me-comment' + str(notification.comment.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.comment.post.pk]

    elif(notification.notification_type == 2 and notification.comment):
        viewName = 'magazine:anArticle'
        args     = [notification.comment.post.pk, '-replace-me-comment' + str(notification.comment.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.comment.post.pk]

    elif(notification.notification_type == 4 and notification.comment):
        viewName = 'magazine:anArticle'
        args     = [notification.comment.post.pk, '-replace-me-comment' + str(notification.comment.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.comment.post.pk]

    elif(notification.notification_type == 5 and notification.comment):
        viewName = 'magazine:anArticle'
        args     = [notification.comment.post.pk, '-replace-me-comment' + str(notification.comment.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.comment.post.pk]

    elif(notification.notification_type == 1 and notification.com_of_com):
        viewName = 'magazine:anArticle'
        args     = [notification.com_of_com.comment.post.pk, '-replace-me-sub-comment' + str(notification.com_of_com.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.com_of_com.comment.post.pk]

    elif(notification.notification_type == 2 and notification.com_of_com):
        viewName = 'magazine:anArticle'
        args     = [notification.com_of_com.comment.post.pk, '-replace-me-sub-comment' + str(notification.com_of_com.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.com_of_com.comment.post.pk]

    elif(notification.notification_type == 4 and notification.com_of_com):
        viewName = 'magazine:anArticle'
        args     = [notification.com_of_com.comment.post.pk, '-replace-me-sub-comment' + str(notification.com_of_com.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.com_of_com.comment.post.pk]

    elif(notification.notification_type == 6 and notification.com_of_com):
        viewName = 'magazine:anArticle'
        args     = [notification.com_of_com.comment.post.pk, '-replace-me-sub-comment' + str(notification.com_of_com.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.com_of_com.comment.post.pk]

    elif(notification.notification_type == 8 and notification.com):
        viewName = 'magazine:anArticle'
        args     = [notification.com_of_com.comment.post.pk, '-replace-me-comment' + str(notification.comment.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.com_of_com.comment.post.pk]

    elif(notification.notification_type == 8 and notification.com_of_com):
        viewName = 'magazine:anArticle'
        args     = [notification.com_of_com.comment.post.pk, '-replace-me-sub-comment' + str(notification.com_of_com.pk)]

        thumbViewName = 'magazine:anArticle'
        thumbArgs     =  [notification.com_of_com.comment.post.pk]


    content_reverse_url = {'viewName':viewName, 'args':args}
    thumb_reverse_url   = {'viewName':thumbViewName, 'args':thumbArgs}
    return {'content_reverse_url':content_reverse_url, 'thumb_reverse_url':thumb_reverse_url}
