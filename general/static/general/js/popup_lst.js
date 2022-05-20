function create_lighten_row_elem()
{
  var highlight_row_cn = get_lighten_row_className();
  return '<div class="' + highlight_row_cn + '"></div>';
}

function get_popup_row_item_className()
{
  return 'popup-msg-list-row-item';
}

function is_popup_lst_shown()
{
   var lst_ancestor_selector = get_lst_ancestor_selector_generic_selector();
   return is_elem_displayed(lst_ancestor_selector);

}

//$(get_popup_row_item_selector()).click(replace_caret_with_selected_word);


function replace_caret_with_selected_txt(e, prefix = '')
{
  //select_row($(this));

  var txt = select_and_get_txt_in_new_selected_item(e);
  var ck_name = $('#activated_editor').val();
  var editor = CKEDITOR.instances[ck_name];
  replace_word_at_caret(editor, prefix + txt);


}

function select_and_get_txt_in_new_selected_item(e)
{
  select_row($(e));
  //var lst_ancestor_selector = get_lst_ancestor_selector_generic_selector();
//var bg_child_selector = get_lighten_row_selector();
  var txt = get_txt_of_selected_row();
  return txt;

  /*select_row($(this));
  var lst_ancestor_selector = get_lst_ancestor_selector_generic_selector();
  var bg_child_selector = get_lighten_row_selector();
  var txt = select_row_item_and_get_txt();

  var ck_name = $('#activated_editor').val();
  var editor = CKEDITOR.instances[ck_name];
  replace_word_at_caret(editor, txt);*/
}

$(get_popup_row_item_selector()).dblclick(function(){

  //select_row($(this));

});


function select_row(new_highlight_elem)
{
  var lst_ancestor_selector = get_lst_ancestor_selector_generic_selector();
  var lst_parent = $(new_highlight_elem).parents(lst_ancestor_selector).first();
  var ligthen_row_selector = get_lighten_row_selector();
  var row_item_selector = get_popup_row_item_selector();

  var prev_highlight_elem = $(lst_parent).find(ligthen_row_selector).parent(row_item_selector);

  rehighlight_list_item(prev_highlight_elem, new_highlight_elem);
}

function get_lst_ancestor_selector_generic_selector()
{
  var selector = '.' + get_lst_ancestor_selector_generic_name();
  return selector;

   //in case you will have multiple elems
   //with this same className
   //you would like to modify this function
   //so it will return only the elems
   //that have display property other than none
   //in that case, you can filter it more
   //before returning the selector val
   //something similar like this line of code below

   //return $(selector).prop('display', 'flex');

}

function get_lst_ancestor_selector_generic_name()
{
  return 'popup-msg-list-to-select';
}

function get_popup_row_item_selector()
{
   return '.' + get_popup_row_item_className();
}

function get_lighten_row_selector()
{
  return '.' + get_lighten_row_className();
}

function get_lighten_row_className()
{
  return 'highlight-row';
}
function remove_lst_popup(elem)
{
  clear_lst_popup(elem);
  $(elem).hide();
}

function clear_lst_popup(elem)
{
  var item_selector = '.' + get_popup_row_item_className()
  $(elem).children(item_selector).remove();
}

//select_row_item_and_get_txt
function get_txt_of_selected_row(txt_node_selector = 'span')
{
   var lst_selector = get_lst_ancestor_selector_generic_selector();
   var txt = get_selected_row_txt(txt_node_selector);
   var elem = $(lst_selector);
   remove_lst_popup(elem);
   return txt;
}

function get_selected_row_txt(txt_node_selector = 'span')
{
  var lst_selector = get_lst_ancestor_selector_generic_selector();
  var  bg_child_selector = get_lighten_row_selector();

  var curr_highlight_elem  = $(lst_selector + ' ' + bg_child_selector).parent();
  var txt_node = $(curr_highlight_elem).find(txt_node_selector);
  var txt = $(txt_node).text();
  return txt;
}

function move_bg_arrow_pressed(ks)
{
  var lst_selector = get_lst_ancestor_selector_generic_selector();
  var  bg_child_selector = get_lighten_row_selector();
  var row_selector = get_popup_row_item_selector();

  var items_selector =  lst_selector + ' ' + row_selector;
  // check if there are items in list
  if(is_elem_exists(items_selector) == false)
  {
    // no items in list
    return;
  }
  var curr_highlight_elem  = $(lst_selector + ' ' + bg_child_selector).parent();
  //move down
  if(ks == 40)
  {
     move_bg_down(curr_highlight_elem);
     return;
  }
  //move up
  if(ks == 38)
  {
    move_bg_up(curr_highlight_elem);
    return;
  }
}


function move_bg_down(curr_highlight_elem)
{

  var  bg_child_selector = get_lighten_row_selector();
  var next_item_in_list = $(curr_highlight_elem).next();
  if(is_elem_exists(next_item_in_list) == false)
  {
    // no items in list
    return;
  }
   rehighlight_list_item(curr_highlight_elem, next_item_in_list);
}


function move_bg_up(curr_highlight_elem)
{
  var  bg_child_selector = get_lighten_row_selector();
  var prev_item_in_list = $(curr_highlight_elem).prev();
  if(is_elem_exists(prev_item_in_list) == false)
  {
    // no items in list
    return;
  }
   rehighlight_list_item(curr_highlight_elem, prev_item_in_list);
}


function rehighlight_list_item(curr_highlight_elem, new_row_elem)
{
    var  bg_child_selector = get_lighten_row_selector();
    $(curr_highlight_elem).children(bg_child_selector).remove();
    $(new_row_elem).append(create_lighten_row_elem());
}

function get_avatar_item_selector_name()
{
  return 'avatar-item-in-popup-lst';
}
