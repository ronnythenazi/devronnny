

//aimed to open hidden box when item has been clickedin nav bar
//nextall select the first matched element after the ellment
//in this case, after the clicked element
var isaudioplay;
$(document).ready(fload);
var arrColors = ['red', 'orange', 'blue', 'green', 'white', 'purple', 'yellow', 'pink', '#9b4a17', '#00fff6'];

$('.arrow-up').click(function(){
  $('body, html').animate({scrollTop:0}, 200);
  });


$(function() {
 $(window).scroll(
  function()
   {
    var atop = $(this).scrollTop;
    //alert(atop);
     if(atop>0)
     {

      $('#navbar').animate({height:'100px'}, 100);
     }
     else {

       $('#navbar').animate({height:'150px'}, 100);
     }
}
);
});

$(window).scroll(function(){
 var distanceY = window.pageYOffset || document.documentElement.scrollTop,
 shrinkOn = 300,
 body = document.querySelector('.item0');
 if ($(this).scrollTop() > 450){
     $('body').addClass("scroll");
 }
 else{
     $('body').removeClass("scroll");
 }
 });

$('button').click(function(){
    var curr_url = window.location.href;
    var url_sub_str = 'magazine/about-ronny-the-nazi/';
    if(curr_url.includes(url_sub_str))
    {
       var new_url = curr_url.replace(url_sub_str , '');
       window.location.href = new_url;
       /*$(this).attr('type', 'submit');
       %(this).parents('form').first('submit');*/

    }


});
$('.menuitemwarpper').mouseover(function(){

  var curr_url = window.location.href;
  var url_sub_str = 'magazine/about-ronny-the-nazi/';
  if(curr_url.includes(url_sub_str))
  {
     var new_url = curr_url.replace(url_sub_str , '');
     window.location.href = new_url;
     /*$(this).attr('type', 'submit');
     %(this).parents('form').first('submit');*/
   }
});

function fload()
{
  var curr_url = window.location.href;
  var url_sub_str = 'magazine/about-ronny-the-nazi/';
  if(curr_url.includes(url_sub_str))
  {
     $('button').attr('type', 'button');

  }

setInterval(function() {
//console.log("timer!");
rotate($('.logoright'));
},100);

setInterval(function() {
//console.log("timer!");
rotate($('.logoleft'), -1);
},100);

setInterval(isended, 1000);


$('.txtaudio').mouseover(function(){
  $(this).css('background-color', 'black');

});
$('.txtaudio').mouseout(function(){
  $(this).css('background-color', 'black');

});

$('#pushbutton').click(function(){
  setaudiotxt();

});

$('.txtaudioparent').click(function(){
  if(isaudioplay == true)
  {
    resetaudiotxt($('.txtaudio'));
  }
});
}


function isended()
{
  var aud = $('.hiddenaudio')[0];
  try {

    if(aud.ended)
    {
      resetaudiotxt($('.txtaudio'));

    }

  } catch (e) {

    return;

  } finally {

  }

}


function setaudiotxt()
{
  setTimeout(function(){
    $('.hiddenaudio')[0].play();


  isaudioplay = true;
  $('.txtaudio').css({border:'0 blue solid'}).animate({borderWidth:5}, 100);
/*  $('.txtaudio').children().css({border:'0 blue solid'}).animate({borderWidth:5}, 100);*/
  $('.txtaudio').show('fast');
  $('#pushbutton').hide('fast');
}, 300);
  setInterval(rotatecolors, 200);

}

function rotatecolors()
{
  let childs = $('.txtaudio span');
  let l = childs.length;
  for(var i=0;i<l;i++)
  {
     var kid = childs[i];
     $(kid).css('border-top-color', arrColors[i]);
     $(kid).css('border-bottom-color', arrColors[i+1]);

  }

  let lastcolor = arrColors[l-1];
  arrColors.pop();
  arrColors.unshift(lastcolor);

}

function resetaudiotxt(e)
{
  isaudioplay = false;
  //$(e).animate({borderWidth:0}, 500);
  //$(e).children().animate({borderWidth:0}, 500);
  $('.hiddenaudio')[0].pause();
  $('.txtaudio').hide('fast');
  $('#pushbutton').show('slow');
}


function rotate(elem, dir=1)
{
    var angel = getRotationDegrees(elem);
    elem.animate(
    { deg:(angel + (100*dir))},
    {
      duration: 1,
      step: function(now) {
        $(this).css({ transform: 'rotate(' + now + 'deg)' });
      }
    }
  );
}

function getRotationDegrees(obj) {
    var matrix = obj.css("-webkit-transform") ||
    obj.css("-moz-transform")    ||
    obj.css("-ms-transform")     ||
    obj.css("-o-transform")      ||
    obj.css("transform");
    if(matrix !== 'none') {
        var values = matrix.split('(')[1].split(')')[0].split(',');
        var a = values[0];
        var b = values[1];
        var angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
    } else { var angle = 0; }
    return (angle < 0) ? angle + 360 : angle;
}

$(".sub_subject_box").click(
  function ()
  {

    var displaystatus = $(this).nextAll(".sub_list").css('display');

    if(displaystatus == 'none')
    {
      $('.sub_list').hide('fast');
      $(this).nextAll(".sub_list").show('fast')
    }
    else
    {
      $(this).nextAll(".sub_list").hide('fast');
    }
  }
);
$('.sub_list').dblclick(function(){$(this).hide('fast');});








//$(".sub_list").mouseout(function(){$(this).css('display', 'none')});

/*$("#btn_expose_img").click(function ()
{
  var display_val = $('#imghitler').css('opacity');
  if(display_val == '0')
  {
    $('#imghitler').css('display', 'inline-block');
    change_btn_style($(this), "red", "black")
    animate_img_appear($('#imghitler'),2000)
    return;
  }
//
  change_btn_style($(this), "blue", "white")
  animate_img_disappear($('#imghitler'));
  //$('#imghitler').css('display', 'none');
}
);

function animate_img_appear(obj, t = 2000)
{
  obj.animate({height:'200px', width:'200px', opacity:1}, t);
}
function animate_img_disappear(obj, t = 2000)
{
  obj.animate({height:'0px', width:'200px', opacity:0}, t);
}
function change_btn_style(obj, bg, fclr)
{
  obj.css({"background-color":bg,
"color":fclr
})
}*/
