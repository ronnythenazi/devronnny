const ws_arr = {};


function loadChatNotifications(result)
{
  for(var i=0;i<result.length;i++)
  {
    var item = result[i];
    var author_name          = item['author_name'];
    var avatar               = item['avatar'];
    var content              = item['content'];
    var time_passed          = item['time_passed'];
    var roomName             = item['roomName'];
    var chatId               = item['chatId'];
    var authorUsername       = item['author'];


    var popup_body = $('#c_notifications_popup_mini .chat_notification_items');
    var data = 'roomName="' + roomName + '" ';
        data += 'chatId ="' + chatId  + '" ';
        data += 'authorUsername ="' + authorUsername  + '" ';
    $(popup_body).append('<div class="chat_notification_item" '+ data +'></div>');
    var item = $(popup_body).find('.chat_notification_item').last();
    $(item).append('<div class="c_notification_cell_author"></div>');
    $(item).append('<div class="c_notification_cell_contentsnip"></div>');
    $(item).append('<div class="c_notification_cell_thumb"></div>');

    var thumb_holder = $(item).find('.c_notification_cell_thumb');


    var prefix = author_name + " " + "שלח" + ":" ;
    $(item).append('<p class="author-name-lbl bluish-clr nowrap-child">'+ prefix +'</p>');
    //$(thumb_holder).append('<div class="c_notification_subcell_contentsnip_timepassed"></div>');
    //var t_lbl = $(thumb_holder).find('.c_notification_subcell_contentsnip_timepassed');
    //$(t_lbl).html(get_friendly_time_format(time_passed));

    /*var cloned = $('#chat-thumb').clone(true);
    $(cloned).attr('id', '');
    var thumb_holder = $(item).find('.c_notification_cell_thumb');
    $(thumb_holder).append(cloned);
    $(cloned).css('display', 'block');*/

    var prefix = author_name + " " + "שלח" + ":" ;
    //$(item).find('.c_notification_cell_author').append('<p class="author-name-lbl bluish-clr nowrap-child">'+ prefix +'</p>');
    $(item).find('.c_notification_cell_author').append('<img src="">');

    var img = $(item).find('.c_notification_cell_author').find('img');
    $(img).attr('src', avatar);


    var subitem = $(item).find('.c_notification_cell_contentsnip');
    $(subitem).append('<div class="c_notification_subcell_contentsnip_msg"></div>');
    $(subitem).append('<div class="c_notification_subcell_contentsnip_timepassed"></div>');
    var msg = $(subitem).find('.c_notification_subcell_contentsnip_msg');
    //var prefix = author_name + " " + "שלח" + ":" ;
    //$(msg).append('<p class="bluish-clr nowrap-child">'+ prefix +'</p>');
    $(msg).append('<p class="wrap-child">'+ content +'</p>');

    var t_lbl = $(subitem).find('.c_notification_subcell_contentsnip_timepassed');
    $(t_lbl).html(get_friendly_time_format(time_passed));

  }

  assign_delegates();
  if(result.length>0)
  {
    $('.chat-path1, .chat-path2').addClass('effect-active');

  }
  if(result.length>=4)
  {
    $('#c_notifications_popup_mini').find('.arrowDownHolder').first().show();
  }
  var popupBody = $('#c_notifications_popup_mini .chat_notification_items');
  $(popupBody).scrollTop($(popupBody)[0].scrollHeight);
}

/*function update_chat_notifications(result)
{
  $('#c_notifications_popup_mini .chat_notification_items>*').remove();
  $('#empty-notifications-chat').hide();
  loadChatNotifications(result);
}*/


function assign_delegates()
{
  $('.chat_notification_items').on('click','.chat_notification_item', notification_item_click);
}

function notification_item_click(e)
{
  var loginUsername = $('#curr-username-cn').val();
  var author = $(this).attr("authorUsername");
  if(is_curs_inside_rect_elem($(this).find('.c_notification_cell_author'), e))
  {
    go_to_user_public_profile(author);
    return;
  }

  var roomName = $(this).attr("roomName");
  var chatId   = $(this).attr("chatId");

  open_chat(loginUsername, chatId, roomName);
  $('#c_notifications_popup_mini').hide();
}



$('#chat-notifications-menuItem').click(function(){


  if(!$('#c_notifications_popup_mini .chat_notification_item').length)
  {
     $('#empty-notifications-chat').css('display', 'flex');
  }


});


$(window).scroll(function(){
  var elem_to_focus = $('#c_notifications_popup_mini');
  var top = $('.main-menu').height() - 50;
  $(elem_to_focus).css('top', top + 'px');
});

$(document).ready(function(){

  if(!$('#curr-username-cn').length)
  {
    return;
  }


   var elem_to_focus = $('#c_notifications_popup_mini');
   var trigger_elem = $('#chat-notifications-menuItem');
   focusout(elem_to_focus, trigger_elem);
   $(elem_to_focus).css('right', offset_right($(trigger_elem)));
   var top = $('.main-menu').height() - 50;
   $(elem_to_focus).css('top', top + 'px');



   connect_to_your_chat_rooms($('#curr-username-cn').val());
   show_chat_notifications(0, 4, freshLoad=true);



});
function show_chat_notifications(fromNumOfNotifications, numOfnewNotifications, freshLoad=false)
{
    fetchNextChatNotificationsAjax(fromNumOfNotifications, numOfnewNotifications, function(result){
    if(freshLoad == true)
    {
      $('#empty-notifications-chat').hide();
    }
    loadChatNotifications(result)
    //update_chat_notifications(result);
  });
}
function load_chat_message(e, username, chatId, roomName)
{
   const data = JSON.parse(e.data);
   var msg = data['message'];
   var author = data['author'];
   if(author == username)
   {
     return;
   }


   if(data['command'] == 'new_message')
   {
     open_chat(username, chatId, roomName);
     $('.update_audio').first()[0].play();

     //not use
     var items    = $('#c_notifications_popup_mini .chat_notification_items .chat_notification_item');
     var numofNotifications = items.length;
     //show_chat_notifications(0, numofNotifications);
     //end not use
     $('#c_notifications_popup_mini .chat_notification_items>*').remove();
     show_chat_notifications(0, 4, freshLoad=true);
   }


}


function connect_to_room(username, chatId, roomName)
{
  if(is_debug(window.location.host))
  {

    url = 'ws://'+window.location.host+'/ws/chat/'+ roomName + '/';



  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/chat/'+ roomName + '/';

  }

  ws_arr[roomName] = new WebSocket(url);
  ws_arr[roomName].onmessage  = function(e){load_chat_message(e, username, chatId, roomName);};


  ws_arr[roomName].onclose = function(){
    setTimeout(function() {
     connect_to_room(username, chatId, roomName);
        }, 1000);


    }
}
function connect_to_your_chat_rooms(username)
{

   var rooms = get_you_rooms_ajax(function(rooms){
      for(var i=0;i<rooms.length;i++)
      {
        var room = rooms[i];
        var roomName = room['roomName'];
        var chatId   = room['chatId'];
        connect_to_room(username, chatId, roomName);

      }
   });
}

$('.loadMoreArrow').click(function(){
  $(this).children('.arrowDownHolder').hide();
  $(this).children('.spinnerHolder').show();
  callfetchNextChatNotificationsAjax(this);
});




function callfetchNextChatNotificationsAjax(e)
{
    var ancestor = $(e).parents('.ronny-notification-popup').first();
    var items    = $(ancestor).find('.chat_notification_items .chat_notification_item');
    var numofNotifications = items.length;

    fetchNextChatNotificationsAjax(numofNotifications.toString(), 4, function(callback){
    loadChatNotifications(callback);
    $(e).children('.spinnerHolder').hide();
    if(callback.length > 0)
    {
      $(e).children('.arrowDownHolder').show();
      return;
    }

    $(e).children('.arrowDownHolder').hide();


  });


}
