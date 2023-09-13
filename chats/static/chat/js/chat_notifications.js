const ws_arr = {};

function update_chat_notifications(result)
{
  $('#c_notifications_popup_mini .chat_notification_items>*').remove();
  $('#empty-notifications-chat').hide();
  
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

    var cloned = $('#chat-thumb').clone(true);
    $(cloned).attr('id', '');
    var thumb_holder = $(item).find('.c_notification_cell_thumb');
    $(thumb_holder).append(cloned);
    $(cloned).css('display', 'block');

    //$(item).append('<div class="c_notification_cell_settings"></div>');

    $(item).find('.c_notification_cell_author').append('<img src="">');
    var img = $(item).find('.c_notification_cell_author').find('img');
    $(img).attr('src', avatar);


    var subitem = $(item).find('.c_notification_cell_contentsnip');
    $(subitem).append('<div class="c_notification_subcell_contentsnip_msg"></div>');
    $(subitem).append('<div class="c_notification_subcell_contentsnip_timepassed"></div>');
    var msg = $(subitem).find('.c_notification_subcell_contentsnip_msg');
    var prefix = author_name + " " + "שלח" + ":" ;
    $(msg).append('<p class="bluish-clr nowrap-child">'+ prefix +'</p>');
    $(msg).append('<p class="wrap-child">'+ content +'</p>');
    //$(msg).html(content);
    var t_lbl = $(subitem).find('.c_notification_subcell_contentsnip_timepassed');
    $(t_lbl).html(get_friendly_time_format(time_passed));




    //subitem = $(item).find('.c_notification_cell_settings');
  //  $(subitem).append('<div class="c_notification_cell_settings_dot"></div>');
  //  $(subitem).append('<div class="c_notification_cell_settings_dot"></div>');
  //  $(subitem).append('<div class="c_notification_cell_settings_dot"></div>');


  }

  assign_delegates();
  if(result.length>0)
  {
    $('.chat-path1, .chat-path2').addClass('effect-active');
  }


}


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
   connect_to_your_chat_rooms($('#curr-username-cn').val());
   show_chat_notifications();

   var elem_to_focus = $('#c_notifications_popup_mini');
   var trigger_elem = $('#chat-notifications-menuItem');
   focusout(elem_to_focus, trigger_elem);
   $(elem_to_focus).css('right', offset_right($(trigger_elem)));
   var top = $('.main-menu').height() - 50;
   $(elem_to_focus).css('top', top + 'px');

});
function show_chat_notifications()
{
    notifications_minimal_view_ajax(function(result){
    update_chat_notifications(result);
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
     show_chat_notifications();
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
