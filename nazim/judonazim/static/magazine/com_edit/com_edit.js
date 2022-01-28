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
$('.edit-popup-item').click(function(){

   var com_ancestor = $(this).parents('.item').first();
   var btn_edit = $(com_ancestor).find('.btn-edit').first();
   $(btn_edit).parents('.comment-edit-parent').first().find('.display-view').hide();
   $(btn_edit).parents('.comment-edit-parent').first().find('.form-view').show();
});

$('.btn-edit-save').click(function(){
  var com_ancestor = $(this).parents('.item').first();
  var id = '';
  var com_type = '';
  if($(com_ancestor).hasClass('comment'))
  {
    id = $(com_ancestor).attr('id').replace('comment', '');
    com_type = 'com';
  }
  else if($(com_ancestor).hasClass('subitem'))
  {
    id = $(com_ancestor).attr('id').replace('sub-comment', '');
    com_type = 'sub_com';
  }
  var ck_edit_ancestor = $(com_ancestor).find('.form-view').first();
  var ck_name = $(ck_edit_ancestor).find('.ckeditor').first().attr('name');
  var body = CKEDITOR.instances[ck_name].getData();
  f_ajax_update_com(com_type, id, body);
  var com = $(com_ancestor).find('.display-view').first().find('.com-to-display');
  $(com).html(body);
  $(this).parents('.comment-edit-parent').first().find('.display-view').show();
  $(this).parents('.comment-edit-parent').first().find('.form-view').hide();
});

//com-ctl-popup
$('.com-edit-popup-item').click(function(){
  $(this).parents('.com-edit-popup').first().find('.com-ctl-popup').css('visibility', 'hidden');
});

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
