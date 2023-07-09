$(document).ready(function(){

  //$('#mr-event-handler').on('click', styled_droped_down_clicked);
  //$('#mr-event-handler').on('mouseleave', styled_droped_down_mouseleave);
  //$('#mr-event-handler').on('click', styled_droped_down_item_selected);




  $('.dict-ddl').each(function(){
    var lst = [];

    var ddl_id = $(this).prev('select').attr('id');
    $('#' + ddl_id).hide();
    lst.push(ddl_id);

    $(this).children('.dict-item').each(function(){
      var txt = $(this).children('.ddl-txt').first().text();
      var svg = $(this).children('.ddl-svg-item').first();
      lst.push({'txt':txt, 'svg':$(svg)});
    });

    set_icons_to_list_items(lst);
  });


});


function styled_droped_down_clicked()
{
  $(this).parents('.styled-drop-down-wrapper').find('.styled-droped-down-body').css('display', 'flex');
}


function styled_droped_down_mouseleave()
{
    $(this).hide();
}

function styled_droped_down_item_selected()
{

  var ancestor = $(this).parents('.styled-drop-down-wrapper').first();
  var select_display = $(ancestor).find('.styled-droped-down-selected-box').first();

  var clone = $(this).clone(true);
  var selected_item = $(select_display).find('.display-choice-styled-droped-down').first();
  $(selected_item).remove();


  $(ancestor).find('.styled-droped-down-body').before($(clone));
  $(clone).removeClass('styled-droped-down-item');
  $(clone).addClass('display-choice-styled-droped-down');
  $(ancestor).find('.styled-droped-down-body').first().hide();





  var opt_index = $(this).prevUntil('.styled-droped-item-template').length;
  
  udpate_val_on_linked_frmdropdwonlist($(ancestor), opt_index);
}

function set_styled_ddl_val_on_initiate(frm_ddl, styled_ddl)
{
   var index = $(frm_ddl)[0].selectedIndex;
   var styled_ddl_id = $(styled_ddl).attr('id');
   var object_to_clone = $('#' + styled_ddl_id + ' .styled-droped-down-item').eq(index + 1);
   var clone = $(object_to_clone).clone(true);

   $(styled_ddl).find('.styled-droped-down-body').before($(clone));
   $(clone).removeClass('styled-droped-down-item');
   $(clone).addClass('display-choice-styled-droped-down');

}


function set_icons_to_list_items(arr)
{

  var dropdown = arr[0];
  initate_styled_dropdown(dropdown);
  var styled_dropdown_selector = "#styled-" + dropdown;
  var styled_dropdown = $(styled_dropdown_selector);




  var elem_to_clone;

  //$(styled_dropdown).find('.styled-drop-down-btn').first().on('click', styled_droped_down_clicked);

  //$('#mr-event-handler').add($(styled_dropdown).find('.ddl-click-element')).on('click', styled_droped_down_clicked);
  //$('#mr-event-handler').add($(styled_dropdown).find('.styled-droped-down-body').first()).on('mouseleave', styled_droped_down_mouseleave);
  $(styled_dropdown).find('.ddl-click-element').on('click', styled_droped_down_clicked);
  $(styled_dropdown).find('.styled-droped-down-body').first().on('mouseleave', styled_droped_down_mouseleave);



  var empty_choice = null;
  var svg_cnt = arr.length - 1;
  if(is_dropdown_accept_null("#" + dropdown, svg_cnt))
  {

    elem_to_clone =  $(styled_dropdown).find('.styled-droped-item-template').first();
    var elem = $(elem_to_clone).clone(true);
    $(elem).removeClass('styled-droped-item-template');
    $(elem).find('.styled-dd-txt').first().html('-');
    $(styled_dropdown).find('.styled-droped-down-body').first().append($(elem));

    empty_choice = $(elem);
    //$('#mr-event-handler').add($(elem)).on('click', styled_droped_down_item_selected);
    $(elem).on('click', styled_droped_down_item_selected);


  }

  for(var i=1;i<arr.length;i++)
  {
    var dict = arr[i];
    var txt = dict['txt'];
    var svg = dict['svg'];
    elem_to_clone =  $(styled_dropdown).find('.styled-droped-item-template').first();
    var cloned = $(elem_to_clone).clone(true);
    $(cloned).removeClass('styled-droped-item-template');
    $(cloned).find('.styled-dd-txt').first().html(txt);
    $(cloned).find('.styled-dd-svg').first().html(svg);

    $(styled_dropdown).find('.styled-droped-down-body').first().append($(cloned));


    //$('#mr-event-handler').add($(cloned)).on('click', styled_droped_down_item_selected);
    $(cloned).on('click', styled_droped_down_item_selected);





  }

  if(empty_choice != null)
  {
    //eq 2 because 0 is styled-droped-item-template)
    //and index 1 is the empty -
   //var get_first_item = $(styled_dropdown).find('.styled-droped-down-item').eq(2);
   //var height = $(get_first_item).find('.styled-dd-svg').first().height();
   //$(empty_choice).height(height);
   $(empty_choice).children().css('height', '30px');

  }

  set_styled_ddl_val_on_initiate("#" + dropdown, styled_dropdown);
}


function is_dropdown_accept_null(dropdown, svg_cnt)
{

  if($(dropdown).children('option').length > svg_cnt)
  {
    return true;
  }
  return false;
}

function udpate_val_on_linked_frmdropdwonlist(styled_ddl, opt_index)
{

  var frm_ddl_id = $(styled_ddl).attr('id');
  frm_ddl_id = frm_ddl_id.replace('styled-', '');




  $("select#" + frm_ddl_id).prop('selectedIndex',opt_index);



}

function initate_styled_dropdown(append_before)
{
  var template = get_template_of_dropdown_html();
  //var append_before = "#sex-up";

  $(template).insertBefore('#' + append_before);
  var styled_dropdown = $('#' + append_before).siblings('.styled-drop-down-wrapper').first();
  $(styled_dropdown).attr('id', 'styled-'+ append_before);



}



function get_template_of_dropdown_html()
{
  var template = '<div class="styled-drop-down-wrapper signfield" id="">';

  //new row
  template += '<div class="ddl-click-element">  </div>';

  template+= '<div class="style-drop-down">';
  template+= '<div class="styled-droped-down-selected-box">';

  template+=  '<div class="styled-droped-down-body">';
  template+= '<div class="styled-droped-down-item styled-droped-item-template">';
  template+= '<span class="styled-dd-txt"></span>';
  template+= '<span class="styled-dd-svg"></span>';
  template+= '</div>';
  template+='</div>';
  template+=     '</div>';

  template+= '</div>';



  template+= '<div class="styled-drop-down-btn">';
  template+= '<span class="styled-dd-arrow"></span>';
  template+= ' </div>';
  template+= '</div>';

  return template;

}
