
$('#the_snippet').click(redirect_to_public_profile);

$('.snippet-txt-body').hover(function(){
  $(this).find('.snippet-row').css('color', '#f207ee');
});
$('.snippet-txt-body').mouseleave(function(){
   $(this).find('.snippet-row').css('color', '#6babf0');
});

function redirect_to_public_profile()
{
  var profile_id = $(this).find('#hid-snippet-profile-id').first().val();
  redirect_to_public_profile_ajax(profile_id, function(callback){
      window.location = callback['url'];
  });
}

function display_user_snippet(user, show_near_elem)
{
     get_user_snippet_details_ajax(user, function(result){
     fill_user_snippet_html_details(user, result);
     show_popup_at_cursor_23($('#the_snippet'), show_near_elem);
   });

}

function forget_user_snippet(e)
{
  if(is_curs_inside_rect_elem($('#the_snippet'), e) == true)
  {
    return;
  }
  forget_popup_snippet_23($('#the_snippet'));
}

function fill_user_snippet_html_details(user, dict)
{

  get_a_user_online_status_ajax(user, function(result){

    //status online or offline
    if(result['status'] == 'online')
    {
      $('.online-green-rdbtn').show();
      $('.offline-red-rdbtn').hide();
    }

    else if(result['status'] == 'offline')
    {
      $('.online-green-rdbtn').hide();
      $('.offline-red-rdbtn').show();
    }

    else
    {

    }
    //the rest of the details
    fill_user_snippet_the_rest(dict);
  });

}

function fill_user_snippet_the_rest(dict)
{
  $('#snippet-name').html(dict['name']);
  $('#snippet-age').html(dict['age']);
  var sex = "";
  if(dict['sex'] == 'male')
  {
      sex = "גבר";
  }
  else if(dict['sex'] == 'female')
  {
     sex = "אישה";
  }
  else
  {
    sex = "חסר מין";
  }

  $('#snippet-sex').html(sex);
  $('#snippet-img').attr('src', dict['avatar']);
  $('#hid-snippet-profile-id').val(dict['profile_id']);
}
