
/*$(document).ready(start);

function start()
{
  wrape_chrs($('.horzmove'));
  movehorz($('.horzmove:not(.reverse)'));
  movehorz($('.horzmove.reverse'), dir = -1);
}*/
 $('.subject *').hover(function(){
  let ancestor = $(this).parents('.subject');
  $(ancestor).siblings().addClass('greyblur');
  $(ancestor).removeClass('greyblur');
});

$('.subject').mouseleave(function(){
  $(this).siblings().removeClass('greyblur');
});

$('.sub_subject_box>*').hover(function(){
  $('.sub_subject_box').children().addClass('hueimg');
  $('.sub_subject_box').children().removeClass('defaultimg');
  $(this).removeClass('hueimg');
  $(this).addClass('defaultimg');
  $(this).siblings().removeClass('hueimg');
  $(this).siblings().addClass('defaultimg');
  $(this).addClass('focus');
  $(this).siblings().addClass('focus');
});



$('.sub_subject_box').hover(function(){
  $('.sub_subject_box').children().addClass('hueimg');
  $('.sub_subject_box').children().removeClass('defaultimg');
  $(this).children().removeClass('hueimg');
  $(this).children().addClass('defaultimg');
});
$('.sub_subject_box').mouseleave(function(){
  $('.sub_subject_box').children().removeClass('hueimg');
  $('.sub_subject_box').children().addClass('defaultimg');
  $(this).children().removeClass('focus');
  /*$(this).children().removeClass('hueimg');
  $(this).children().addClass('defaultimg');*/
});

function movehorz(elem_to_move, dir = 1, index = 0, tmax=10000, toffsetunit=100)
{

    var offset = index * toffsetunit;
    var slidewidth = getElemWidth(elem_to_move);
      $(elem_to_move + ":not(.stick)").children('span').animate(
      {right:(dir*slidewidth)+"px"}
      ,(tmax - offset)
    ).animate({right:((-1)*dir*slidewidth)+"px"},1);

    $(elem_to_move + ".stick").children('span').animate(
    {right:(dir*slidewidth)+"px"}
    ,(tmax - offset)
  ).animate({right:((-1)*dir*slidewidth)+"px"},tmax);

    movehorz(elem_to_move);
}

function getCurrX(elem)
{
  var str = $(elem).css('right');
  var currX = parseInt(str.replace("px", ""));
  return currX;
}
function getElemParentWidth(elem)
{
  return parseInt($(elem).parent().css('width').replace("px",""));
}
function getElemWidth(elem)
{
  return parseInt($(elem).css('width').replace("px",""));
}
