$('.menu-tooltip-lst').mouseleave(function(){
  $(this).hide();
  var parent_category =  $(this).parents('.category-2023').first();
  var menu_tooltip_btn = $(parent_category).find('.menu-tooltip-btn').first();
  $(menu_tooltip_btn).show();
});

$('.menu-tooltip-btn').hover(function(){
  var parent_category =  $(this).parents('.category-2023').first();
  var menu_tooltip_btn_bg = $(parent_category).find('.menu-tooltip-btn-bg').first();
  $(menu_tooltip_btn_bg).show();
});
$('.menu-tooltip-btn').mouseleave(function(){
  var parent_category =  $(this).parents('.category-2023').first();
  var menu_tooltip_btn_bg = $(parent_category).find('.menu-tooltip-btn-bg').first();
  $(menu_tooltip_btn_bg).hide();
});
$('.menu-tooltip-btn').click(function(){
  var parent_category =  $(this).parents('.category-2023').first();
  var menu_tooltip_btn = $(parent_category).find('.menu-tooltip-btn').first();
  var menu_tooltip_lst = $(parent_category).find('.menu-tooltip-lst').first();
  $(menu_tooltip_btn).hide();
  $(menu_tooltip_lst).css('display', 'flex');
});

function abort_deleting_label_23(data)
{
  var params = data.split(',');
  var parent_elem = params; // '#posts-label-23-' + id;
  $(parent_elem).find('.menu-tooltip-lst').hide();
  $(parent_elem).find('.menu-tooltip-btn').show();
}

function confirm_deleting_label_23(data)
{
   var params = data.split(',');
   var label_id = params[0];
   remove_label_ajax(label_id);
   var elemtoremove = params[1];
   $(elemtoremove).remove();
}

$('.remove-item-23').click(function(){

 var abort_fname = "abort_deleting_label_23";
 var ok_fname = "confirm_deleting_label_23";

 var parent_category = $(this).parents('.category-2023').first();
 var id = $(parent_category).find('.label-id-23').first().val();

 params1 = '#posts-label-23-' + id; //parent_elem
 params2 =  id  + ',' + '#posts-label-23-' + id;

  // label id and elemtoremove second
 var val = show_confirm_popup_23(abort_fname, ok_fname, params1, params2);
});

$('.edit-item-2023').click(function(){
  var parent_category = $(this).parents('.category-2023').first();
  var lbl_2023 =  $(parent_category).find('.lbl-2023').first();
  $(lbl_2023).hide();
  var txt_to_edit = $(parent_category).find('.standard-txt-input').first();
  $(txt_to_edit).val($(lbl_2023).text());
  $(txt_to_edit).show();
  $(parent_category).find('.ctl-cancel-edit-2023').css('display', 'flex');
  $(parent_category).find('.menu-tooltip').hide();
});

$('.cancel-lbl-btn-2023').click(function(){

  var parent_category =  $(this).parents('.category-2023').first();
  var txt_input = $(parent_category).find('.standard-txt-input').first();
  $(txt_input).hide();
  $(parent_category).find('.lbl-2023').show();
  $(txt_input).val('');
  $(parent_category).find('.ctl-cancel-edit-2023').first().hide();
  $(parent_category).find('.menu-tooltip').css('display', 'flex');

});
$('.save-lbl-btn-2023').click(function(){

  var parent_category =  $(this).parents('.category-2023').first();
  var txt_input = $(parent_category).find('.standard-txt-input').first();
  $(txt_input).hide();
  $(parent_category).find('.lbl-2023').html($(txt_input).val());
  var id = $(parent_category).find('.label-id-23').first().val();
  update_label_name_ajax(id, $(txt_input).val());
  $(txt_input).val('');
  $(parent_category).find('.lbl-2023').show();
  $(parent_category).find('.ctl-cancel-edit-2023').first().hide();
  $(parent_category).find('.menu-tooltip').css('display', 'flex');
});