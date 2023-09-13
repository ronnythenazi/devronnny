var wsMyprivateToken;
var wsMyPublicToken;
var wsUsersPublicTokens = {};


$(document).ready(function(){
  secure_connect();


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
   get_user_public_token_ajax(toUserName, function(callback){
      var publicToken = callback['publicToken'];
      connectToSendNotification(publicToken, notificationId);
   });
}

function secure_connect()
{
    get_user_tokens_ajax(function(callback){
    var token       = callback['token'];
    var publicToken = callback['publicToken'];
    $('#user-token').val(token);
    $('#user-public-token').val(publicToken);
    connectNotifications(token);
    connectToBeNotifiedforNotifiations(publicToken);
  });
}

function connectToSendNotification(publicToken, notificationId)
{
  var url="";
  if(is_debug(window.location.host))
  {
    url = 'ws://'+window.location.host+'/ws/notifications/'+ publicToken  + '/';
  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/notifications/'+ publicToken  + '/';

  }
    wsUsersPublicTokens[publicToken] = new WebSocket(url);

    wsUsersPublicTokens[publicToken].onopen = function(e){

    sendNotificationOfNotification(publicToken, notificationId);
  };

  wsUsersPublicTokens[publicToken].onclose = function(){
    setTimeout(function() {
     connectToSendNotification(publicToken, notificationId);
   }, 1000);

  };

}

function sendNotificationOfNotification(publicToken, notificationId)
{
  wsUsersPublicTokens[publicToken].send(JSON.stringify({
      'command'       : 'NotifyforNotification',
      'notificationId':  notificationId,
  }));
}

function connectToBeNotifiedforNotifiations(publicToken)
{
  var url="";
  if(is_debug(window.location.host))
  {
    url = 'ws://'+window.location.host+'/ws/notifications/'+ publicToken  + '/';
  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/notifications/'+ publicToken  + '/';

  }
    wsMyPublicToken = new WebSocket(url);

    wsMyPublicToken.onopen = function(e){


  };


  wsMyPublicToken.onmessage =  function(e){
    fetchNewNotification(e);

  };


   wsMyPublicToken.onclose = function(){
    setTimeout(function() {
     connectToBeNotifiedforNotifiations(publicToken);
   }, 1000);

  };
}

function connectNotifications(token)
{
  var url="";
  if(is_debug(window.location.host))
  {
    url = 'ws://'+window.location.host+'/ws/notifications/'+ token  + '/';
  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/notifications/'+ token  + '/';

  }
  wsMyprivateToken = new WebSocket(url);

  wsMyprivateToken.onopen = function(e){

    fetchNotifications(token);
  };


   wsMyprivateToken.onmessage =  function(e){
     var data = JSON.parse(e.data);

   load_notifications(data);};


   wsMyprivateToken.onclose = function(){
     setTimeout(function() {
      connectNotifications(token);
    }, 1000);

   };


}
function fetchNewNotification(e, notificationId)
{
  var data = JSON.parse(e.data);
  if(data['command'] == 'NotifyforNotification')
  {
    wsMyprivateToken.send(JSON.stringify({
        'command'       : 'fetchNotifications',
        'notificationId':  data['notificationId'],
    }));
  }

}
function fetchNotifications(token)
{

  wsMyprivateToken.send(JSON.stringify({
      'command'       : 'fetchNotifications',
  }));
}

function load_notifications(data)
{
   $('#notifications-popup .notification-items>*').remove();
   $('#empty-notifications').hide();


   if(data['command'] == 'newNotification')
   {

     update_notifications_log(data['notification']);


   }

   else if(data['command'] == 'fetchNotifications')
   {


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
      return;
    }
    $('#ring-the-bell').hide();
    $('#dont-ring-the-bell').show();


    if(data['command'] != 'newNotification')
    {
      return;
    }

    if(data['notificationId'].length > 0)
    {

      $('#notification-sound')[0].play();

    }
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
