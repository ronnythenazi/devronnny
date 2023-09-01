


function set_draggable(elem)
{

  $(elem)
  .mousedown(function() {
      $(this).attr('isDragging', 'false');
  })
  .mousemove(function() {
      $(this).attr('isDragging', 'true');
   })
  .mouseup(function() {
      var wasDragging = $(this).attr('isDragging');
      $(this).attr('isDragging', 'false');
      if (!wasDragging) {
          show_popup_at_cursor_23(elem);
      }
  });
}
