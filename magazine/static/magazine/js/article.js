

$('#btn-follow').click(function(){

  var caller_type = 'post';
  // id of post
  var id = $('#post_pk').val();

  //now unfollow option is visible and fllow is hidden
  $(this).siblings('#btn-unfollow').show();
  $(this).hide();

  //function inside article.html page, call ajax
  f_follow(caller_type, id, flag = 'follow');
});


$('#btn-unfollow').click(function(){

  var caller_type = 'post';
  // id of post
  var id = $('#post_pk').val();

  //now follow option is visible and unfllow is hidden
  $(this).siblings('#btn-follow').show();
  $(this).hide();

  //function inside article.html page, call ajax
  f_follow(caller_type, id, flag = 'unfollow');
});


function mark_banned_users()
{
  $('.user-com-label').each(function(){
    if(is_attr_exist($(this), 'is_active') == false)
    {
      //mean continue the loop
      return true;
    }
    // get the value of attr,
    var is_active = $(this).attr('is_active');
    //if the attr has value false, this mean it is banned user
    if(is_active.toLowerCase() == 'false')
    {
      //mark it as banned by adding class with throughline decoration
      $(this).addClass('banned');
      //$(this).contents().eq(0).wrap('<span class="banned-user-label"/>');
      //$(this).prevUntil('img.super-tiny-avatar, img.very-tiny-avatar').addClass('banned');
    }
  });
}
