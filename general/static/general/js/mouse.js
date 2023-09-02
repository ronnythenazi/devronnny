
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

function draggable(elem)
{

  $(elem).draggable(
    {
     containment: '#page-inner',
     scroll:'true',
     snap:true,
     snapMode:'outer',
     stack   :'true',
     cursorAt: { left: -25 },
     disabled: false,

     start: function( event, ui ) {
         $(this).addClass('dragging');
     },
     stop: function( event, ui ) {
         $(this).removeClass('dragging');
     },

    });




}

function set_undraggable(elem)
{

  $(elem).draggable('disable');

}
function set_draggable(elem)
{
  $(elem).draggable('enable');
}
