



$("#btn_expose_img").click(function ()
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
}
