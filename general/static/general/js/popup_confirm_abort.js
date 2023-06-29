


function show_confirm_popup_23(fname1, fname2, params1, params2)
{
  var popup = $('.confirmation-box-2023').first();

  var dialog_abort_hid = $(popup).find('.digalog-response-abort').first();
  $(dialog_abort_hid).find('.fname').val(fname1);
  $(dialog_abort_hid).find('.params').val(params1);
  var dialog_ok_hid = $(popup).find('.digalog-response-ok').first();
  $(dialog_ok_hid).find('.fname').val(fname2);
  $(dialog_ok_hid).find('.params').val(params2);

  $(popup).css('display', 'flex');

  $('body').append('<div id="darken-screen"></div>');
  $('#darken-screen').on('click', hide_popup_confirm_23);
}

$('.confirm-delete-2023').click(function(){
  call_function_based_on_answer(1);
  hide_popup_confirm_23();
});

function hide_popup_confirm_23()
{
  $('#darken-screen').remove();
  $('.confirmation-box-2023').hide();

}


$('.confirm-cancel-2023').click(function(){
    call_function_based_on_answer(-1);
    hide_popup_confirm_23();
});

function call_function_based_on_answer(answer)
{
   var data;
   var fname;
   if(answer == -1)
   {
     data = extract_stored_hidden_data('.digalog-response-abort');
   }
   else if(answer == 1)
   {
     data = extract_stored_hidden_data('.digalog-response-ok');
   }
   else
   {

   }
   var fname = data[0];


  window[fname](data[1]);



}

function extract_stored_hidden_data(dialog_selector)
{

  var popup = $('.confirmation-box-2023').first();

  var dialog_hid = $(popup).find(dialog_selector).first();
  var fname = $(dialog_hid).find('.fname').val();
  var params = $(dialog_hid).find('.params').val();
  var data = [fname, params];
  return data;
}





$('body>*:not(.confirmation-box-2023, .confirmation-box-2023 *)').click(
  function(){
  var hidden_status = $('.confirmation-box-2023').first().css('display');
  if(hidden_status == none || String(hidden_status) == 'none')
  {
    call_function_based_on_answer(-1);
    return;
  }

});
