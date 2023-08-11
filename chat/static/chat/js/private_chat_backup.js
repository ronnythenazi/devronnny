
let chatSocket;
let chat_dialog;

$(document).scroll(function(){
  $('.hid-is-chat-activated').each(function(){

    var is_chat_activated = $(this).val();
    if(is_chat_activated == 'false')
    {
      return;
    }
    var elem = $(this).parents('.chat_room_dialog').first();
    hide_elem_if_close_to_bottom(elem, bottom = 334, display='flex', extra_space=0);

  });

});

$('.minimize_svg').click(minimize_chat);
$('.maximize_svg').click(maximize_chat);





function maximize_chat()
{
  var ancestor = $(this).parents('.chat_room_dialog').first();
  $(ancestor).children().not('script,link').css('display', 'flex');
  $(ancestor).css('right', '50%');
  $(ancestor).css('top', '50%');
  $(ancestor).find('.minimize_svg').first().show();
  $(ancestor).find('.maximize_svg').first().hide();
}

function minimize_chat()
{
  var ancestor = $(this).parents('.chat_room_dialog').first();
  $(ancestor).children().not('.chat_room_header').css('display', 'none');
  $(ancestor).css('right','200px');
  $(ancestor).css('top', '90%');
  $(ancestor).find('.minimize_svg').first().hide();
  $(ancestor).find('.maximize_svg').first().show();
}

function open_private_chat(to_username)
{
  $(chat_dialog).find('.hid-is-chat-activated').first().val('true');
  get_names_and_avatars_private_chat_ajax(to_username ,function(callback){

    var status = callback[0]['status'];
    if(status == 'not-log-in')
    {
      ok_not_log_in_chat();
      return;
    }
    $(chat_dialog).find('.sender-avatar').first().attr('src', callback[0]['avatar']);
    $(chat_dialog).find('.reciever-avatar').first().attr('src', callback[1]['avatar']);
    $(chat_dialog).find('.reciever-name').first().text(callback[1]['name']);
    $(chat_dialog).find('.chat_room_dialog').first().css('display', 'flex');

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


$('.chat-send-btn-wrapper').click(send_message_chat);


function send_message_chat()
{

  var ancestor = $(this).parents('.chat_room_dialog').first();
  const message = $(ancestor).find('.txt-chat').first().val();
  chatSocket.send(JSON.stringify({
      'message': message
  }));
  $(ancestor).find('.txt-chat').first().val('');
}


function update_private_chat_log(e)
{
  const data = JSON.parse(e.data);
  var ancestor = $(chat_dialog);
  var chat_log = $(ancestor).find('.chat-log').first()
  $(chat_log).append('<div class="chat-row chat-row-sender">' + data.message + '</div>');
  var log_row =$(chat_log).find('.chat-row').first();
  $(log_row).find('.reciever-name').val();



}

function close_chat()
{
  $(chat_dialog).hide();
}


function chat_key_up(e)
{
  if (e.key === 'Enter')
  {  // enter, return
      send_message_chat($(this));
  }
}

$(document).ready(function(){

 chat_dialog = $('.chat_room_dialog').first();
 var roomName = $(chat_dialog).find('.room-name').first().val();

 if(is_debug(window.location.host))
 {
   chatSocket = new WebSocket('ws://'+window.location.host+'/ws/chat/'+ roomName + '/');
 }
 else
 {
   chatSocket = new WebSocket('wss://'+window.location.host+'/ws/chat/'+ roomName + '/');
 }




  chatSocket.onmessage =  update_private_chat_log;


  chatSocket.onclose = close_chat;
  $(chat_dialog).find('.txt-chat').first().focus();
  $(chat_dialog).find('.txt-chat').first().keyup(chat_key_up);


});
