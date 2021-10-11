/*$(document).ready(play(1, 'm'));*/
var currPage = 1;
setInterval(playlist, 1000);


function playfirst(plylist_index)
{
  pausemediainpreviouspage(currPage);
  currPage = plylist_index;
  var media_elems = $('li').eq(plylist_index-1).find('video, audio');
  var length = media_elems.length;
  if(length<=0)
  {
    return;
  }
  $(media_elems[0])[0].play();
}
function pausemediainpreviouspage(prevpageindex)
{
  var media_elems = $('li').eq(prevpageindex-1).find('video, audio');
  var length = media_elems.length;
  {
    for(i=0;i<length;i++)
    {
      $(media_elems[i])[0].pause();
    }
  }

}
function playlist()
{

  var media_elems = $('li').eq(currPage-1).find('video, audio');
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
  /*
  for(i=0;i<length-1;i++)
  {
    var nextindex = (i+1)%length;
    var elem = $(media_elems[i])[0];
    var nextmedia = $(media_elems[nextindex])[0];
    elem.addEventListener('ended', function(){nextmedia.play()}, false);
  }
   $(media_elems[0])[0].play();*/
}
function play(elem)
{
  try {
      elem.autoplay = true;
      elem.play();
  } catch (e) {
    elem.play();


  } finally {
    return;
  }


}

/*function play(index=1, prefix="m")
{

  var elem = $("#"+prefix + index);
  var pageholder = elem.parents("li");
  var res = pageholder.is(":visible");
  if(res)
  {
    try
    {
       elem[0].play();
       alert("elem.get(0).play()");
    }
    catch(e)
    {
      elem.play();
      alert("elem.play()");
    }
    finally
    {

      var nextindex = index +1;

      var length = $("."+prefix).length;

      if(nextindex<=length)
      {
         elem.addEventListener('ended', play(nextindex, prefix));
         alert('finally');
      }
    }
  }
}*/
