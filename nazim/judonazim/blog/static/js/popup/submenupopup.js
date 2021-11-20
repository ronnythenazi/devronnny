
$('.popupmenu>ul>li').mouseenter(function(){$('#sub-level2').remove();});
$('.subpopup').mouseover(function(){showSubMenu($(this));});




function showSubMenu(subMenuItem)
{
  if($('#sub-level2').length)
  {
    return;
  }
  var contentID = $(subMenuItem).attr('id').replace('submenu-','');
  var subcontentplace = $('#' + contentID+'>div>.btnspan');
  var lst = fillsubmenupopup(subcontentplace);
  var fontclass = adjustfont();

 var submenupopup = '<div id="sub-level2" class="submenupopup ' + fontclass + '">'+ lst + '</div>';


  $('.menu').append(submenupopup);
    adjust_left_most(subMenuItem);//very new
  var x =  $(subMenuItem).offset().left - $('#sub-level2').outerWidth();

  var offsetUp = $(subMenuItem).offset().top - $(subMenuItem).parents('.popupmenu').offset().top;//new

  var y = $(subMenuItem).offset().top  - Math.min(offsetUp, 10) + 10;
  $('#sub-level2').offset({top:y, left:x-1});
  $('#sub-level2').on('mouseleave', subleave);
  $('#sub-level2').children('button').on('mouseover', function(){
    $(this).children('.redlineVer').css('height', $(this).height() + 'px');
  });
  $('#sub-level2').children('button').on('mouseleave', function(){
    $(this).children('.redlineVer').css('height', '0');
  });

}

function adjust_left_most(subpopup)
{

  var is_left_most = false;
   if($(subpopup).parents('.menuitemwarpper').index() == $('.menuitemwarpper').last().index())
   {
     is_left_most = true;


   }

  var window_width = $(window).width();
   if(is_left_most && window_width<=1100 && window_width>950)
   {

      $('#sub-level2').css('max-width', '100px');
    //  $('#sub-level2').css('box-sizing', 'border-box');

   }
   else if(is_left_most && window_width<=950 && $(window).width()>750) {
      $('#sub-level2').css('max-width', '50px');
   }
   else if(is_left_most && window_width<750)
   {
     $('#sub-level2').css('max-width', '100px');
   }
   else if(window_width > 1000)
   {
     $('#sub-level2').css('max-width', '400px');
  //   $('#sub-level2').css('max-width', '400px');
   }
   else if(window_width <1000 && window_width>500)
   {
     $('#sub-level2').css('max-width', '200px');
   }

}
function subleave()
{
  $(this).remove();
}

function fillsubmenupopup(subcontentplace)
{
  var lst = "";
  for(i=0;i<subcontentplace.length;i++)
  {
    lst += '<button type="submit" name="submenu-'+ $(subcontentplace[i]).attr('name') + '">';
    lst += '<div class="redlineVer"></div>';
    lst += '<span>'+ $(subcontentplace[i]).text() + '</span>';
    lst += '</button>';
  }
  return lst;

}
function adjustfont()
{


  var screensize = $(window).width();

  if(screensize >= 1400)
  {
    return 'defW';
  }
  else if(screensize <= 1400 && screensize>=1000)
  {
    return 'mediumW';
  }
  else if(screensize>500 && screensize<1000)
  {
    return 'smallW';
  }
  else
  {
    return 'verysmallW';
  }

}
