
// 06-08-2023

$('.order-num, .user-com-label').hover(function(){

  var com_ancestor = $(this).parents('.item').first();
  var user = get_com_author(com_ancestor);
  display_user_snippet(user, $(this));
});


$(document).mousemove(function(e){

  var vis = $('#the_snippet').css('display');
  if(vis == 'none')
  {
    return;
  }


  forget_user_snippet(e);

});
//end 06-08-2023








$('#article-menu-lst').mouseleave(function(){
  $('#article-menu-lst').hide();
});

$('#article-menu-btn').hover(function(){
  $('#article-menu-btn-bg').show();
});
$('#article-menu-btn').mouseleave(function(){
  $('#article-menu-btn-bg').hide();
});
$('#article-menu-btn').click(function(){

  $('#article-menu-lst').css('display', 'flex');
});







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
