

var curr_active_page = 1;

$(document).ready(finit);

function finit()
{
  $('.center').show();
  if(get_num_of_pages() <= 1)
  {
    $('#ulnavpages').hide();
    playfirst(1);
    return;
  }
  init_pages_nav_links();
  $('#ulnavpages li').eq(get_num_of_pages()-1).after("<li class='arrows next'><a href='#hg1bgc'>&#10095;</a></li>");
  $('#ulnavpages li').eq(0).before("<li class='arrows prev'><a href='#hg1bgc'>&#10094;</a></li>");
  displaypage();
  $('#ulnavpages li.arrows.next').on('click', function(){nextarrow();});
  $('#ulnavpages li.arrows.prev').on('click', function(){prevarrow();});
  playfirst(1);
}

function init_pages_nav_links()
{
  var num_of_pages = get_num_of_pages();
  for(i=1;i<=num_of_pages;i++)
  {
    $('#ulnavpages').append("<li><a href='#hg1bgc'>"+i+"</a></li>"); // value of list item will be his number in the order

    if(i>3)
    {
        $('#ulnavpages li a:contains('+i+')').parent().css('display', 'none');
    }
  }
  $('#ulnavpages li:not(.arrows)').on('click', function(){display($(this).index());}); //assign event handler\delegate to list items on click

}
function prevarrow()
{

  var prevpage = curr_active_page - 1;
  if(prevpage<1)
  {
    return;
  }
  display(prevpage); //because of zero index

}
function nextarrow()
{

  var nextpage = curr_active_page + 1;
  if(nextpage > get_num_of_pages())
  {
    return;
  }
  display(nextpage); //because of zero index

}

function display(index)
{
  displaypage(index);
  pages_nav_to_display(index);
  curr_active_page = index;
  playfirst(index);
}

function displaypage(activepage = 1)
{

  var num_of_pages = get_num_of_pages();
  var selector_pagination = $('#ulnavpages li');
  var selector_pages = $('#ulpages li');
  for(i=1;i<=num_of_pages;i++)
  {
    if(i==activepage)
    {
      selector_pages.eq(i-1).css('display', 'block'); //-1 because of the arrow
    /*  $('#ulnavpages li').eq(i).css('color', 'blue');*/
      selector_pagination.eq(i).css('background-color', '#4CAF50');
      continue;
    }

     selector_pages.eq(i-1).css('display', 'none');
  /*  $('#ulnavpages li').eq(i).css('color', 'black');*/
    selector_pagination.eq(i).css('background-color', '#ffffff');

  }

}

function pages_nav_to_display(activepage)
{
  var num_of_pages = get_num_of_pages();
  if(activepage  >= num_of_pages || activepage <= 1)
  {
    return;
  }
  var selector = $('#ulnavpages li');

  if(selector.eq(activepage+1).css('display') == 'none')
  {
    selector.eq(activepage+1).show();
    selector.eq(activepage-2).css('display', 'none');
  }

  if(selector.eq(activepage-1).css('display') == 'none')
  {
    selector.eq(activepage-1).show();
    selector.eq(activepage+2).css('display', 'none');

  }

}
function get_num_of_pages()
{

  return $('#ulpages li').length;
}
