function get_pop_cklst_name()
{
  var active_cklst = $('.active-cklst');
  return get_cklst_type($(active_cklst).first().attr('id'));
}

$('.trigger-cklst').click(function(){
  $(this).addClass('active-cklst');
  var cklst_of_what = get_pop_cklst_name();
  title = "שמור ל";
  var name = '#' + cklst_of_what;
  $(name + ' .popup-msg-title').text(title);
  set_body_of_cklst(cklst_of_what);
  //ok_btn = "הבנתי";
//  set_popup_cklst(title, body);

  $(name).fadeIn("slow");
  $('body').append('<div id="darken-screen"></div>');
  $('#darken-screen').on('click', hide_popup_cblst);
});

function hide_popup_cblst()
{
  var name = get_pop_cklst_name();
  $('#' + name).hide();
  var body = get_body_cblst();
  $(body).empty();
  $(this).remove();
  $('.trigger-cklst').removeClass('active-cklst');

  $('.popup-new-label-post').css('display', 'flex');
  $('.popup-new-label-entery-field').hide();
  $('.standard-txt-input').val('');
}
$('.popup-cklst-close').click(function(){
    $('#darken-screen').remove();
    hide_popup_cblst();
});





//start
function get_cklst_type(id)
{
  var cklst_of_what = 'popup-'+ id;
  return cklst_of_what;
}



$('body>*:not(#' +  get_pop_cklst_name() + ', #' + get_pop_cklst_name() + ' *)').click(
  function(){
  var hidden_status = $('#' + get_pop_cklst_name()).css('display');
  if(hidden_status == none || String(hidden_status) == 'none')
  {
    return;
  }

});



$("#" + get_pop_cklst_name() + ' .popup-cklst-close').click(function(){
  $("#" + get_pop_cklst_name()).hide();
  $('#darken-screen').remove();
  var body = get_body_cblst();
  $(body).empty();
  $('.trigger-cklst').removeClass('active-cklst');

  $('.popup-new-label-post').css('display', 'flex');
  $('.popup-new-label-entery-field').hide();
  $('.standard-txt-input').val('');

});


function get_body_cblst()
{
  return $("#" + get_pop_cklst_name() + ' .popup-cblst-body').first();
}
//end
function set_body_of_cklst(cklst_of_what)
{

      get_cblist_ajax(cklst_of_what, function(result){
      var elem = get_body_cblst();
      //fill_cklst_popup(result, elem, cklst_of_what);

      for(var i=0;i<result.length;i++)
      {
        var info = result[i];
        create_row_item(elem, info, cklst_of_what, i);

      }
    });


}
$('.popup-new-label-post').click(function(){
  $(this).hide();
  $('.popup-new-label-entery-field').css('display', 'flex');

});

$('.create-label-btn-wrapper').click(function(){

  var txt_field = $(this).parent('.popup-new-label-entery-field').find('.label-name-field').first();
  var txt = $(txt_field).val();
  if(txt.length == 0)
  {
    $(txt_field).attr('placeholder', 'חובה להזין טקסט');
    return;
  }
  if(txt.length < 5)
  {
    $(txt_field).val('');
    $(txt_field).attr('placeholder', 'טקסט חייב להיות בין 5 תווים לפחות');
    return;
  }
  create_new_label_for_post(txt)
  $('#darken-screen').remove();
  hide_popup_cblst();
});
function create_new_label_for_post(txt)
{

  var cblist_of_what = get_pop_cklst_name();
  create_new_label_to_post_ajax(cblist_of_what, txt, function(result){

  });
  //create_new_label_to_post_ajax
}

function create_row_item(elem, info, cklst_of_what, index = 0)
{

  var item_name = info['item_name'];
  var item_id = info['id'];
  var row_item_holder_name = "cblst-item-holder-" + item_id;

  var item_id_name = item_name + item_id;
  var is_checked = info['checked'];
  var visible = get_visible_val(is_checked);
  var checked = '';
  if(visible == 'visible')
  {
    checked = 'checked';
  }
  var cb = '<input ' + checked + ' style="visibility:' + visible  +';"' + ' data-id="' + item_id +'"' + ' type="checkbox" class="cb"' + ' id="' +  item_id_name +   '">';
  var txt = '<span>' + info['txt'] + '</span>';
  var row_id_name = 'row-' + item_id_name;
  var odd_or_even = parseInt(index) + 1;
  var oddeven = 'odd';
  if (odd_or_even % 2 == 0)
  {
    oddeven = 'even';
  }

  var row = '<div id="' + row_id_name + '" class="cblst-item">';
  var row_item_holder = '<div class="cblst-item-holder '+ oddeven + '" id="'+ row_item_holder_name + '">';
  var remove_btn_name = 'remove-cb-label-item-' + item_id;
  var remove_btn = '<span id="' + remove_btn_name +  '" class="remove_cb_label_item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"  class="bi bi-trash-fill" viewBox="0 0 16 16">';
  remove_btn += '<path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>';
  remove_btn += '</svg></span>'

  row = row + cb + txt + '</div>';
  row_item_holder = row_item_holder + row + remove_btn + "</div>";
  $(elem).append(row_item_holder);
  $(item_id_name).prop('checked', is_checked);
  $('#'+ row_id_name).on('click', cblst_item_pressed);
  $('#' + remove_btn_name).on('click', quick_delete_label_item);
   $('#'+ row_item_holder_name).on('mouseover', expose_label_item_23);
   $('#'+ row_item_holder_name).on('mouseout', hide_label_item_23);
  // $('#'+ row_id_name + ' input[type="checkbox"]').on('change', cb_changed);


}
function expose_label_item_23()
{
      $(this).find('.remove_cb_label_item').first().css('visibility', 'visible');
}
function hide_label_item_23()
{
  $(this).find('.remove_cb_label_item').first().css('visibility', 'hidden');
}

function get_visible_val(is_checked)
{
  var visible = 'hidden';
  if(is_checked == true || is_checked == 'true')
  {
    visible = 'visible';
  }
  return visible;
}
function quick_delete_label_item()
{

  var cblst_selector =  ".cblst-item-holder";
  var cklst_of_what = get_pop_cklst_name();
  var row_item = $(this).parents(cblst_selector).first();
  var id = $(row_item).find('.cb').first().data('id');
  quick_delete_label_item_ajax(id, cklst_of_what, function(result){
     $(row_item).remove();
     repair_odd_even_colors();
  });
}
function  repair_odd_even_colors()
{
  var index = 1;
  $('.cblst-item-holder').each(function(){
    $(this).removeClass('odd');
    $(this).removeClass('even');
    if(index % 2 == 0)
    {
        $(this).addClass('even');
    }
    else
    {
      $(this).addClass('odd');
    }
    index +=1;
  });
}
function cblst_item_pressed()
{
  var cb = $(this).find('.cb').first();
  //var cb_id = $(cb).attr('id');
  var is_checked = $(cb).prop('checked');
  is_checked = !is_checked;
  var visible = get_visible_val(is_checked);
  $(cb).css('visibility', visible);
  $(cb).prop('checked', is_checked);
  var label_id =  $(cb).data('id');
  save_update_cklst_to_db(label_id, is_checked);


}

/*function cb_changed()
{
      var label_id =  $(this).data('data-id');
      var is_checked = $(this).prop('checked');
      save_update_cklst_to_db(label_id, is_checked);
}*/


function save_update_cklst_to_db(label_id, is_checked)
{
  var cklst_of_what = get_pop_cklst_name();
  //call ajax
  save_update_cklst_ajax(cklst_of_what, label_id, is_checked, function(result){

  });
  /*if($(this).hasClass('popup-label-post'))
  {
    //calls ajax;
  }*/
}

/*$('.popup-new-label-post').click(function(){
  save_update_cklst_to_db();
}):*/
