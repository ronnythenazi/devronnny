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
  setInterval(bell_ring, 7000);
});

$('form').submit(function(){
  var btn_loader = $(this).find('.btn-loader');
  $(btn_loader).css('font-size', '0');
  $(btn_loader).children('.loader').show();
  var bluish_btn = $(this).find('.btn-loader.subscribe').first();
  if(bluish_btn)
  {

    $(bluish_btn).css('background', '#2F9BDD');
    $(bluish_btn).css('box-shadow', 'unset');
    $(bluish_btn).on('mouseover', function(){
      $(this).css('box-shadow', 'unset');
      $(this).css('background-color', '#2F9BDD');
    });
  }

  if($(btn_loader).hasClass('btnSave'))
  {
      $(btn_loader).addClass('thinking');
  }

  if($(btn_loader).hasClass('btnDeleteTrans'))
  {
      $(btn_loader).addClass('thinking');
  }
});

function bell_ring()
{
  $('.red-bell').addClass('red-bell-ring');
  setTimeout(function(){
    $('.red-bell').removeClass('red-bell-ring');
  }, 3000);
  setTimeout(2500);
  $('.red-bell').addClass('red-bell-ring-scale');
  setTimeout(function(){
    $('.red-bell').removeClass('red-bell-ring-scale');
  }, 1000);
}
