

//aimed to open hidden box when item has been clickedin nav bar
//nextall select the first matched element after the ellment
//in this case, after the clicked element
$(document).ready(fload);

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

function fload()
{


setInterval(function() {
//console.log("timer!");
rotate($('.logoright'));
},100);

setInterval(function() {
//console.log("timer!");
rotate($('.logoleft'), -1);
},100);


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
