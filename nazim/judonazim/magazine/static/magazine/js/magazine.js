$('.menuItem').click(function(){$(this).children('div').css('visibility', 'visible');});
$('.menuItem>div').mouseleave(function(){$(this).css('visibility', 'hidden');});
$('.more-posts-link').mouseover(function(){
  $(this).find('.bi-chevron-double-left').css('fill', 'yellow');
});
$('.more-posts-link').mouseleave(function(){
  $(this).find('.bi-chevron-double-left').css('fill', 'orange');
});
$('.red-hover').mouseover(function(){
  $(this).find('.red-hover').css('fill', 'red');
});
$('.red-hover').mouseleave(function(){
  $(this).find('.red-hover').css('fill', 'blue');
});

$(document).ready(function(){
  setTimeout(function(){$('a').attr('target' , '_blank');}, 100);

});

$('.equal-cols-height-row').mouseenter(function(){
  $('#mouseclick')[0].play();
});

var flicker_round = 1;
$('.svg-rate').click(function(){
    var btn_rate = $(this).parent();
    if(btn_rate)
    {
      var msg = $(btn_rate).nextAll('.msg');
      flicker(msg);
    }

  });
  function flicker(msg)
  {
    $(msg).animate({opacity:1}, 500).animate({opacity:1}, 1000).animate(
      {opacity:0},
      {duration:500,
       complete: function(){
        flicker_round = (flicker_round + 1) % 3;
        if(flicker_round == 0)
        {
           $(msg).css('opacity', 0);
           flicker_round = 1;
           return;
        }
        flicker(msg);
      }
      });
  }
