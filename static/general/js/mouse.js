
function drop_object(e, elem)
{
/*  target.addEventListener("drop", (event) => {
 // prevent default action (open as link for some elements)
  event.preventDefault();
  // move dragged element to the selected drop target
  if (event.target.classList.contains("dropzone")) {
   event.target.classList.remove("dragover");
   event.target.appendChild(dragged);
 }
});*/

}

function set_draggable(elem)
{
  $(elem).draggable(
    {containment: '#page-inner'}
  );

}
