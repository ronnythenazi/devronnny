
$('.popupmenu>ul>li').mouseenter(function(){$('#sub-level2').remove();});
$('.subpopup').mouseover(function(){showSubMenu($(this));});


//$('#sub-level2').mouseleave(function(){$('#sub-level2').remove();});

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
  var x =  $(subMenuItem).offset().left - $('#sub-level2').outerWidth();
//  var y =  $(subMenuItem).offset().top; new
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

  if(screensize >= 1000)
  {
    return 'defW';
  }
  else if(screensize> 500 && screensize<1000)
  {
    return 'smallW';
  }
  else
  {
    return 'verysmallW';
  }
}
