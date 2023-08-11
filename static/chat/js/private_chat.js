
let chatSocket;

function clone_and_open_private_chat(from_username, to_username)
{
  var cloned_chat = $('.chat-room-template').first().clone();
  $(cloned_chat).removeClass('chat-room-template');

   //maybe not must done
  $(cloned_chat).find('script').remove();

   $('.chat-room-template').first().after(cloned_chat);


   assign_event_to_cloned_chat(cloned_chat);
   /*create_private_chat_room_ajax(from_username, to_username, function(callback){

       var chat_id = callback['chatId'];

       init_private_chat(chat_id, cloned_chat, from_username, to_username);
   });*/
   init_private_chat(cloned_chat, from_username, to_username);
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

function assign_event_to_cloned_chat(cloned)
{
  $(cloned).find('.minimize_svg').first().on('click', minimize_chat);
  $(cloned).find('.maximize_svg').first().on('click', maximize_chat);
  $(cloned).find('.chat-send-btn-wrapper').first().on('click', send_message_chat);
  $(cloned).find('.txt-chat').first().on('keyup',chat_key_up);

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

function init_private_chat(cloned_chat, from_username, to_username)
{

  var chat_dialog = $(cloned_chat);

  $(chat_dialog).find('.user-log-in-to-chat-dialog').first().val(from_username);
  $(chat_dialog).find('.hid-is-chat-activated').first().val('true');
  //$(chat_dialog).find('.hid-chat-id').first().val(chat_id);
  get_names_and_avatars_private_chat_ajax(from_username ,function(callback){

    var status = callback[0]['status'];
    if(status == 'not-log-in')
    {
      ok_not_log_in_chat();
      return;
    }

    connect_private_chat(chat_dialog, from_username, to_username);

    $(chat_dialog).find('.chat-input-txt').first().find('.sender-avatar').first().attr('src', callback[0]['avatar']);





    $(chat_dialog).not('.chat-room-template').first().css('display', 'flex');

    maximize_chat($(chat_dialog));
    set_txtarea_caret($(chat_dialog).find('.txt-chat').first());
  });


}

$('.ronny-style-field').focusin(function(){
  $(this).addClass('chat-input-activate');
});

$('.ronny-style-field').focusout(function(){
  $(this).removeClass('chat-input-activate');
});


//$('.chat-send-btn-wrapper').click(send_message_chat);


function send_message_chat()
{


  var ancestor = $(this).parents('.chat_room_dialog').not('.chat-room-template').first();
  var username = get_chat_user_login(ancestor);
  const message = $(ancestor).find('.txt-chat').first().val();
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

  var message = data.content;//data['message'];
  var author =  data['author'];

  var username = get_chat_user_login(ancestor);

  if(author == username)
  {

    //you send message

    $(chat_log).append('<div class="chat-row"></div>');
    var log_row =$(chat_log).find('.chat-row').last();
    $(log_row).append('<span class="sender-name blood-clr"></span>');
    $(log_row).append('<span class="chat-icon-user-body"><img class="sender-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="sender-bubble bubble"></span>');

    var bubble = $(log_row).find('.sender-bubble').first();
    $(bubble).html(message);


    var name = $(log_row).find('.sender-name').first();
    $(name).val(data['name']);
    var avatar = $(log_row).find('.sender-avatar').first();
    $(avatar).attr('src', data['avatar']);


  }
  else
  {

    //you recieve message
    $(chat_log).append('<div class="chat-row row-reciever"></div>');
    var log_row =$(chat_log).find('.chat-row').last();
    $(log_row).append('<span class="reciever-name blood-clr"></span>');
    $(log_row).append('<span class="chat-icon-user-body"><img class="reciever-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="reciver-bubble bubble"></span>');

    var bubble = $(log_row).find('.reciver-bubble').first();
    $(bubble).html(message);


    var name = $(log_row).find('.reciever-name').first();
    $(name).val(data['name']);
    var avatar = $(log_row).find('.reciever-avatar').first();
    $(avatar).attr('src', data['avatar']);


  }
}

function get_chat_user_login(chat_dialog)
{
  var username = $(chat_dialog).find('.user-log-in-to-chat-dialog').first().val();
  return username;
}

function close_chat(chat_dialog)
{
  $(chat_dialog).hide();
}


function chat_key_up(e)
{
  if (e.key === 'Enter')
  {  // enter, return
      //send_message_chat($(this));
  }
}
function connect_private_chat(chat_dialog, from_username, to_username)
{

  var roomName = $(chat_dialog).find('.room-name').first().val();

  if(is_debug(window.location.host))
  {


    chatSocket = new WebSocket('ws://'+window.location.host+'/ws/chat/'+ roomName + '/');
    //chatSocket = new ReconnectingWebSocket('ws://'+window.location.host+'/ws/chat/'+ roomName + '/');

  }
  else
  {

    //chatSocket = new WebSocket('ws://'+window.location.host+'/ws/chat/'+ roomName + '/');
    chatSocket = new WebSocket('wss://'+window.location.host+'/ws/chat/'+ roomName + '/');
    //chatSocket = new ReconnectingWebSocket('wss://'+window.location.host+'/ws/chat/'+ roomName + '/');
  }






   chatSocket.onmessage =  function(e){



     update_private_chat_log(e, chat_dialog);};


   chatSocket.onclose = function(){close_chat(chat_dialog);};

   chatSocket.onopen = function(e){
     fetchMessages(chat_dialog, from_username, to_username);
   };

   $(chat_dialog).find('.txt-chat').first().focus();

}


function fetchMessages(chat_dialog, from, to)
{
  //var chat_id = $(chat_dialog).find('.hid-chat-id').first().val();
  chatSocket.send(JSON.stringify({'command':'fetch_messages', 'from':from, 'to':to}));
}
