$('#thumbnail').change(showPreview);

function showPreview(event){
if(event.target.files.length > 0){
  var src = URL.createObjectURL(event.target.files[0]);
  $('#preview').attr('src', src);
  $('.thumb-holder').show();

 }
}

$('.trigger-upload').click(function(){$(this).prev().trigger('click');})


$('.nicetxtbox').keypress(setTxTStyle);
$('.nicetxtbox').mouseleave(unsetTxTStyle);
$('.nicetxtbox').mouseenter(setTxTStyle);
function setTxTStyle()
{
  $(this).css('outline-color', 'blue');
  $(this).css('outline-width', '2px');
  if(!$(this).val().trim())
  {
    unsetTxTStyle()
     return;
  }
  $(this).css('font-size', '2rem');
}
function unsetTxTStyle()
{
  $(this).css('outline-width', '0');
  if(!$(this).val().trim())
  {
     $(this).css('font-size', '4rem');
  }
}
