function wrape_chrs(elemToAppend)
{
  var txt = $('.hidtxt').text();
  if(txt.length<=0)
  {
    return;
  }
  for(var i=0;i<txt.length;i++)
  {
    $(elemToAppend).append('<span class="spintxt blueglowclr">'+txt[i]+'</span>');
  }

}
