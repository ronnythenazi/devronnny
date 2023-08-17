$('#open-chat-with-user').click(function(){
  if(!$('#hid_username_log_in').length)
  {
    ok_not_log_in_chat();
    return;
  }

  var from_username = $('#hid_username_log_in').val();

  var to_username = $('#hid_username').val();


  var chatId = $('#hid_personal_chat_id').val();
  var roomName = $('#hid_personal_room_name').val();

  if(chatId == 'none')
  {
     var dict = open_personal_chat(from_username, to_username);
     chatId = dict['chatId'];
     roomName = dict['roomName'];

     $('#hid_personal_chat_id').val(chatId);
     $('#hid_personal_room_name').val(roomName);
     return;
  }
  open_chat(from_username, chatId, roomName);


});
