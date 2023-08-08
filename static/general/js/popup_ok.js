function ok_not_log_in_chat()
{
  body = "התחבר כמשתמש רשום כדי שהשיחות צאט יהיו זמינות עבורך";
  ok_msg_show(body);
}

function ok_msg_show(body)
{
  title = "אינך מחובר";
  //
  ok_btn = "הבנתי";
  set_ok_popup_msg(title, body, ok_btn);

}

function set_ok_popup_msg(title, body, ok_btn)
{
  $('#popup-ok-msg .popup-msg-title').text(title);
  $('#popup-ok-msg .popup-msg-body').first().text(body);
  $('#popup-ok-msg #popup-ok-msg-cancel').text(ok_btn);

  $('#popup-ok-msg').fadeIn("slow");
  $('body').append('<div id="darken-screen"></div>');
  $('#darken-screen').on('click', hide_popup_ok);
}

function hide_popup_ok()
{
  $('#popup-ok-msg').hide();
  $(this).remove();
}

$('body>*:not(#popup-ok-msg, #popup-ok-msg *)').click(function(){
  var hidden_status = $('#popup-ok-msg').css('display');
  if(hidden_status == none || String(hidden_status) == 'none')
  {
    return;
  }

});


$('#popup-ok-msg-cancel').click(function(){
  $('#popup-ok-msg').hide();
  $('#darken-screen').remove();
});
