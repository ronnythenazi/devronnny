//$(document).ready(play(1, 'm'));
//play automatically all media, one by one, and repeat
//like a loop, this is my own version of
//auto playist, playing in a loop
//I tested and it work really great

var currPage = 1;
setInterval(playlist, 1000);

function playfirst(plylist_index)
{
  pausemediainpreviouspage(currPage);
  currPage = plylist_index;
  var media_elems = $('li').eq(plylist_index-1).find('video, audio').not('.noauto');
  var length = media_elems.length;
  if(length<=0)
  {
    return;
  }
  $(media_elems[0])[0].play();
}
function pausemediainpreviouspage(prevpageindex)
{
  var media_elems = $('li').eq(prevpageindex-1).find('video, audio').not('.noauto');
  var length = media_elems.length;
    for(i=0;i<length;i++)
    {
      $(media_elems[i])[0].pause();
    }

}
function playlist()
{

  var media_elems = $('li').eq(currPage-1).find('video, audio').not('.noauto');
  var length = media_elems.length;

  for(i=length;i>0;i--)
  {
    var nextindex = i%length;
    var nextclip = $(media_elems[nextindex])[0];
    var curr_clip = $(media_elems[i-1])[0];
    if(curr_clip.pause && curr_clip.currentTime>0 && curr_clip.ended)
    {
      curr_clip.currentTime = 0;
      nextclip.play();
    }
  }

}

$('.vidandtitlecontainer, .centerfootage').hover(function(){$(this).children('.vidandtitlecontainer.bg').animate({opacity:0},300);});
$('.vidandtitlecontainer').mouseleave(function(){$(this).children('.vidandtitlecontainer.bg').animate({opacity:1},200);});
$('.playgifico').click(function(){showvideoonplaybtnclick($(this));});
$('.centerfootage').click(function(){showvideoonplaybtnclick($(this));});

function showvideoonplaybtnclick(self)
{

  $('.centerfootage').animate({opacity:'0'},2000);
  $('.playgifico').animate({opacity:'0'},2000);
  setTimeout(function(){
   $('.centerfootage').css('z-index', '0');
   $('.playgifico').css('z-index', '0');
   self.siblings('video')[0].play();
 }, 1000);



}
