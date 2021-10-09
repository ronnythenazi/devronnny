
$(document).ready(finit);

function finit()
{
  init_pages_nav_links();
  displaypage();

}
function init_pages_nav_links()
{
  var num_of_pages = get_num_of_pages();
  for(i=1;i<=num_of_pages;i++)
  {
    $('#ulnavpages').append("<li><a>"+i+"</a></li>"); // value of list item will be his number in the order

    if(i>3)
    {
        $('#ulnavpages li a:contains('+i+')').parent().css('display', 'none');
    }
  }
  $('#ulnavpages li').on('click', function(){display($(this).index());}); //assign event handler\delegate to list items on click

}

function display(index)
{

  displaypage(index);
  pages_nav_to_display(index);
}

function displaypage(activepage = 0)
{
  var num_of_pages = get_num_of_pages();
  for(i=0;i<num_of_pages;i++)
  {
    if(i==activepage)
    {
      $('#ulpages li').eq(i).css('display', 'block');
      $('#ulnavpages li').eq(i).css('color', 'blue');
      continue;
    }

    $('#ulpages li').eq(i).css('display', 'none');
    $('#ulnavpages li').eq(i).css('color', 'black');

  }

}

function pages_nav_to_display(activepage)
{

  var num_of_pages = get_num_of_pages();
  if(activepage  == (num_of_pages-1) || activepage == 0)
  {
    return;
  }



  //var nextpage = activepage+1;
  if($('#ulnavpages li').eq(activepage+1).css('display') == 'none')
  {
    $('#ulnavpages li').eq(activepage+1).show();
    $('#ulnavpages li').eq(activepage-2).css('display', 'none');
  }

  if($('#ulnavpages li').eq(activepage-1).css('display') == 'none')
  {
    $('#ulnavpages li').eq(activepage-1).show();
    $('#ulnavpages li').eq(activepage+2).css('display', 'none');

  }

}
function get_num_of_pages()
{
  return $('#ulpages li').length;
}




/*
$('ul li a').live('click', function() {
    console.log($(this).parent('li').index());
});
*/
