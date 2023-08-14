
let chatSocket;

function close_chat_dialog()
{
  var chat_dialog = $(this).parents('.chat_room_dialog').first();
  $(chat_dialog).remove();
}


function open_private_chat(from_username, to_username)
{
  generate_private_room(from_username, to_username, function(result){
    var status = result['status'];

    if (status == 'not_authenticated')
    {
      //ok_not_authenticated_to_chat();
      //return;
    }
    var roomName = result['roomName'];
    var chat_win_id = 'room-name-' + roomName;
    var chat_win_selector = '#' + chat_win_id;
    var chat_dialog;
    if($(chat_win_selector).length)
    {

      chat_dialog = $(chat_win_selector).parents('.chat_room_dialog').first();
      maximize_chat($(chat_dialog));
    }
    else
    {
      chat_dialog = cloned_and_assign_events();
      $(chat_dialog).find('.room-name').first().attr('id', chat_win_id);
      var chatId   = result['chatId'];
      init_private_chat(chat_dialog, from_username, to_username, roomName, chatId);
    }







  //var cloned_chat = $('.chat-room-template').first().clone();
  //$(cloned_chat).removeClass('chat-room-template');
  //$(cloned_chat).find('.room-name').first().attr(id, chat_win_id);

   //maybe not must done
  //$(cloned_chat).find('script').remove();

   //$('.chat-room-template').first().after(cloned_chat);





   });
}

$(document).scroll(function(){
  $('.hid-is-chat-activated').each(function(){

    var is_chat_activated = $(this).val();
    if(is_chat_activated == 'false')
    {
      return;
    }
    var elem = $(this).parents('.chat_room_dialog').not('.chat-room-template').first();
    hide_elem_if_close_to_bottom(elem, bottom = 334, display='flex', extra_space=0);

  });

});

function cloned_and_assign_events()
{
  var cloned = $('.chat-room-template').first().clone();
  $(cloned).removeClass('chat-room-template');


   //maybe not must done
  $(cloned).find('script').remove();

   $('.chat-room-template').first().after(cloned);
  $(cloned).find('.minimize_svg').first().on('click', minimize_chat);
  $(cloned).find('.maximize_svg').first().on('click', maximize_chat);
  $(cloned).find('.close_chat_svg').first().on('click', close_chat_dialog)
  $(cloned).find('.chat-send-btn-wrapper').first().on('click', btn_send_clicked);
  $(cloned).find('.txt-chat').first().on('keyup',chat_key_up);

  return cloned;

}
/*$('.minimize_svg').click(minimize_chat);
$('.maximize_svg').click(maximize_chat);*/





function maximize_chat()
{
  var ancestor = $(this).parents('.chat_room_dialog').not('.chat-room-template').first();
  $(ancestor).children().not('script,link').css('display', 'flex');
  $(ancestor).css('right', '50%');

  var popup_height = get_css_variable_val('--chat-popup-height').replace('px', '');
  var top = (parseInt(popup_height) / 2) + "px";




  $(ancestor).css('top', top);
  $(ancestor).find('.minimize_svg').first().show();
  $(ancestor).find('.maximize_svg').first().hide();
}

function minimize_chat()
{
  var ancestor = $(this).parents('.chat_room_dialog').not('.chat-room-template').first();
  $(ancestor).children().not('.chat_room_header').css('display', 'none');
  $(ancestor).css('right','200px');
  $(ancestor).css('top', '90%');
  $(ancestor).find('.minimize_svg').first().hide();
  $(ancestor).find('.maximize_svg').first().show();
}

function init_private_chat(cloned_chat, from_username, to_username, roomName, chatId)
{

  var chat_dialog = $(cloned_chat);

  $(chat_dialog).find('.user-log-in-to-chat-dialog').first().val(from_username);
  $(chat_dialog).find('.hid-is-chat-activated').first().val('true');
  $(chat_dialog).find('.hid-chat-id').first().val(chatId);
  get_names_and_avatars_private_chat_ajax(from_username ,function(callback){

    var status = callback[0]['status'];
    if(status == 'not-log-in')
    {
      ok_not_log_in_chat();
      return;
    }

    //set_private_chat(chat_dialog, from_username, to_username, roomName, chatId);
    connect(chat_dialog, roomName, chatId);

    $(chat_dialog).find('.chat-input-txt').first().find('.sender-avatar').first().attr('src', callback[0]['avatar']);





    $(chat_dialog).not('.chat-room-template').first().css('display', 'flex');

    maximize_chat($(chat_dialog));
    //set_txtarea_caret($(chat_dialog).find('.txt-chat').first());
  });


}

$('.ronny-style-field').focusin(function(){
  $(this).addClass('chat-input-activate');
});

$('.ronny-style-field').focusout(function(){
  $(this).removeClass('chat-input-activate');
});


function btn_send_clicked()
{
  send_message_chat($(this));
}


function send_message_chat(sender)
{
  var ancestor = $(sender).parents('.chat_room_dialog').not('.chat-room-template').first();

  var username = get_chat_user_login(ancestor);

  var message = $(ancestor).find('.txt-chat').first().val();
  var chat_id = $(ancestor).find('.hid-chat-id').first().val();
  chatSocket.send(JSON.stringify({
      'command': 'new_message',
      'message': message,
      'from'   : username,
      'chatId' : chat_id,
  }));

  $(ancestor).find('.txt-chat').first().val('');
}


function update_private_chat_log(e, chat_dialog)
{


    const data = JSON.parse(e.data);

    if(data['command'] == 'messages')
    {
      $(chat_dialog).find('.hid-chat-id').first().val(data['chatId']);


      for(let i=0;i<data['messages'].length;i++)
      {

        create_message(data['messages'][i], chat_dialog);
      }
    }
    else if(data['command'] == 'new_message')
    {

      create_message(data['message'], chat_dialog);
    }




}

function create_message(data, chat_dialog)
{

  var ancestor = $(chat_dialog);
  var chat_log = $(ancestor).find('.chat-log').first()

  var message = data.content;
  var author =  data['author'];

  var username = get_chat_user_login(ancestor);

  if(author == username)
  {

    //you send message

    $(chat_log).append('<div class="chat-row"></div>');
    var log_row =$(chat_log).find('.chat-row').last();

    $(log_row).append('<div class="contact"></div>');
    var contact = $(log_row).find('.contact').first();
    $(contact).append('<span class="sender-name blood-clr"></span>');
    $(contact).append('<span class="chat-icon-user-body"><img class="sender-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="sender-bubble bubble"></span>');

    /*$(log_row).append('<span class="sender-name blood-clr"></span>');
    $(log_row).append('<span class="chat-icon-user-body"><img class="sender-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="sender-bubble bubble"></span>');*/

    var bubble = $(log_row).find('.sender-bubble').first();
    $(bubble).html(message);


    var name = $(log_row).find('.sender-name').first();
    $(name).html(data['name']);
    var avatar = $(log_row).find('.sender-avatar').first();
    $(avatar).attr('src', data['avatar']);


  }
  else
  {

    //you recieve message
    $(chat_log).append('<div class="chat-row row-reciever"></div>');
    var log_row =$(chat_log).find('.chat-row').last();


    $(log_row).append('<div class="contact"></div>');
    var contact = $(log_row).find('.contact').first();
    $(contact).append('<span class="reciever-name blood-clr"></span>');
    $(contact).append('<span class="chat-icon-user-body"><img class="reciever-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="reciver-bubble bubble"></span>');

    /*$(log_row).append('<span class="reciever-name blood-clr"></span>');
    $(log_row).append('<span class="chat-icon-user-body"><img class="reciever-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="reciver-bubble bubble"></span>');*/

    var bubble = $(log_row).find('.reciver-bubble').first();
    $(bubble).html(message);


    var name = $(log_row).find('.reciever-name').first();
    $(name).html(data['name']);
    var avatar = $(log_row).find('.reciever-avatar').first();
    $(avatar).attr('src', data['avatar']);


  }
  var inserted_elem = $(chat_log).find('.chat-row').last();
  var extra = get_css_variable_val('--chat-log-gap').replace('px', '');
  scroll_down_the_gap_on_new_msg($(chat_log), inserted_elem, extra);

}

function get_chat_user_login(chat_dialog)
{
  var username = $(chat_dialog).find('.user-log-in-to-chat-dialog').first().val();
  return username;
}

function close_chat(chat_dialog)
{
  //$(chat_dialog).remove();
}


function chat_key_up(e)
{
   var keyCode = e.keyCode || e.which;

   if (keyCode === 13 && !e.ctrlKey)
   {
      e.preventDefault();
      send_message_chat($(this));
      return false;
    // Ajax code here

   }


  if (keyCode === 13  && e.ctrlKey)
  {
    $(this).val(function(i,val)
    {
        var line_height = $(this).prop('line-height');

        $(this).scrollTop($(this).scrollTop() + line_height);
        return val + "\n";
    });

  }

}


function connect(chat_dialog, roomName, chatId)
{

  //var roomName = $(chat_dialog).find('.room-name').first().val();
  var url="";
  if(is_debug(window.location.host))
  {

    url = 'ws://'+window.location.host+'/ws/chat/'+ roomName + '/';

    //$(chat_dialog).find('.ws-url').first().val(url);

    //chatSocket = new WebSocket('ws://'+window.location.host+'/ws/chat/'+ roomName + '/');
    //chatSocket = new ReconnectingWebSocket('ws://'+window.location.host+'/ws/chat/'+ 'PrivateChat92' + '/');

  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/chat/'+ roomName + '/';
  //  $(chat_dialog).find('.ws-url').first().val(url);

    //chatSocket = new WebSocket('ws://'+window.location.host+'/ws/chat/'+ roomName + '/');
    //chatSocket = new WebSocket('wss://'+window.location.host+'/ws/chat/'+ roomName + '/');
    //chatSocket = new ReconnectingWebSocket('wss://'+window.location.host+'/ws/chat/'+ roomName + '/');
  }
  chatSocket = new WebSocket(url);

  chatSocket.onopen = function(e){
    //fetchMessages(chat_dialog, from_username, to_username, chatId);
    fetchMessages(chat_dialog, chatId);
  };


   chatSocket.onmessage =  function(e){



   update_private_chat_log(e, chat_dialog);};


   chatSocket.onclose = function(){
     setTimeout(function() {
      connect(chat_dialog, roomName, chatId);
    }, 1000);

   };



   $(chat_dialog).find('.txt-chat').first().focus();

}


//function fetchMessages(chat_dialog, from, to, chatId)
function fetchMessages(chat_dialog, chatId)
{


   //chatSocket.send(JSON.stringify({'command':'fetch_messages', 'from':from, 'to':to, 'chatId':chatId}));
   chatSocket.send(JSON.stringify({'command':'fetch_messages',  'chatId':chatId}));
}
