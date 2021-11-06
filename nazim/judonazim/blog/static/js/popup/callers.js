$(document).ready(function(){
  $('.menuitem').each(function(){
    $(this).attr('value', $(this).siblings('.popupmenu').css('height'));
    $(this).data('topY', -1);
    $(this).data('leftX',-1);
});
});

$('#btnnazimbgmenuitem').mouseover(function (){
  if($(this).siblings('.popupmenu').css('visibility') == 'hidden')
  {
    handleclick($(this));
    addimages($(this).attr('id'));
  }

});

$('#btnronny').mouseover(function (){
  if($(this).siblings('.popupmenu').css('visibility') == 'hidden')
  {
  handleclick($(this));
  addimages($(this).attr('id'));
  }
});
