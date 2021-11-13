var laptopwidth = 1519;
var minWindowWidth = 1312;
var middDefMinWidth;
var navrightDefMinWidth;
var sloganfontsize;
var prevSizeWasBiggerOrEqualToDefaultWindowSize;

$.fn.tagNameLowerCase = function()
{
  return $(this).prop('tagName').toLowerCase();
}

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


$(document).ready(fsetup);



function fsetup()
{
  var currWindowWidth = $(window).width();
  if(currWindowWidth >= minWindowWidth)
  {
    prevSizeWasBiggerOrEqualToDefaultWindowSize = true;
  }
  else
  {
    prevSizeWasBiggerOrEqualToDefaultWindowSize = false;
  }

    setGeneral('item1');
    setGeneral('item2');
    saveDefFontSize('maincontext');
    middDefMinWidth  = parseInt($('.item2').css('min-width').replace("px", ""));
    navrightDefMinWidth  = parseInt($('.item1').css('min-width').replace("px", ""));
    adjust_to_screensize();
}

$(window).resize(adjust_to_screensize);

function adjust_to_screensize()
{
  var currWindowWidth = $(window).width();
  var ratio = (currWindowWidth/laptopwidth);

  if(currWindowWidth >= minWindowWidth)
  {
       if(prevSizeWasBiggerOrEqualToDefaultWindowSize)
       {
          return;
       }
       revertToDefault();
       prevSizeWasBiggerOrEqualToDefaultWindowSize = true;
       return;
  }

   var sloganFontSize = "60px";

    if(currWindowWidth<=1500)
    {
     sloganFontSize = "50px";
    }
    if(currWindowWidth<=1300)
    {
      $('.judonazimlogorotate').width(75);
      $('.judonazimlogorotate').height(75);
      sloganFontSize = "45px";
    }
   if(currWindowWidth<=1100)
    {
      $('.judonazimlogorotate').width(65);
      $('.judonazimlogorotate').height(65);
      sloganFontSize = "37px";
    }
    if(currWindowWidth <= 1300)
    {
      setFontSize('maincontext', 1.5);
    }
    if(currWindowWidth<=800)
    {
      $('.judonazimlogorotate').width(50);
      $('.judonazimlogorotate').height(50);

      $('.hg1middleimg').height(100);
      $('.hg1middleimg').width(100);

      $('body').css('overflow-x', 'auto');

      $('.item1').hide();


      $('.bodyflex').css('align-items', 'stretch');
      $('.maingrid').css('justify-content', 'stretch');
      $('.middle_section').css('justify-content', 'stretch');

      $('.stretchToWindowWidth').width($(window).width());
      $('.item2').width($(window).width());

      $('.maingrid').addClass('wholespace');

      $('.middle_section').width($(window).width());



      $('.menu').height(40);

      $('.menu').css('font-size', '15px');
    //  $('.menu').css('justify-content', 'center'); new


      $('.popupmenu>ul>li').css('line-height', '15px');
      $('.popupmenu button').css('font-family', 'formal');
      $('.popupmenu button').css('font-size', '8px');

      $('.menuitem>.menuitembutton').css('font-size', '8px');
      $('.menuitem>.menuitembutton>button>span').removeClass('robotstroke');

      $('.popupmenu>ul>li>button').css('padding-top', '9px');
      $('.popupmenu>ul>li>button').css('padding-bottom', '9px');
      $('.submenuitemico').css('width', '12.5px');
      $('.submenuitemico').css('height', '12.5px');
      $('.ico').width(20);

      $('.maincontext>#ulpages *').addClass('tinyfont');
      $('.maincontext>#ulpages *').removeClass('verytinyfont');
      $('.arrow-up').width(35);
      $('.arrow-up').height(35);
      $('.arrow-up').css('font-size', '20px');

    //   setPopupsDataHeight(); //new


      $('.menuitemtitle').css('font-size', '10px');
      $('.menuitemtitlewarrper:last-child').css('height', '50%');

      $('#ulnavpages').css('font-size', '15px');
      $('#ulnavpages').css('line-height', '30px');
      $('#ulnavpages>li').css('border-width', '1.5px');
      $('#ulnavpages>li a').css({'padding': '6px 12px'});



      sloganFontSize = "30px";

      setFontSize('maincontext', 1.5);
    }
    else {

      $('.item1').show();
      $('.bodyflex').css('align-items', 'center');
      $('.maingrid').css('justify-content', 'center');
      $('.middle_section').css('justify-content', 'center');

      $('.stretchToWindowWidth').width(0);


      $('body').css('overflow-x', 'hidden');
      $('.menu').height(80);

      $('.menu').css('font-size', '20px');
    //  $('.menu').css('justify-content', 'right'); //new
    //  $('.menu').css('padding-left', '0'); new


      $('.popupmenu button').css('font-size', '16px');

      $('.menuitem>.menuitembutton').css('font-size', '15px');
      $('.menuitem>.menuitembutton>button>span').addClass('robotstroke');
      $('.popupmenu button').css('font-family', 'formal');
      $('.popupmenu>ul>li>button').css('padding-left', '20px');
      $('.popupmenu>ul>li>button').css('padding-right', '20px');
      $('.popupmenu>ul>li>button').css('padding-top', '10px');
      $('.popupmenu>ul>li>button').css('padding-bottom', '10px');
      $('.submenuitemico').css('width', '25px');
      $('.submenuitemico').css('height', '25px');

      $('.ico').width(40);
      $('.maincontext').css('font-size', '20px');
      $('.maincontext>#ulpages *').removeClass('verytinyfont');
      $('.maincontext>#ulpages *').removeClass('tinyfont');
      $('.arrow-up').width(50);
      $('.arrow-up').height(50);
      $('.arrow-up').css('font-size', '25px');
      //setPopupsDataHeight(); //new

      $('.menuitemtitle').css('font-size', '15px');
      $('.menuitemtitlewarrper:last-child').css('height', '50%');

      $('#ulnavpages').css('font-size', '20px');
      $('#ulnavpages').css('line-height', '40px');
      $('#ulnavpages>li').css('border-width', '2px');
      $('#ulnavpages>li a').css({'padding': '8px 16px'});

      setFontSize('maincontext');
    }
    if(currWindowWidth<=500)
    {
      sloganFontSize = "18px";
      $('.judonazimlogorotate').width(30);
      $('.judonazimlogorotate').height(30);
      $('.item1').hide();

      $('.bodyflex').css('align-items', 'stretch');
      $('.maingrid').css('justify-content', 'stretch');
      $('.middle_section').css('justify-content', 'stretch');
      $('.item2').addClass('wholespace');

      $('.stretchToWindowWidth').width($(window).width());

      $('body').css('overflow-x', 'auto');

      $('.menu').height(30);

    //  $('.menu').css('justify-content', 'center'); new

      $('.popupmenu button').css('font-family', 'formal');
      $('.popupmenu button').css('font-size', '5px');

      $('.menuitem>.menuitembutton').css('font-size', '5px');
      $('.menuitem>.menuitembutton>button>span').removeClass('robotstroke');

      $('.popupmenu>ul>li>button').css('padding-left', '5px');
      $('.popupmenu>ul>li>button').css('padding-right', '5px');
      $('.popupmenu>ul>li>button').css('padding-top', '2.5px');
      $('.popupmenu>ul>li>button').css('padding-bottom', '2.5px');
      $('.submenuitemico').css('width', '5px');
      $('.submenuitemico').css('height', '5px');

      $('.ico').width(20);
      $('.maincontext>#ulpages *').removeClass('tinyfont');
      $('.maincontext>#ulpages *').addClass('verytinyfont');
      $('.arrow-up').width(17.5);
      $('.arrow-up').height(17.5);
      $('.arrow-up').css('font-size', '10px');

      //setPopupsDataHeight(); //new


      $('.menuitemtitle').css('font-size', '4px');
      $('.menuitemtitlewarrper:last-child').css('height', '25%');

      $('#ulnavpages').css('font-size', '10px');
      $('#ulnavpages').css('line-height', '20px');
      $('#ulnavpages>li').css('border-width', '1px');
      $('#ulnavpages>li a').css({'padding': '4px 8px'});

      setFontSize('maincontext', 2.5);
    }
    if(currWindowWidth > 800 && currWindowWidth <= 1100)
    {
      $('.menu').height(60);
      $('.popupmenu>ul>li').css('line-height', '15px');
      $('.menuitem>.menuitembutton').css('font-size', '10px');
      $('.popupmenu>ul>li>button').css('padding-top', '10px');
      $('.popupmenu>ul>li>button').css('padding-bottom', '10px');
      $('.popupmenu button').css('font-family', 'formal');
      $('.popupmenu button').css('font-size', '8px');
      //setPopupsDataHeight(); //new
    }
    if(currWindowWidth<=300)
    {
      $('.hg1middleimg').height(100);
      $('.hg1middleimg').width(100);
    }

    $('.solganwarper').css('font-size', sloganFontSize);
    if(currWindowWidth>800)
    {
     shrinkGeneral('item1', ratio);
     $('.item1').css('min-width', (ratio * navrightDefMinWidth) + "px");

     shrinkGeneral('item2', ratio);
     $('.item2').css('min-width', (ratio * middDefMinWidth) + "px");
    }


  prevSizeWasBiggerOrEqualToDefaultWindowSize = false;
}

function revertToDefault()
{
  $('.menuitem>.menuitembutton').css('font-size', '15px');
  $('.menuitem>.menuitembutton>button>span').removeClass('robotstroke');

  $('.item1').css('min-width', navrightDefMinWidth + "px");
  $('.item2').css('min-width', middDefMinWidth + "px");

  $('.solganwarper').css('font-size', '60px');

  $('.judonazimlogorotate').width(100);
  $('.judonazimlogorotate').height(100);


  $('.hg1middleimg').height(200);
  $('.hg1middleimg').width(200);

  $('body').css('overflow-x', 'hidden');

  $('.menu').css('font-size', '20px');
  $('.menu').height(80);

  //$('.menu').css('justify-content', 'right'); //new
  //$('.menu').css('padding-left', '0'); //new



  $('.popupmenu button').css('font-family', 'formal');
  $('.popupmenu button').css('font-size', '16px');

  $('.popupmenu>ul>li>button').css('padding-left', '20px');
  $('.popupmenu>ul>li>button').css('padding-right', '20px');
  $('.popupmenu>ul>li>button').css('padding-top', '10px');
  $('.popupmenu>ul>li>button').css('padding-bottom', '10px');

  $('.submenuitemico').css('width', '25px');
  $('.submenuitemico').css('height', '25px');
  $('.ico').width(40);
  $('.maincontext').css('font-size', '20px');
  $('.maincontext>#ulpages *').removeClass('verytinyfont');
  $('.maincontext>#ulpages *').removeClass('tinyfont');
  $('.arrow-up').width(50);
  $('.arrow-up').height(50);
  $('.arrow-up').css('font-size', '25px');

  revertGeneral('item1');
  revertGeneral('item2');
  setFontSize('maincontext');



  $('.menuitemtitle').css('font-size', '15px');
  $('.menuitemtitlewarrper:last-child').css('height', '50%');

  $('#ulnavpages').css('font-size', '20px');
  $('#ulnavpages').css('line-height', '40px');
  $('#ulnavpages>li').css('border-width', '2px');
  $('#ulnavpages>li a').css({'padding': '8px 16px'});

  $('.item1').show();

  $('.bodyflex').css('align-items', 'center');
  $('.maingrid').css('justify-content', 'center');
  $('.middle_section').css('justify-content', 'center');

  $('.stretchToWindowWidth').width(0);
}


function saveDefFontSize(className)
{
    var selector_obj = $('.'+ className + ', .'+ className + ' *');
    $(selector_obj).each(function(){
      var attr = $(this).attr('data-font-size')
     if(attr != undefined && attr != false)
     {
        return false;
     }

     $(this).attr('data-font-size', $(this).css('font-size'));
     $(this).attr('data-line-height', $(this).css('line-height'));

     if($(this).tagNameLowerCase() == 'img' )//|| $(this).tagNameLowerCase() == 'video')
     {
       $(this).attr('data-img-width', $(this).width());
       $(this).attr('data-img-height', $(this).height());
     }
   });

}

function setFontSize(className, magnitude = 0)
{

  var reduceFactor = 1/3;
  var fontype = String(magnitude);
  var selector_obj = $('.'+ className + ', .'+ className + ' *');
  $(selector_obj).each(function(){

    if($(this).attr('data-fontType') == fontype)
    {
        return false;
    }
    var attr = $(this).parents('#ulnavpages').first().attr('id');
    if($(this).attr('id') == 'ulnavpages' || $(this).attr('class') == 'solganwarper'  || (attr != undefined && attr != false))
    {
      return true;
    }


    $(this).attr('data-fontType', fontype);

    var defFontSize = parseInt($(this).attr('data-font-size').replace("px", ""));



    var reduceAmount = magnitude * (reduceFactor * defFontSize);
    var newFontSize = (defFontSize - reduceAmount) +"px";
    var deflineheight = parseInt($(this).attr('data-line-height').replace("px", ""));
    $(this).css('line-height', deflineheight + 'px');
    if(defFontSize >= 50 && magnitude !=0)
    {
      newFontSize = defFontSize - (magnitude * 5) - 20;
      $(this).css('line-height', (50 * magnitude) + "%");
    }

    if($(this).tagNameLowerCase() == 'img' && $(this).attr('class') != 'centerfootage' && $(this).attr('class')!='playgifico')
    {
      var defimgwidth = parseInt($(this).attr('data-img-width'));
      var defimgheight = parseInt($(this).attr('data-img-height'));
      var imgDecreaseRatio;
      if(magnitude >= 2 && $(this).width()>=100)
      {
        $(this).css('width', 100 + "px" );
        imgDecreaseRatio = $(this).width() / defimgwidth;
        $(this).css('height', (defimgheight * imgDecreaseRatio) + "px" );
      }
      else if(magnitude >= 1 && $(this).width()>=100)
      {
        $(this).css('width', 200 + "px" );
         imgDecreaseRatio = $(this).width() / defimgwidth;
         $(this).css('height', (defimgheight * imgDecreaseRatio) + "px" );
      }
      else if(magnitude == 0){
        $(this).css('width', defimgwidth + "px");
        imgDecreaseRatio = $(this).width() / defimgwidth;
        $(this).css('height', (defimgheight * imgDecreaseRatio) + "px" );
      }
      else {

      }

    }



   if(defFontSize >= 20)
   {
    $(this).css('font-size', newFontSize);
   }
    //$(this).css('line-height', newLineHeight);

  //  $(this).css('line-height', newLineHeight);

  });
}


function shrinkGeneral(className, ratio)
{

  var selector_obj = $('.'+ className + ', .'+ className + ' *');
  $(selector_obj).each(function(){
   $(this).width(parseInt($(this).attr('data-width')) * ratio);

   if($(this).attr('data-height'))
   {
      $(this).height(parseInt($(this).attr('data-height')) * ratio);
   }


});

}

 function setGeneral(className)
 {
   var selector_obj = $('.'+ className + ', .'+ className + '>*');
   $(selector_obj).each(function(){
      $(this).attr('data-width', String($(this).width()));
    });

   $(selector_obj).each(function(){
      if($(this).attr('height'))
      {
        $(this).attr('data-height', String($(this).height()));
      }
    });
}



function revertGeneral(className)
{
  var selector_obj = $('.'+ className + ', .'+ className + '>*');

  $(selector_obj).each(function(){
     $(this).width(parseInt($(this).attr('data-width')));
   });

  $(selector_obj).each(function(){
  if($(this).attr('data-height'))
     {
        $(this).height(parseInt($(this).attr('data-height')));
     }
  });


}
