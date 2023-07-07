


$('.shrink-win-to-left-svg-23').click(function(){

    $('#press_audio')[0].play();
    hide_win_active_visitors();
});



   // Animation complete.



$('.expand-win-to-right-svg-23').click(function(){

     $('#press_audio')[0].play();
     expand_win_active_visitors();
});

function refresh_active_users(items, win_view = 'site')
{

  if(items.length == 0)
  {
    $('.active_visitor_parent').hide();
    return;
  }

  $('.active_visitor_parent').css('display', 'flex');
  clear_before_refresh_active_users();
  for(var i=0;i<items.length;i++)
  {
    var item = items[i];
    var last_time_active = item['last_time_active'];
    var user_id          = item['user_id'];
    var name             = item['name'];
    var avatar           = item['avatar'];
    var ip_address       = item['ip_address'];

    clone_active_visitors_lst_item(last_time_active, user_id, name, avatar, ip_address, win_view);
  }



  expand_win_active_visitors();
  $('#update_audio')[0].play();
  window.setTimeout(function(){
    $('#hide_audio')[0].play();
    hide_win_active_visitors();}, 10000);


}

function set_footer_visitors(guests ,win_view = 'site')
{
   if(guests.length == 0)
   {
     $('.footer-active-visitors').hide();
     return;
   }

   var suffix = "";
   if(win_view == 'site')
   {
     suffix = "באתר";
   }
   else
   {

      suffix = "בעמוד";

   }
   var txt = guests.length + ' ' +  'אורחים' + ' ' + suffix;
   $('.footer-active-visitors>span').text(txt);
   $('.footer-active-visitors').css('display', 'flex');

}
function expand_win_active_visitors()
{
  $(".active_visitor_parent").animate({width: 250}, duration = 1000, complete = function() {

    $('.expand-win-to-right-svg-23').css('display', 'none');
    $('.shrink-win-to-left-svg-23').show();

  });

  $('.active_visitors_parent_holder').animate({left:0},1000);
}

function hide_win_active_visitors()
{
  $(".active_visitor_parent").animate({width: 0},duration = 1000, complete = function() {

    $('.shrink-win-to-left-svg-23').css('display', 'none');
    $('.expand-win-to-right-svg-23').show();
  });
  $('.active_visitors_parent_holder').animate({left:0},1000);
}

function clone_active_visitors_lst_item(last_time_active, user_id, name, avatar, ip_address, win_view)
{


  var elem_to_clone = $('.templeate_visitor_item').first();

  var num_of_items = $('.active_visitor_item').length + 1;
  var active_visitor_img_id = "active_visitor_img_" + num_of_items;
  var last_seen_msg = get_last_seen_msg(last_time_active);
  var cloned = $(elem_to_clone).clone(true);
  $(cloned).removeClass('templeate_visitor_item');
  $(cloned).css('display', 'flex');
  $(cloned).find('.img_active_user').attr('src', avatar);
  $(cloned).find('.img_active_user').attr('onload', "fadeInImg('"+ active_visitor_img_id +"')");
  $(cloned).find('.img_active_user').attr('id', active_visitor_img_id);
  $(cloned).find('.active_user_item_name').text(name);
  $(cloned).find('.active_visitor_item_last_seen').text(last_seen_msg);
  $(cloned).find('.hidden_user_id_for_active_user').data('user_id',user_id);
  if(win_view == 'page')
  {

    $('.header_active_visitor_parent>span').text('נמצאים בעמוד');

  }
  else
  {
    $('.header_active_visitor_parent>span').text('פעילים לאחרונה באתר');
  }

  $('.active_visitor_item').last().after(cloned);
}

function clear_before_refresh_active_users()
{
   $('.active_visitor_item:not(.templeate_visitor_item)').each(function(){
     $(this).remove();
   });
}

function get_last_seen_msg(last_time_active)
{
  var last_seen_msg = "";
  if(last_time_active == '1')
  {
    last_seen_msg =  "לפני דקה";
  }
  else if(last_time_active == '0')
  {
    last_seen_msg =  "עכשיו";
  }
  else
  {
    last_seen_msg =  "לפני" + " " + last_time_active + " " + "דקות";
  }
  return last_seen_msg;
}
