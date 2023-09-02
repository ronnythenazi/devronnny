
let sockets = {};

function close_chat_dialog()
{
  var chat_dialog = $(this).parents('.chat_room_dialog').first();
  $(chat_dialog).remove();
}
function active_chat_waiting_animation(chat_dialog)
{
  $(chat_dialog).find('.chat-log').addClass('effect-activated');
  $(chat_dialog).find('.chat-input').addClass('effect-activated');
  $(chat_dialog).find('.hourgalss').show();
  //hourgalss-waiting-animation
}

function end_chat_waiting_animation(chat_dialog)
{
  $(chat_dialog).find('.chat-log').removeClass('effect-activated');
  $(chat_dialog).find('.chat-input').removeClass('effect-activated');
  $(chat_dialog).find('.hourgalss').hide();
}

function open_chat(username, chatId, roomName)
{
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
    active_chat_waiting_animation(chat_dialog);
    init_private_chat(chat_dialog, username, roomName, chatId);
  }

}

function open_personal_chat(from_username, to_username)
{
    generate_private_room(from_username, to_username, function(result){
    var status = result['status'];

    if (status == 'not_authenticated')
    {
      ok_not_authenticated_to_chat();
      return;
    }

    var roomName = result['roomName'];
    var chat_win_id = 'room-name-' + roomName;
    var chat_win_selector = '#' + chat_win_id;
    var chat_dialog;
    var chatId  = result['chatId'];
    if($(chat_win_selector).length)
    {

      chat_dialog = $(chat_win_selector).parents('.chat_room_dialog').first();
      maximize_chat($(chat_dialog));
    }
    else
    {
      chat_dialog = cloned_and_assign_events();
      $(chat_dialog).find('.room-name').first().attr('id', chat_win_id);

      init_private_chat(chat_dialog, from_username, roomName, chatId);
    }

   return {'roomName':roomName, 'chatId':chatId};
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
  $(ancestor).children().not('script,link,audio, audio>*').css('display', 'flex');
  $(ancestor).css('left', '50%');

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
  $(ancestor).css('left','90%');
  $(ancestor).css('top', '90%');
  $(ancestor).find('.minimize_svg').first().hide();
  $(ancestor).find('.maximize_svg').first().show();
}

function init_private_chat(cloned_chat, from_username, roomName, chatId)
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


    connect(chat_dialog, roomName, chatId);

    $(chat_dialog).find('.chat-input-txt').first().find('.sender-avatar').first().attr('src', callback[0]['avatar']);





    $(chat_dialog).not('.chat-room-template').first().css('display', 'flex');

    draggable($(chat_dialog));
    disable_draggable(chat_dialog);
    enable_draggable(chat_dialog);

    maximize_chat($(chat_dialog));

  });


}
function disable_draggable(dialog)
{
  $(dialog).children('.chat-log').on('mouseover', function(){

    set_undraggable(dialog);
  });
}

function enable_draggable(dialog)
{
  $(dialog).children('.chat-log').on('mouseleave', function(){

    set_draggable(dialog);
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
  var roomName = $(ancestor).find('.room-name').first().val();
  //var username = get_chat_user_login(ancestor);

  var message = $(ancestor).find('.txt-chat').first().val();
  if(String(message).replace(/\s+/g, ' ').trim().length <= 0)
  {
    return;
  }
  var chat_id = $(ancestor).find('.hid-chat-id').first().val();
  sockets[roomName].send(JSON.stringify({
      'command': 'new_message',
      'message': message,
      //'from'   : username,
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
      $('.hide_audio').first()[0].play();


    }
    else if(data['command'] == 'typing')
    {
      notify_that_user_is_typing(data, chat_dialog);
    }

  end_chat_waiting_animation(chat_dialog);

}


function get_typing_elem_unique_cname(chatId, author)
{
   var typing_elem_unique_cname = 'typing-' + chatId + '-' + author;
   return typing_elem_unique_cname;
}

function notify_that_user_is_typing(data, chat_dialog)
{
  var chat_log = $(chat_dialog).find('.chat-log').first();

  var author = data['author'];
  var username_log_in = get_chat_user_login(chat_dialog);

  if(author == username_log_in)
  {
    return;
  }
  var chatId = $(chat_dialog).find('.hid-chat-id').first().val();

  var typing_elem_unique_cname = get_typing_elem_unique_cname(chatId, author);
  var typing_elem = '<div class="typing ' + typing_elem_unique_cname +  ' reciever-clr"></div>';
  var typing_elem_selector = '.' + typing_elem_unique_cname;
  if($(typing_elem_selector).length)
  {
    return;
  }

  $(chat_log).append('<div class="chat-row row-reciever"></div>');
  var log_row =$(chat_log).find('.chat-row').last();

  $(log_row).append('<div class="contact"></div>');
  var contact = $(log_row).find('.contact').first();
  $(contact).append('<span class="reciever-name reciever-clr"></span>');
  $(contact).append('<span class="chat-icon-user-log"><img class="reciever-avatar" src="" alt=""></span>');

  var name = $(log_row).find('.reciever-name').first();
  $(name).html(data['name']);
  var avatar = $(log_row).find('.reciever-avatar').first();
  $(avatar).attr('src', data['avatar']);

  $(log_row).append(typing_elem);

  var inserted_elem = $(chat_log).find('.chat-row').last();
  var extra = get_css_variable_val('--chat-log-gap').replace('px', '');
  scroll_down_the_gap_on_new_msg($(chat_log), inserted_elem, extra);

  setTimeout(function(){$(log_row).remove()}, 6000);



}

function create_message(data, chat_dialog)
{

  var ancestor = $(chat_dialog);

  var chat_log = $(ancestor).find('.chat-log').first();

  var message = data.content;
  var author =  data['author'];



  var chatId = $(chat_dialog).find('.hid-chat-id').first().val();
  var typing_elem_unique_cname = get_typing_elem_unique_cname(chatId, author);
  var typing_elem_selector = '.' + typing_elem_unique_cname;
  if($(typing_elem_selector).length)
  {
    $(typing_elem_selector).find('.chat-row').first().remove();
  }



  var username = get_chat_user_login(ancestor);

  if(author == username)
  {

    //you send message

    $(chat_log).append('<div class="chat-row"></div>');
    var log_row =$(chat_log).find('.chat-row').last();

    $(log_row).append('<div class="contact"></div>');
    var contact = $(log_row).find('.contact').first();
    $(contact).append('<span class="sender-name sender-clr"></span>');
    $(contact).append('<span class="chat-icon-user-log"><img class="sender-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="sender-bubble bubble"></span>');



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
    $(contact).append('<span class="reciever-name reciever-clr"></span>');
    $(contact).append('<span class="chat-icon-user-log"><img class="reciever-avatar" src="" alt=""></span>');
    $(log_row).append('<span class="reciver-bubble bubble"></span>');



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
  var chat_dialog = $(this).parents('.chat_room_dialog').not('.chat-room-template').first();
  var roomName = $(chat_dialog).find('.room-name').first().val();
  sockets[roomName].send(JSON.stringify({'command':'typing'}));

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

  var url="";
  if(is_debug(window.location.host))
  {

    url = 'ws://'+window.location.host+'/ws/chat/'+ roomName + '/';



  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/chat/'+ roomName + '/';

  }
  sockets[roomName] = new WebSocket(url);
  $(chat_dialog).find('.room-name').first().val(roomName);

  sockets[roomName].onopen = function(e){

    fetchMessages(chat_dialog, chatId, roomName);
  };


   sockets[roomName].onmessage =  function(e){



   update_private_chat_log(e, chat_dialog);};


   sockets[roomName].onclose = function(){
     setTimeout(function() {
      connect(chat_dialog, roomName, chatId);
    }, 1000);

   };



   $(chat_dialog).find('.txt-chat').first().focus();

}



function fetchMessages(chat_dialog, chatId, roomName)
{



   sockets[roomName].send(JSON.stringify({'command':'fetch_messages',  'chatId':chatId}));
}
