function hide_elem_if_close_to_bottom(elem, bottom, display='flex', extra_space=0)
{
  var scrollHeight = $(document).height();
  var scrollPosition = $(window).height() + $(window).scrollTop();

  //var elem_height = $(elem).height();
  ///  if (scrollHeight - scrollPosition < bottom + extra_space + elem_height)
  if (scrollHeight - scrollPosition < bottom + extra_space)
  {
    $(elem).hide();
  }
  else
  {
     $(elem).css('display', display)
  }
}
