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

$('.hide-popup-item').click(function(){
  var id    = get_com_id($(this));
  var comType  = getComTypeV2($(this));
  hideComAjax(id, comType, function(result){
   var com = getComObj(comType, id);
   $(com).hide();
  });

});

function getComObj(comType, id)
{
  if(comType == 'com')
  {
    return $('#comment' + id);
  }
  return $('#sub-comment' + id)
}

$('.deactivate-popup-item').click(function(){
   var com_ancestor = $(this).parents('.item').first();
   var user = get_com_author(com_ancestor);
   deactivate_user(user);
   $(com_ancestor).find('.deactivate-popup-item').first().hide();
   $(com_ancestor).find('.activate-popup-item').first().show();
});

$('.activate-popup-item').click(function(){
   var com_ancestor = $(this).parents('.item').first();
   var user = get_com_author(com_ancestor);
   activate_user(user);
   $(com_ancestor).find('.activate-popup-item').first().hide();
   $(com_ancestor).find('.deactivate-popup-item').first().show();
});

function get_com_author(com)
{
   var com_type = com_or_subcom(com);
   var username = '';
   if(com_type == 'com')
   {
       username = $(com).find('.com-author').first().val();
   }
   if(com_type == 'sub_com')
   {
     username = $(com).find('.sub-com-author').first().val();
   }
   return username;

}

function com_or_subcom(com)
{
   var com_type = '';
   if($(com).hasClass('comment'))
   {
     com_type = 'com';
   }
   else if($(com).hasClass('subitem'))
   {
     com_type = 'sub_com';
   }
   return com_type;
}

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

function getComTypeV2(e)
{
  var ancestor = $(e).parents('.organ').first().parents('.item').first();
  var id = $(ancestor).attr('id');
  if(id.indexOf('sub-comment')>=0)
  {
    return 'subcom';
  }
  return 'com';
}

function get_com_type(e)
{
  var ancestor = $(e).parents('.organ').first().parents('.item').first();
  var id = $(ancestor).attr('id');
  if(id.indexOf('sub-comment')>=0)
  {
    return 'sub_com';
  }
  return 'com';
}
function get_com_id(e)
{
  var ancestor = $(e).parents('.organ').first().parents('.item').first();
  var id = $(ancestor).attr('id');
  if(id.indexOf('sub-comment')>=0)
  {
    id = id.replace('sub-comment','');
    return id;
  }
  id = id.replace('comment','');
  return id;
}
$('.follow-popup-item').click(function(){

  //id of com or sub_com
  var id = get_com_id($(this));
  // com or sub_com
  var type = get_com_type($(this));

  //now unfollow option is visible and fllow is hidden
  $(this).siblings('.unfollow-popup-item').show();
  $(this).hide();

  //function inside article.html page, call ajax
  f_follow(type, id, flag = 'follow');
});

$('.unfollow-popup-item').click(function(){

  //id of com or sub_com
  var id = get_com_id($(this));
  // com or sub_com
  var type = get_com_type($(this));

  //now follow option is visible and unfllow is hidden
  $(this).siblings('.follow-popup-item').show();
  $(this).hide();

  //function inside article.html page, call ajax
  f_follow(type, id, flag = 'unfollow');
});

function hide_confirm_popup()
{
  $('#confirmation-box').hide();
  $(this).remove();
}

function hide_popup_msg()
{
  $('#popup-msg').hide();
  $(this).remove();
}





function set_popup_msg(title, body, ok_btn)
{
  $('#popup-msg .popup-msg-title').text(title);
  $('#popup-msg .popup-msg-body').text(body);
  $('#popup-msg #popup-msg-cancel').text(ok_btn);
}

$('.not-log-in').click(function(){
  title = "אינך מחובר";
  body = "רק משתמשים רשומים ומחוברים יכולים להגיב";
  ok_btn = "הבנתי";
  set_popup_msg(title, body, ok_btn);
  $('#popup-msg').fadeIn("slow");
  $('body').append('<div id="darken-screen"></div>');
  $('#darken-screen').on('click', hide_popup_msg);
});

$('body>*:not(#popup-msg, #popup-msg *)').click(function(){
  var hidden_status = $('#popup-msg').css('display');
  if(hidden_status == none || String(hidden_status) == 'none')
  {
    return;
  }

});

$('#popup-msg-cancel').click(function(){
  $('#popup-msg').hide();
  $('#darken-screen').remove();
});
