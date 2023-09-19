
var wsUsersNotifications = {};


$(document).ready(function(){
  var username = $('#curr-username-cn').val();
  var roomName = username + 'Notifications';
  connectNotifications(roomName, 'read');
  if($('#article-notifications').length)
  {

    connectNotifications($('#article-notifications').val(), 'readAndwrite');
  }


  var elem_to_focus = $('#notifications-popup');
  var trigger_elem = $('#bell-menu-item');
  focusout(elem_to_focus, trigger_elem);
  $(elem_to_focus).css('right', offset_right($(trigger_elem)));
  var top = $('.main-menu').height() - 50;
  $(elem_to_focus).css('top', top + 'px');
});

$(window).scroll(function(){
  var elem_to_focus = $('#notifications-popup');
  var top = $('.main-menu').height() - 50;
  $(elem_to_focus).css('top', top + 'px');
});

$('#bell-menu-item').click(function(){


  if(!$('#notifications-popup .notification-item').length)
  {
     $('#empty-notifications').css('display', 'flex');
  }


});




function notifyAllforNotifications(notifications)
{
   for(var i=0;i<notifications.length;i++)
   {
     var toUserName = notifications[i]['toUserName'];
     var notificationId = notifications[i]['notificationId'];
     NotifyforNotification(toUserName, notificationId);
   }
}

function NotifyforNotification(toUserName, notificationId)
{
  var roomName = toUserName + 'Notifications';
  connectNotifications(roomName, 'send', notificationId);

}



function connectNotifications(roomName, flag, notificationId = null)
{
  var url="";
  if(is_debug(window.location.host))
  {
    url = 'ws://'+window.location.host+'/ws/notifications/'+ roomName  + '/';
  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/notifications/'+ roomName  + '/';

  }
  wsUsersNotifications[roomName] = new WebSocket(url);

  wsUsersNotifications[roomName].onopen = function(e){
    if(flag == 'send')
    {
      sendNotificationOfNotification(roomName, notificationId);
    }
    else if(flag == 'read')
    {
      fetchNotifications(roomName);
    }

  };


   wsUsersNotifications[roomName].onmessage =  function(e){
     var data = JSON.parse(e.data);

   load_notifications(roomName, data);};


   wsUsersNotifications[roomName].onclose = function(){
     setTimeout(function() {
      connectNotifications(roomName, flag, notificationId);
    }, 1000);

   };


}

function sendNotificationOfNotification(roomName, notificationId)
{
  wsUsersNotifications[roomName].send(JSON.stringify({
      'command'       : 'NotifyforNotification',
      'notificationId':  notificationId,
  }));
}

function fetchNotifications(roomName)
{

  wsUsersNotifications[roomName].send(JSON.stringify({
      'command'       : 'fetchNotifications',
  }));
}

function update_unvoting(objName, objId, unvoteType, total_likes,  total_dislikes, author, notTrollKey)
{
  if(!$('#article-notifications').length)
  {
    return;
  }
  if($('#article-notifications').val() != notTrollKey)
  {
    return;
  }
  var curr_user = $('#curr-user').val();
  /*if(curr_user == author)
  {
    return;
  }*/

  var upvoteSelector   = '';
  var downvoteSelector = '';
  var ancestor         = '';
  if(objName == 'com')
  {
    upvoteSelector   = '#comment' + objId + ' .rate-count.rate-green';
    downvoteSelector = '#comment' + objId + ' .rate-count.rate-red';
    ancestor         = '#comment' + objId;

  }
  if(objName == 'subcom')
  {
    upvoteSelector   = '#sub-comment' + objId + ' .rate-green';
    downvoteSelector = '#sub-comment' + objId + ' .rate-red';
    ancestor         = '#sub-comment' + objId;
  }
  if(objName == 'post')
  {
    upvoteSelector   = '#rate-post-form' + ' .rate-count.rate-green';
    downvoteSelector = '#rate-post-form' + ' .rate-count.rate-red';
    ancestor         = '#rate-post-form';
  }


  $(upvoteSelector).text(total_likes);
  $(downvoteSelector).text(total_dislikes);

  if(total_likes == 0)
  {
    $(upvoteSelector).hide();
  }

  if(total_dislikes == 0)
  {
    $(downvoteSelector).hide();
  }

  if(total_likes > 0)
  {
    $(upvoteSelector).show();
  }

  if(total_dislikes > 0)
  {
    $(downvoteSelector).show();
  }

  if(unvoteType == 'unlike' && curr_user == author)
  {
    $(ancestor + ' .user_liked').hide();
    $(ancestor + ' .user_unliked').show();
  }

  if(unvoteType =='undislike' && curr_user == author)
  {
    $(ancestor + ' .user_disliked').hide();
    $(ancestor + ' .user_undisliked').show();
  }



}

function update_rating(objName, objId, total_likes,  total_dislikes, notificationType, author, notTrollKey)
{

  if(!$('#article-notifications').length)
  {
    return;
  }
  if($('#article-notifications').val() != notTrollKey)
  {
    return;
  }
  var curr_user = $('#curr-user').val();

  var upvoteSelector   = '';
  var downvoteSelector = '';
  var ancestor         = '';

  if(objName == 'com')
  {
    upvoteSelector   = '#comment' + objId + ' .rate-count.rate-green';
    downvoteSelector = '#comment' + objId + ' .rate-count.rate-red';
    ancestor         = '#comment' + objId;
  }
  if(objName == 'subcom')
  {
    upvoteSelector =   '#sub-comment' + objId + ' .rate-green';
    downvoteSelector = '#sub-comment' + objId + ' .rate-red';
    ancestor       =   '#sub-comment' + objId;
  }
  if(objName == 'post')
  {
    upvoteSelector   = '#rate-post-form' + ' .rate-count.rate-green';
    downvoteSelector = '#rate-post-form' + ' .rate-count.rate-red';
    ancestor         = '#rate-post-form';
  }

  $(upvoteSelector).text(total_likes);
  $(downvoteSelector).text(total_dislikes);

  if(total_likes == 0)
  {
    $(upvoteSelector).hide();
  }

  if(total_dislikes == 0)
  {
    $(downvoteSelector).hide();
  }

  if(total_likes > 0)
  {
    $(upvoteSelector).show();
  }

  if(total_dislikes > 0)
  {
    $(downvoteSelector).show();
  }

  var is_user_liked    = false;
  var is_user_disliked = false;

  if(notificationType == '1' && author == curr_user)
  {
     is_user_liked = true;
  }

  if(notificationType == '4' && author == curr_user)
  {
     is_user_disliked = true;
  }


  if(is_user_liked)
  {
    $(ancestor + ' .user_liked').show();
    $(ancestor + ' .user_unliked').hide();
    $(ancestor + ' .user_disliked').hide();
    $(ancestor + ' .user_undisliked').show();

  }
  else if(is_user_disliked)
  {
    $(ancestor + ' .user_liked').hide();
    $(ancestor + ' .user_unliked').show();
    $(ancestor + ' .user_disliked').show();
    $(ancestor + ' .user_undisliked').hide();
  }
  else
  {
    /*$(ancestor + ' .user_liked').hide();
    $(ancestor + ' .user_unliked').show();
    $(ancestor + ' .user_disliked').hide();
    $(ancestor + ' .user_undisliked').show();*/
  }

}




function load_notifications(roomName, data)
{
   if(data['command'] == 'unRated')
   {
     notTrollKey    = data['notTrollKey'];
     objId          = data['objId'];
     objName        = data['objName'];
     author         = data['author'];
     total_likes    = data['total_likes'];
     total_dislikes = data['total_dislikes'];
     unvoteType     = data['unvoteType'];
     update_unvoting(objName, objId, unvoteType, total_likes,  total_dislikes, author, notTrollKey);
   }
   else if(data['command'] == 'comRated')
   {

     var msg = data['comRateData'];
     var total_likes = msg['total_likes']
     var total_dislikes = msg['total_dislikes']
     update_rating('com', msg['comId'], total_likes, total_dislikes, msg['notificationType'], msg['author'], msg['notTrollKey']);
   }

   else if(data['command'] == 'subComRated')
   {
     var msg = data['subComRateData'];
     var total_likes = msg['total_likes']
     var total_dislikes = msg['total_dislikes']
     update_rating('subcom', msg['subComId'], total_likes, total_dislikes, msg['notificationType'], msg['author'], msg['notTrollKey']);
   }

   else if(data['command'] == 'postRated')
   {
     var msg = data['postRateData'];
     var total_likes = msg['total_likes']
     var total_dislikes = msg['total_dislikes']
     update_rating('post', null, total_likes, total_dislikes, msg['notificationType'], msg['author'], msg['notTrollKey']);
   }


   else if(data['command'] == 'NotifyforNotification')
   {
     wsUsersNotifications[roomName].send(JSON.stringify({
         'command'       : 'newNotification',
         'notificationId':  data['notificationId'],
     }));
   }

   else if(data['command'] == 'newNotification')
   {
     $('#empty-notifications').hide();
     update_notifications_log(data['notification']);


   }

   else if(data['command'] == 'fetchNotifications')
   {

     $('#notifications-popup .notification-items>*').remove();
     $('#empty-notifications').hide();
     for(let i=0;i<data['notifications'].length;i++)
     {

       update_notifications_log(data['notifications'][i]);

     }

  }

  setBellAnimation(data);

}



function setBellAnimation(data)
{


  if($('#notifications-popup .notification-item').length>0)
  {
    $('#ring-the-bell').show();
    $('#dont-ring-the-bell').hide();
    $('.notification-counter').text($('#notifications-popup .notification-item').length.toString());

  }
  else
  {
    $('#ring-the-bell').hide();
    $('#dont-ring-the-bell').show();
  }



  if(data['command'] != 'newNotification')
  {
     return;
  }

    $('#notification-sound')[0].play();
}



function update_notifications_log(item)
{


  var author = item['author'];
  var username_log_in = $('#curr-username-cn').val();

   if(author == username_log_in)
   {
     return;
   }

    var authorName          = item['authorName'];
    var authorAvatar        = item['authorAvatar'];
    var content             = item['content'];
    var timePassed          = item['timePassed'];
    var notificationId      = item['notificationId'];
    var user_has_seen       = item['user_has_seen'];
    var content             = item['content'];
    var contentPrefix       = item['contentPrefix'];
    var thumb               = item['thumb'];


    var popup_body = $('#notifications-popup .notification-items');
    var data = 'notificationId="' + notificationId + '" ';
        data += 'author ="' + author  + '" ';
    $(popup_body).prepend('<div class="notification-item" '+ data +'></div>');
    var item = $(popup_body).find('.notification-item').first();
    $(item).append('<div class="notification-cell-author"></div>');
    $(item).append('<div class="notification-cell-contentsnip"></div>');
    $(item).append('<div class="notification-cell-thumb"></div>');


    var thumb_holder = $(item).find('.notification-cell-thumb');
    $(thumb_holder).append('<img src="'+ thumb +'" alt="">');

    $(item).find('.notification-cell-author').append('<img src="">');
    var img = $(item).find('.notification-cell-author').find('img');
    $(img).attr('src', authorAvatar);


    var subitem = $(item).find('.notification-cell-contentsnip');
    $(subitem).append('<div class="notification-subcell-contentsnip-msg"></div>');
    $(subitem).append('<div class="notification-subcell-contentsnip-timepassed"></div>');
    var msg = $(subitem).find('.notification-subcell-contentsnip-msg');
    var prefix = authorName  + ":" ;
    $(msg).append('<p class="nowrap-child notification-prefix"></p>');
    var notificationPrefix =  $(msg).find('.notification-prefix');
    $(notificationPrefix).append('<span class="prefix-name bluish-clr nowrap-child"></span>');
    $(notificationPrefix).append('<span class="contentPrefix blood-clr nowrap-child"></span>');

    var contentPrefixelem =  $(notificationPrefix).find('.contentPrefix');
    var prefixNameelem =  $(notificationPrefix).find('.prefix-name');

   $(contentPrefixelem).html(contentPrefix);
   $(prefixNameelem).html(prefix);

    $(msg).append('<p class="wrap-child content-notification"></p>');
    contentNotification =  $(msg).find('.content-notification');
    $(contentNotification).html(content);
    var t_lbl = $(subitem).find('.notification-subcell-contentsnip-timepassed');
    $(t_lbl).html(get_friendly_time_format(timePassed));



  assignDelegates();

}



function assignDelegates()
{
  $('.notification-items').on('click','.notification-item', notificationItemClick);
}


function notificationItemClick(e)
{

  var urlType = "";
  if(is_curs_inside_rect_elem($(this).find('.notification-cell-author'), e))
  {
    urlType = 'author';

  }
  else if(is_curs_inside_rect_elem($(this).find('.notification-cell-contentsnip'), e))
  {
    urlType = 'content';
  }
  else if(is_curs_inside_rect_elem($(this).find('.notification-cell-thumb'), e))
  {
    urlType = 'thumb';
  }
  else
  {

  }
  var notificationId = $(this).attr('notificationId');
  getUrlOfNotificationObjajax(notificationId, urlType, function(callback){
    window.location = callback['url'];
  });
}




function notifyForcomRated(notificationId)
{
  wsUsersNotifications[$('#article-notifications').val()].send(JSON.stringify({
      'command'       : 'comRated',
      'notificationId':  notificationId,
      'notTrollKey'   : $('#article-notifications').val(),
  }));
}

function notifyForSubComRated(notificationId)
{
//  try
//  {
    wsUsersNotifications[$('#article-notifications').val()].send(JSON.stringify({
        'command'       : 'subComRated',
        'notificationId':  notificationId,
        'notTrollKey'   : $('#article-notifications').val(),
    }));
//  }
//  catch (e)
//  {

  //  setTimeout(function(){
    //  notifyForSubComRated(notificationId)},
  //   1000);
//  }

}

function notifyForPostRated(notificationId)
{
  wsUsersNotifications[$('#article-notifications').val()].send(JSON.stringify({
      'command'       : 'postRated',
      'notificationId':  notificationId,
      'notTrollKey'   : $('#article-notifications').val(),
  }));
}

function notifyForUnvoting(objId, objName, unvoteType)
{
  wsUsersNotifications[$('#article-notifications').val()].send(JSON.stringify({
      'command'       : 'unRated',
      'objId'         :objId,
      'objName'       :objName,
      'unvoteType'    :unvoteType,
      'notTrollKey'   : $('#article-notifications').val(),
  }));
}
