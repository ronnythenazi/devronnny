$('.popup-3-dots').click(function(){
  var ancestor = $(this).parents('.organ').first().parents('.item').first();
  var id = $(ancestor).attr('id');
  if(id.indexOf('sub-comment')>=0)
  {
    $('#caller-type').val('sub_com');
    $('#caller-id').val(id.replace('sub-comment',''));
  }
  else
  {
    $('#caller-type').val('com');
    $('#caller-id').val(id.replace('comment',''));
  }
  $(this).css('outline-width', '1px');
  var bg_child = $(this).children('.popup-3-dots-after');
  $(this).parent().find('.com-ctl-popup').first().css('visibility', 'visible');
  $(this).css('outline-width', '0');
  $(bg_child).animate({opacity:0.3}, 100).animate({opacity:0}, 300);

});
$('.comment.item *:not(.comment-of-comment, .comment-of-comment *)').mouseover(function(){
  $(this).parents('.item').first().find('.organ').first().find('.com-edit-popup').first().css('display', 'flex');
  $(this).parents('.item').first().find('.organ').first().find('.popup-3-dots').first().css('display', 'flex');
});
$('.comment.item').mouseleave(function(){
  $(this).find('.organ').first().find('.popup-3-dots').first().hide();
  $(this).find('.organ').first().find('.com-edit-popup').first().hide();
  $(this).find('.organ').first().find('.com-ctl-popup').first().css('visibility', 'hidden');
});
$('.item.subitem').mouseover(function(){
  $(this).find('.organ').first().find('.com-edit-popup').first().css('display', 'flex');
  $(this).find('.organ').first().find('.popup-3-dots').first().css('display', 'flex');
  $(this).parents('.comment.item').first().find('.organ').first().find('.popup-3-dots').first().hide();
  $(this).parents('.comment.item').first().find('.organ').first().find('.com-edit-popup').first().hide();
  $(this).parents('.comment.item').first().find('.organ').first().find('.com-ctl-popup').first().css('visibility', 'hidden');
});
$('.item.subitem').mouseleave(function(){
  $(this).find('.organ').first().find('.popup-3-dots').first().hide();
  $(this).find('.organ').first().find('.com-edit-popup').first().hide();
  $(this).find('.organ').first().find('.com-ctl-popup').first().css('visibility', 'hidden');
});
/*$('.organ').mouseover(function(){
  $(this).find('.com-edit-popup').first().css('display', 'flex');
  $(this).find('.popup-3-dots').first().css('display', 'flex');
});*/
/*$('.organ').mouseleave(function(){
  $(this).find('.popup-3-dots').first().hide();
  $(this).find('.com-edit-popup').first().hide();
  $(this).find('.com-ctl-popup').first().css('visibility', 'hidden');
});*/

$('.delete-popup-item').click(function(){
  $('#confirmation-box').fadeIn("slow");
  $('body').append('<div id="darken-screen"></div>');
  $('#darken-screen').on('click', hide_confirm_popup);
});
$('body>*:not(#confirmation-box, #confirmation-box *)').click(function(){
  var hidden_status = $('#confirmation-box').css('display');
  if(hidden_status == none || String(hidden_status) == 'none')
  {
    return;
  }

});
$('#confirm-cancel').click(function(){
  $('#confirmation-box').hide();
  $('#darken-screen').remove();
});
$('#confirm-delete').click(function(){
  $('#confirmation-box').hide();
  $('#darken-screen').remove();
  var caller_type = $('#caller-type').val();
  var id = $('#caller-id').val();
  f_com_delete(caller_type, id);
});
function hide_confirm_popup()
{
  $('#confirmation-box').hide();
  $(this).remove();
}
