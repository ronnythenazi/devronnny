var defaultmiddwidth;

$.fn.HasScrollBar = function() {
    //note: clientHeight= height of holder
    //scrollHeight= we have content till this height
    var _elem = $(this)[0];
    var _hasScrollBar = false;
    if (_elem.scrollWidth - _elem.clientWidth > 200) {
        _hasScrollBar = true;
    }
    return _hasScrollBar;
}


$(document).ready(setup);

$( window ).resize(function() {
   /*var isOverFlowX  = $('body').HasScrollBar();
   var viewPortWidth =  $(window).width();*/
   if(isOverFlowX)
   {
        $('.item1').hide();
        $('.item2').removeClass('takewholesspace');
        $('.item2').addClass('takewholesspace');
        $('.item2').after('.menubarsfather');
        $('body').removeClass('scrollbar');
        $('body').addClass('scrollbar');
   }
   else {
      $('.item2').removeClass('takewholesspace');
      $('.item2').after('.item1');
      $('body').removeClass('scrollbar');
      $('.item1').show();
   }

});
  /* if(sizechange > 1.1)
   {
     $('.item1').hide();
   }
   else {
     $('.item1').show();
   }*/



function setup()
{
  defaultmiddwidth = $('.item2').width();
}
