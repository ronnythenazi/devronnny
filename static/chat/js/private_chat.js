
let chatSocket;

$(document).scroll(function(){
  var is_chat_activated = $('#hid-is-chat-activated').val();
  if(is_chat_activated == 'false')
  {
    return;
  }
  var elem = $('.chat_room_dialog');
  hide_elem_if_close_to_bottom(elem, bottom = 334, display='flex', extra_space=0);
});

$('.minimize_svg').click(function(){

  minimize_chat();

});
$('.maximize_svg').click(function(){

   maximize_chat();
});


function maximize_chat()
{
  $('.chat_room_dialog>*:not(script,link)').css('display', 'flex');
  $('.chat_room_dialog').css('right', '50%');
  $('.chat_room_dialog').css('top', '50%');
  $('.minimize_svg').show();
  $('.maximize_svg').hide();
}

function minimize_chat()
{
  $('.chat_room_dialog>*:not(.chat_room_header)').css('display', 'none');
  $('.chat_room_dialog').css('right','200px');
  $('.chat_room_dialog').css('top', '90%');
  $('.minimize_svg').hide();
  $('.maximize_svg').show();
}

function open_private_chat(to_username)
{
  $('#hid-is-chat-activated').val('true');
  get_names_and_avatars_private_chat_ajax(to_username ,function(callback){

    var status = callback[0]['status'];
    if(status == 'not-log-in')
    {
      ok_not_log_in_chat();
      return;
    }
    $('.sender-avatar').attr('src', callback[0]['avatar']);
    $('.reciever-avatar').attr('src', callback[1]['avatar']);
    $('.reciever-name').text(callback[1]['name']);
    $('.chat_room_dialog').css('display', 'flex');

    maximize_chat();
    set_txtarea_caret($('#txt-chat'));
  });


}

$('.ronny-style-field').focusin(function(){
  $(this).addClass('chat-input-activate');
});

$('.ronny-style-field').focusout(function(){
  $(this).removeClass('chat-input-activate');
});


$('#chat-send-btn-wrapper').click(send_message_chat);


function send_message_chat()
{

  const message = $('#txt-chat').val();
  chatSocket.send(JSON.stringify({
      'message': message
  }));
  $('#txt-chat').val('');
}


function update_private_chat_log(e)
{
  const data = JSON.parse(e.data);
  $('#chat-log').append('<div class="chat-row chat-row-sender">' + data.message + '</div>');
  
}

function close_chat()
{
  $('.chat_room_dialog').hide();
}


function chat_key_up(e)
{
  if (e.key === 'Enter')
  {  // enter, return
      send_message_chat();
  }
}

$(document).ready(function(){


 var roomName = $('#room-name').val();

  chatSocket = new WebSocket('ws://'+window.location.host+'/ws/chat/'+roomName + '/');


  chatSocket.onmessage =  update_private_chat_log;


  chatSocket.onclose = close_chat;

  document.querySelector('#txt-chat').focus();
  document.querySelector('#txt-chat').onkeyup = chat_key_up;

});
