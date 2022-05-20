
$('input[type=file]').change(showPreview);

function showPreview(event){
if(event.target.files.length > 0){
  var src = URL.createObjectURL(event.target.files[0]);
  var preview = $(this).parents('.thumbnail').first().next('.thumb-holder').find('.preview').first();
  $(preview).attr('src', src);
  $(this).parents('.thumbnail').first().next('.thumb-holder').show();
 }
}
// code for preiview upload image
$('.trigger-upload').click(function(){$(this).parent().find('input[type=file]').trigger('click');});



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
