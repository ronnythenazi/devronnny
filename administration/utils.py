from magazine.models import Comment, comment_of_comment


def hideComObj(objName, id):
    com = None
    if(objName == 'com'):
        com = Comment.objects.get(id = id)
    elif(objName == 'subcom'):
        com = comment_of_comment.objects.get(id = id)
    hideComment(com)

def unhideComObj(objName, id):
    com = None
    if(objName == 'com'):
        com = Comment.objects.get(id = id)
    elif(objName == 'subcom'):
        com = comment_of_comment.objects.get(id = id)
    unhideComment(com)


def hideComment(com):
    com.hidden = True
    com.save()

def unhideComment(com):
    com.hidden = False
    com.save()
