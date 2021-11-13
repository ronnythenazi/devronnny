var popupselector = '.popupmenu';
// var popup; //new
var duration = 0;

function handleclick(e)
{
   var popup = $(e).siblings('.popupmenu');
   var curritemWarpper = $(e).parent('.menuitemwarpper');
  // curritemWarpper.on("mouseleave", leaved); // new
   var currmenuitemidname = $(e).attr('id');
  // var popupheight = $(e).attr('data-value'); //new
   if($(popup).css('visibility') == 'hidden')
   {
    //  hideveryonexceptcurrent(e); new
    //  $(popup).css('height', '0');//new
      $(popup).css('visibility', 'visible');
      $(popup).find('*').css('visibility', 'visible');
      $(popup).siblings('.upperpointer').css('visibility', 'visible');
      $(popup).children('.menuitemtitlewarrper').css('opacity', '1');
    //  $(popup).animate({height:popupheight}, duration);// new
      $(e).children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '100%');
  }
  else {

   $(popup).css('visibility', 'hidden'); //new
   $(popup).find('*').css('visibility', 'hidden'); //new
   $(popup).siblings('.upperpointer').css('visibility', 'hidden'); //new
   $(popup).children('.menuitemtitlewarrper').css('opacity', '0') //new

   $(e).children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '0%');
 }
}


 $(document).mousemove(function(e){
$('.popupmenu').each(function(){
  if($(this).css('visibility') == 'hidden')
  {
    return true;
  }


 var popup = $(this);
  var topY = $(popup).siblings('.menuitem').parent('.menuitemwarpper').offset().top;//new
  var leftX = $(popup).siblings('.menuitem').parent('.menuitemwarpper').offset().left;//new

   if(topY <0 || leftX <0)
   {
     return;
   }



var height = $(popup).outerHeight() + $(popup).siblings('.menuitem').parent('.menuitemwarpper').outerHeight(); //new
var width  = $(popup).siblings('.menuitem').parent('.menuitemwarpper').outerWidth(); //new

var tooFar = 0;

/*if($('#sub-level2').length)
{
  return;
}*/
var condition = false;

if(!($('#sub-level2').length))
{
  if(e.pageY - (topY + height)>=tooFar  || topY - e.pageY >= tooFar|| leftX - e.pageX >= tooFar  || e.pageX - (leftX + width) >= tooFar)
  {
    condition = true;
  }
}
else
{
  var subpopY =  $('#sub-level2').offset().top;
  var subpopX =  $('#sub-level2').offset().left;
  //var subpopW =  $('#sub-level2').outerWidth();
  var subpopH =  $('#sub-level2').outerHeight();
  if(e.pageX - (leftX + width) >= tooFar || subpopX - e.pageX >= tooFar || topY - e.pageY >= tooFar || e.pageY - Math.max(subpopH + subpopY, (topY + height))>=tooFar)
  {
    condition = true;
  }
}

 if(condition)
 {

  $('#sub-level2').remove();
  $(popup).siblings('.upperpointer').css('visibility', 'hidden');
  $(popup).children('.menuitemtitlewarrper').css('opacity' , '0');

   $(popup).css('visibility', 'hidden');
    $(popup).find('*').css('visibility', 'hidden');


   $(popup).siblings('.menuitem').children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '0%');

  }
});
});
