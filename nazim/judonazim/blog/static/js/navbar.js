



function nazilogohover()
{
//alert('asasasa')
//  document.getElementById('navbar').style.backgroundColor = "#07071A";


$('#navbar').css({
  'backgroundColor':'#07071A'

});


}

function nazilogoleave()
{
  //document.getElementById('navbar').style.backgroundColor = "#010001";
  $('#navbar').css({

     'backgroundColor':'#010001'
  });
  $('#judonazimnavimg').animate({opacity:1},1000);
  $('#fire').css("filter","saturate("+0+")" );
  $('#fire').animate({opacity:0},1000);
}
$('#judonazimnavimg').mouseover(function(){

   $('#fire').css('display', 'inline-block');
   $('#fire').css("filter","saturate("+0.5+")" );
   $('#fire').animate({opacity:1},1000);
   $(this).animate({padding:'2px',opacity:0.8},1000);
   $(this).animate({padding:'-2px'},1000);


});
