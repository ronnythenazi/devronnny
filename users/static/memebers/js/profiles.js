function create_profile_link(username, prefix_user = '@')
{
  var link = '<span class="tagged-user"';
  //var style = get_tagged_user_style();
  //link = link + style + ' ';

  link  = link + '>';

  link = link + prefix_user + username;
  link = link + '</span>';
  return link;
}

function get_tagged_user_style()
{
  style = 'style="font-weight:bolder;text-decoration:none;color:blue;"';
  return style;
}
function remove_profile_link_from_cke(username, ck_name)
{
  var s_to_remove = create_profile_link(username, prefix_user = '');
  replace_html_in_ckeditor(s_to_remove, username, ck_name);
}

function tag_caret_with_selected_txt()
{
   var e  = $(this);
   var prefix = '@';
   replace_caret_with_selected_txt(e, prefix);
}

function show_user_lst_popup(users_dict_lst, elem, left, top)
{
   for(var i=0;i<users_dict_lst.length;i++)
   {
     var user_info = users_dict_lst[i];
     var row = create_user_lst_row_item(user_info);
     $(elem).append(row);
     var new_elem_cname = get_popup_row_item_className();
     $('.' + new_elem_cname + ':last-child').on('click', tag_caret_with_selected_txt);
   }
   $(elem).css('top', top + 'px');
   var elem_width = $(elem).width();
   left = left - elem_width - 20;
   $(elem).css('left', left + 'px');
   var bg_child = create_lighten_row_elem();
   $(elem).children().first().append(bg_child);
   $(elem).show();

}

/*function remove_user_lst_popup(elem)
{
  clear_user_lst_popup(elem);
  $(elem).hide();
}

function clear_user_lst_popup(elem)
{
  $(elem).children('.popup-msg-list-row-item').remove();
}*/


function create_user_lst_row_item(user_info)
{
  var row = '<div class="' + get_popup_row_item_className() + '">';
  var username = '<span>'+ user_info['username'] + '</span>';
  var avatar = user_info['avatar'];
  var src = ' src="' + avatar +'" ';
  var img_selector_name = get_avatar_item_selector_name();
  var cls= ' class="'+ img_selector_name  +'" ';
  var img_serial_number = $('.' + img_selector_name).length + 1;
  var img_id_name = img_selector_name + img_serial_number;
  var id = ' id="' + img_id_name + '" ';
  var onload = ' onload="fadeInImg('+ "'" + img_id_name + "'" +')" ';
  var img = '<img' + cls + id  + src  + onload + '/>';
  row = row + username + img + '</div>';
  return row;
}

function get_tagged_users_suggestion_lst_selector()
{
  return "#" + get_tagged_users_suggestion_lst_id_name();
}

function get_tagged_users_suggestion_lst_id_name()
{
  return 'tagged-users-suggestion-lst';
}
