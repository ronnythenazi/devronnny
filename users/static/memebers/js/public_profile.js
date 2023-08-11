$('#open-chat-with-user').click(function(){
  if(!$('#hid_username_log_in').length)
  {
    ok_not_log_in_chat();
    return;
  }

  var from_username = $('#hid_username_log_in').val();

  var to_username = $('#hid_username').val();

  clone_and_open_private_chat(from_username, to_username);


});
