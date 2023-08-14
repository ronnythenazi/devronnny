
//not only relveant to chat messages
//but relvant to many other cases when the scorllheight
//is updated to be greater, and you need to
//scroll down a bit to offset the new gap
//the whell position will move down
//depnding on where your current wheel now
//and what is the update in height for the new scorllheight
function scroll_down_the_gap_on_new_msg(dialog, inserted_elem, extra=0)
{
  $(dialog).scrollTop($(dialog).scrollTop() + $(inserted_elem).height() + extra);

}

function scroll_to_bottom_most(dialog)
{
  $(dialog).scrollTop($(dialog).prop("scrollHeight"));
}

function get_wheel_height(elem)
{

  var scrollHeight = $(elem).prop("scrollHeight");
  var clientHeight = $(elem).prop("clientHeight");

  var scrollbarHeight = scrollHeight - clientHeight;

  return scrollbarHeight;

}
function set_txtarea_caret(elem, caret=10)
{
  $(elem).append('<div id="bookmark" style="display:none;">א</div>');
  var node = $('#bookmark');
  node.focus();
  var textNode = node.firstChild;
  var range = document.createRange();
  range.setStart(textNode, caret);
  range.setEnd(textNode, caret);
  var sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  $('#bookmark').html('');
}





function hide_elem_if_close_to_bottom(elem, bottom, display='flex', extra_space=0)
{
  var scrollHeight = $(document).height();
  var scrollPosition = $(window).height() + $(window).scrollTop();

   var elem_height = $(elem).height();
  ///  if (scrollHeight - scrollPosition < bottom + extra_space + elem_height)
  if (scrollHeight - scrollPosition < bottom +  extra_space)
  {
    $(elem).hide();
  }
  else
  {
     $(elem).css('display', display)
  }
}

function is_curs_inside_rect_elem(elem, e, min_dis = 0)
{

   var x_elem = $(elem).offset().left;
   var y_elem = $(elem).offset().top;



   var elem_w = $(elem).width();
   var elem_h = $(elem).height();

   var cur_x = e.pageX;
   var cur_y = e.pageY;


   if(cur_x <= x_elem + elem_w && cur_x >= x_elem && cur_y>= y_elem && cur_y<= y_elem + elem_h)
   {
     return true;
   }

  return false;

}

function show_popup_at_cursor_23(popup, show_near_elem)
{
   var x = $(show_near_elem).offset().left;
   var y = $(show_near_elem).offset().top;

   $(popup).css('left', x);
   $(popup).css('top', y);
   $('body').append(popup);
   $(popup).css('display', 'flex');
   //$(popup).fadeIn('slow');
}

function forget_popup_snippet_23(popup)
{
  //$(popup).remove();
  $(popup).fadeOut('fast');
}
