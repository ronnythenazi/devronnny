var popupselector = '.popupmenu';
var popup;
var duration = 0;

/*function addimages(menuitemidname){
  var imgparent = $("#"+menuitemidname).siblings('.popupmenu').children('ul').children('li').children('button').children('ul').children('li');
  if($(imgparent).children('.'+menuitemidname)[0])
  {
    return;
  }
  $(imgparent).children('span').before('<img class="'+menuitemidname+'">');
  var titleimg = $("#"+menuitemidname).children('.menuitembutton').children('button').children('img.ico');

   $('.'+menuitemidname).addClass('submenuitemico');
   $('.'+menuitemidname).attr('src', $(titleimg).attr('src'));
}*/




function handleclick(e)
{
   popup = $(e).siblings(popupselector);
   var curritemWarpper = $(e).parent('.menuitemwarpper');
   curritemWarpper.on("mouseleave", leaved);
   var currmenuitemidname = $(e).attr('id');
   var popupheight = $(e).attr('data-value');
   if($(popup).css('visibility') == 'hidden')
   {
      hideveryonexceptcurrent(e);
      $(popup).css('height', '0');
      $(popup).css('visibility', 'visible');
      $(popup).find('*').css('visibility', 'visible');
      $(popup).siblings('.upperpointer').css('opacity', '1');
      $(popup).children('.menuitemtitlewarrper').css('opacity', '1');
      $(popup).animate({height:popupheight}, duration);
      $(e).children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '100%');
  }
  else {


   $(popup).siblings('.upperpointer').animate({opacity:0}, {duration:duration/2, complete:function(){$(popup).children('.menuitemtitlewarrper').animate({opacity:0}, duration/2);}});
   $(popup).animate(
     {height:0},
     {duration:duration,
        complete:function(){
              $(popup).find('*').css('visibility', 'hidden');
              $(popup).css('visibility', 'hidden');
        }
     }
   );

   //$(popup).find('*').animate({height:0}, duration);

   $(e).children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '0%');
 }
}

function hideveryonexceptcurrent(e)
{
   var currId = $(e).attr('id');
   var others = $('#' + currId).parent('.menuitemwarpper').siblings('.menuitemwarpper').children('.popupmenu');
   $(others).siblings('.upperpointer').animate({opacity:0}, {duration:duration/2, complete:function(){$(others).children('.menuitemtitlewarrper').animate({opacity:0}, duration/2);}});
   $(others).animate(
     {height:0},
     {duration:duration,
        complete:function(){
              $(others).css('visibility', 'hidden');
              $(others).find('*').css('visibility', 'hidden');
        }
     }
   );
   $(others).siblings('.menuitem').children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '0%');
}

function leaved(){
    var menuitemwarpper = $(popup).parent();
    var y = $(menuitemwarpper).offset().top;
    var x = $(menuitemwarpper).offset().left;

     $(popup).siblings('.menuitem').attr('data-topY', String(y));
     $(popup).siblings('.menuitem').attr('data-leftX', String(x));
}


 $(document).mousemove(function(e){
   var topY = parseInt($(popup).siblings('.menuitem').attr('data-topY'));
   var leftX = parseInt($(popup).siblings('.menuitem').attr('data-leftX'));



  if(topY <0 || leftX <0)
  {
    return;
  }

  var height = parseInt($(popup).css('height').replace('px', ''));
  var width  = parseInt($(popup).css('width').replace('px', ''));
  var offX = Math.abs(leftX - e.pageX);
  var offY = Math.abs(topY - e.PageY);
  var tooFar = 0;


if(e.pageY - (topY + height)>=tooFar  || topY - e.pageY >= tooFar  || leftX - e.pageX >= tooFar  || e.pageX - (leftX + width) >= tooFar)
{
  $(popup).siblings('.upperpointer').animate({opacity:0}, duration);
  $(popup).children('.menuitemtitlewarrper').animate({opacity:0}, duration);
  $(popup).animate(
    {height:0},
    {duration:duration,
       complete:function(){
             $(popup).css('visibility', 'hidden');
             $(popup).find('*').css('visibility', 'hidden');

       }
    }
  );

  $(popup).siblings('.menuitem').children('.menuitembutton').children('.line180warpper').children('.line180').css('width', '0%');
  $(popup).siblings('.menuitem').attr('data-leftX', '-1');
  $(popup).siblings('.menuitem').attr('data-topY', '-1');
}
});
