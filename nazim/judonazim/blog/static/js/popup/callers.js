$(document).ready(function(){
  $('.menuitem').each(function(){
    $(this).attr('data-value', $(this).siblings('.popupmenu').css('height'));
    $(this).attr('data-topY', '-1');
    $(this).attr('data-leftX','-1');
});
$('.menuitemwarpper').on('mouseover click', function (){
  if($(this).children('.menuitem').siblings('.popupmenu').css('visibility') == 'hidden')
  {
    handleclick($(this).children('.menuitem'));
    //addimages($(this).children('.menuitem').attr('id'));
  }

});
});

function setPopupsDataHeight()
{
  var childsHeight;
  $('.menuitem').each(function(){
      childsHeight = 0;
      var this_popup = $(this).siblings('.popupmenu');
      $(this_popup).children().each(function(){
        childsHeight += $(this).height() +
                        parseInt($(this).css('padding-top').replace("px","")) +
                        parseInt($(this).css('padding-bottom').replace("px",""));
      });
      $(this).attr('data-value', childsHeight + "px");
  });
}
