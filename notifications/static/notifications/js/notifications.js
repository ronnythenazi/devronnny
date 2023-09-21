
var wsUsersNotifications = {};


$(document).ready(function(){

  var elem_to_focus = $('#notifications-popup');
  var trigger_elem = $('#bell-menu-item');
  focusout(elem_to_focus, trigger_elem);
  $(elem_to_focus).css('right', offset_right($(trigger_elem)));
  var top = $('.main-menu').height() - 50;
  $(elem_to_focus).css('top', top + 'px');




  var username = $('#curr-username-cn').val();
  var roomName = username + 'Notifications';
  connectNotifications(roomName, 'read');
  if($('#article-notifications').length)
  {

    connectNotifications($('#article-notifications').val(), 'readAndwrite');
  }



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
      'command'            : 'fetchNotifications',
      'startCnt'           :'0',
      'maxNotificationsCnt':'4',


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

  var upvoteSelector     = '';
  var downvoteSelector   = '';
  var ancestor           = '';
  var userLikedElem      = '';
  var userDislikedElem   = '';
  var userUnlikedElem    = '';
  var userUndislikedElem = '';

  if(objName == 'com')
  {
    upvoteSelector   = '#comment' + objId + ' .rate-count.rate-green';
    downvoteSelector = '#comment' + objId + ' .rate-count.rate-red';
    ancestor         = '#comment' + objId;
    userLikedElem       =  ancestor + ' .user_liked';
    userDislikedElem    =  ancestor + ' .user_disliked';
    userUnlikedElem     =  ancestor + ' .user_unliked';
    userUndislikedElem  =  ancestor + ' .user_undisliked';

  }
  if(objName == 'subcom')
  {
    upvoteSelector      = '#sub-comment' + objId + ' .rate-green';
    downvoteSelector    = '#sub-comment' + objId + ' .rate-red';
    ancestor            = '#sub-comment' + objId;
    userLikedElem       =   ancestor + ' .sub_com_user_liked';
    userDislikedElem    =   ancestor + ' .sub_com_user_disliked';
    userUnlikedElem     =   ancestor + ' .sub_com_user_unliked';
    userUndislikedElem  =   ancestor + ' .sub_com_user_undisliked';
  }
  if(objName == 'post')
  {
    upvoteSelector   = '#rate-post-form' + ' .rate-count.rate-green';
    downvoteSelector = '#rate-post-form' + ' .rate-count.rate-red';
    ancestor         = '#rate-post-form';
    userLikedElem       =  ancestor + ' .user_liked';
    userDislikedElem    =  ancestor + ' .user_disliked';
    userUnlikedElem     =  ancestor + ' .user_unliked';
    userUndislikedElem  =  ancestor + ' .user_undisliked';
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
    $(userLikedElem).hide();
    $(userUnlikedElem).show();
  }

  if(unvoteType == 'undislike' && curr_user == author)
  {
    $(userDislikedElem).hide();
    $(userUndislikedElem).show();
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

  var userLikedElem      = '';
  var userDislikedElem   = '';
  var userUnlikedElem    = '';
  var userUndislikedElem = '';

  if(objName == 'com')
  {
    upvoteSelector   = '#comment' + objId + ' .rate-count.rate-green';
    downvoteSelector = '#comment' + objId + ' .rate-count.rate-red';
    ancestor         = '#comment' + objId;
    userLikedElem       =  ancestor + ' .user_liked';
    userDislikedElem    =  ancestor + ' .user_disliked';
    userUnlikedElem     =  ancestor + ' .user_unliked';
    userUndislikedElem  =  ancestor + ' .user_undisliked';
  }
  if(objName == 'subcom')
  {
    upvoteSelector      =   '#sub-comment' + objId + ' .rate-green';
    downvoteSelector    =   '#sub-comment' + objId + ' .rate-red';
    ancestor            =   '#sub-comment' + objId;
    userLikedElem       =   ancestor + ' .sub_com_user_liked';
    userDislikedElem    =   ancestor + ' .sub_com_user_disliked';
    userUnlikedElem     =   ancestor + ' .sub_com_user_unliked';
    userUndislikedElem  =   ancestor + ' .sub_com_user_undisliked';
  }
  if(objName == 'post')
  {
    upvoteSelector   = '#rate-post-form' + ' .rate-count.rate-green';
    downvoteSelector = '#rate-post-form' + ' .rate-count.rate-red';
    ancestor         = '#rate-post-form';
    userLikedElem       =  ancestor + ' .user_liked';
    userDislikedElem    =  ancestor + ' .user_disliked';
    userUnlikedElem     =  ancestor + ' .user_unliked';
    userUndislikedElem  =  ancestor + ' .user_undisliked';
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
    $(userLikedElem).show();
    $(userUnlikedElem).hide();
    $(userDislikedElem).hide();
    $(userUndislikedElem).show();

  }
  else if(is_user_disliked)
  {
    $(userLikedElem).hide();
    $(userUnlikedElem).show();
    $(userDislikedElem).show();
    $(userUndislikedElem).hide();
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
     return;
   }
   else if(data['command'] == 'comRated')
   {

     var msg = data['comRateData'];
     var total_likes = msg['total_likes']
     var total_dislikes = msg['total_dislikes']
     update_rating('com', msg['comId'], total_likes, total_dislikes, msg['notificationType'], msg['author'], msg['notTrollKey']);
     return;
   }

   else if(data['command'] == 'subComRated')
   {
     var msg = data['subComRateData'];
     var total_likes = msg['total_likes']
     var total_dislikes = msg['total_dislikes']
     update_rating('subcom', msg['subComId'], total_likes, total_dislikes, msg['notificationType'], msg['author'], msg['notTrollKey']);
     return;
   }

   else if(data['command'] == 'postRated')
   {
     var msg = data['postRateData'];
     var total_likes = msg['total_likes']
     var total_dislikes = msg['total_dislikes']
     update_rating('post', null, total_likes, total_dislikes, msg['notificationType'], msg['author'], msg['notTrollKey']);
     return;
   }


   else if(data['command'] == 'NotifyforNotification')
   {
     wsUsersNotifications[roomName].send(JSON.stringify({
         'command'       : 'newNotification',
         'notificationId':  data['notificationId'],
     }));
     return;
   }

   else if(data['command'] == 'newNotification')
   {
     $('#empty-notifications').hide();
     update_notifications_log(data['notification'], newNotification=true);
   }

   else if(data['command'] == 'fetchNotifications')
   {
      if(data['notifications'].length<4)
      {
        $('#notifications-popup>.ronny-loadMoreArrow>.arrowDownHolder').first().hide();
      }

     $('#notifications-popup .notification-items').scrollTop($('#notifications-popup .notification-items')[0].scrollHeight);

     $('#notifications-popup .notification-items>*').remove();
     $('#empty-notifications').hide();

     for(let i=0;i<data['notifications'].length;i++)
     {

       update_notifications_log(data['notifications'][i]);

     }
     if(data['notifications'].length>=4)
     {
      $('#notifications-popup>.ronny-loadMoreArrow .arrowDownHolder').first().show();
     }

  }

  setBellAnimation(data, data['totalNotificationsCount']);

}



function setBellAnimation(data, totalNotificationsCount)
{


  if($('#notifications-popup .notification-item').length>0)
  {
    $('#ring-the-bell').show();
    $('#dont-ring-the-bell').hide();
    //$('.notification-counter').text($('#notifications-popup .notification-item').length.toString());
    $('.notification-counter').text(totalNotificationsCount);

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



function update_notifications_log(item, newNotification = false)
{

   //alert(1);
   var author = item['author'];
   var username_log_in = $('#curr-username-cn').val();
   //alert('author:' + author + '  userLogin:' + username_log_in);
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

    var item = null;
    if(newNotification == true)
    {
      $(popup_body).prepend('<div class="notification-item" '+ data +'></div>');
      item = $(popup_body).find('.notification-item').first();
    }
    else
    {
      $(popup_body).append('<div class="notification-item" '+ data +'></div>');
      item = $(popup_body).find('.notification-item').last();
    }

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

$('.ronny-loadMoreArrow').click(function(){
  $(this).children('.arrowDownHolder').hide();
  $(this).children('.spinnerHolder').show();
  callfetchNextNotificationsAjax(this);
});




function callfetchNextNotificationsAjax(e)
{
    var ancestor = $(e).parents('.notifications-popup').first();
    var items    = $(ancestor).find('.notification-items .notification-item');
    var numofNotifications = items.length;
    var maxNotificationsCnt = 4

    fetchNextNotificationsAjax(numofNotifications.toString(), maxNotificationsCnt.toString(), function(callback){
    loadNotificationLog(callback);
    $(e).children('.spinnerHolder').hide();
    if(callback.length < maxNotificationsCnt)
    {
      $(e).children('.arrowDownHolder').hide();
      return;
    }


    $(e).children('.arrowDownHolder').show();

   $('#notifications-popup .notification-items').scrollTop($('#notifications-popup .notification-items')[0].scrollHeight);


  });


}

function loadNotificationLog(notifications)
{
  for(i=0;i<notifications.length;i++)
  {
    update_notifications_log(notifications[i]);
  }

}
