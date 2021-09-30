

	$(document).ready(floadtexteditor);
	//fwiggle();


function floadtexteditor()
{
  var editor = $('.richtext');
	editor.editing.view.change( writer => {
	    writer.setStyle( 'height', '600px', editor.editing.view.document.getRoot() );
	} );
	/*$("#txtEditor").Editor();

	var stxt = 'רשום כאן';
  $("#txtEditor").Editor('setText',stxt);
	$("#txtEditor").Editor('align','right');
*/

}
$("#btnshowtxteditor").click(function () {floadtexteditor();});



function fwiggle(elem_name = '.container-fluid', interval = 1000, max_magnitude_for_wig = 3)
{

		setInterval(function() {
  //console.log("timer!");
	wiggle(elem_name, Math.floor(interval/2), max_magnitude_for_wig);
},interval);

}

function wiggle(elem_name, wig_dir_time, max_magnitude_for_wig)
{

	var strtop = $(elem_name).css('top');
	var strleft = $(elem_name).css('left');
	var orgtop = strtop;
	var orgleft = strleft;
  var numtop = parseInt(strtop.replace('px',''));
	var numleft = parseInt(strleft.replace('px',''));
  var orientVer = Math.pow(-1, Math.floor(Math.random() * 3));
	var orientHor = Math.pow(-1, Math.floor(Math.random() * 3));
	var magnitudeVer = Math.floor(Math.random() * (max_magnitude_for_wig +1));
	var magnitudeHor = Math.floor(Math.random() * (max_magnitude_for_wig +1));
	var msforchange = Math.floor(Math.random() * (wig_dir_time*2)) +wig_dir_time +1;
	var msforreturn = Math.floor(Math.random() * (wig_dir_time*2)) +wig_dir_time +1;


  magnitudeHor = magnitudeHor*orientHor;

	magnitudeVer = magnitudeVer*orientVer;

	strtop= (magnitudeVer + numtop) + "px";
	strleft = (magnitudeHor + numleft) + "px";



	//$('.col-lg-9').an
//animate({'border-width':'12px'},1000);
	//$('.col-lg-9').animate({'border-width':'10px'},1000);
	$('.container-fluid').animate({top:strtop, left:strleft},msforchange);
	$('.container-fluid').animate({top:orgtop, left:orgleft},msforreturn);
//	$('.col-lg-9').animate({borderTopColor:"#ffffff"},100);

	//$('.col-lg-9').animate({borderTopColor:"#000000"},100);
	  //  $('.Timer').text((new Date - start) / 1000 + " Seconds");


}
//function(){$(this).animate({color:'white'},1000);}
