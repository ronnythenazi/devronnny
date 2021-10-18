$(document).ready(start);

function start()
{
  var elem = '.horzmove';//$('.horzmove');
  wrape_chrs(elem);
  movehorz(elem);


  //movehorz($('.horzmove:not(.reverse)'));
//  movehorz($('.horzmove.reverse'), dir = -1);
}
