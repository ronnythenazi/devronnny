$('.arrow-up').click(function(){

  $('body, html').animate({scrollTop:0}, 1000);
  });
$('.rotate-arrow-up').click(function(){
  var drop_down_arrow = $(this).find('.bi-chevron-down');
  if($(drop_down_arrow).hasClass('rotate-up'))
  {
    $(drop_down_arrow).removeClass('rotate-up');
  }
  else
  {

    $(drop_down_arrow).addClass('rotate-up');
  }
});

$('.rotate-arrow-up').mouseleave(function(){
  var drop_down_arrow = $(this).find('svg');
  $(drop_down_arrow).removeClass('rotate-up');

});

$(document).ready(function(){
  $('.btn-loader').append('<div class="loader"></div>');
});

$('form').submit(function(){
  var btn_loader = $(this).find('.btn-loader');
  $(btn_loader).css('font-size', '0');
  $(btn_loader).children('.loader').show();
});
