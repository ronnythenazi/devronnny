$('.arrow-up').click(function(){

  $('body, html').animate({scrollTop:0}, 1000);
  });
$('.rotate-arrow-up').click(function(){
  var drop_down_arrow = $(this).find('.bi-chevron-down');
  if($(drop_down_arrow).hasClass('rotate-up'))
  {
    $(drop_down_arrow).removeClass('rotate-up');
  }
  else
  {

    $(drop_down_arrow).addClass('rotate-up');
  }
});

$('.rotate-arrow-up').mouseleave(function(){
  var drop_down_arrow = $(this).find('svg');
  $(drop_down_arrow).removeClass('rotate-up');

});

$(document).ready(function(){
  $('.btn-loader').append('<div class="loader"></div>');
  setInterval(bell_ring, 7000);
});

$('form').submit(function(){
  var btn_loader = $(this).find('.btn-loader');
  $(btn_loader).css('font-size', '0');
  $(btn_loader).children('.loader').show();
  var bluish_btn = $(this).find('.btn-loader.subscribe').first();
  if(bluish_btn)
  {

    $(bluish_btn).css('background', '#2F9BDD');
    $(bluish_btn).css('box-shadow', 'unset');
    $(bluish_btn).on('mouseover', function(){
      $(this).css('box-shadow', 'unset');
      $(this).css('background-color', '#2F9BDD');
    });
  }

  if($(btn_loader).hasClass('btnSave'))
  {
      $(btn_loader).addClass('thinking');
  }

  if($(btn_loader).hasClass('btnDeleteTrans'))
  {
      $(btn_loader).addClass('thinking');
  }
});

function bell_ring()
{
  $('.red-bell').addClass('red-bell-ring');
  setTimeout(function(){
    $('.red-bell').removeClass('red-bell-ring');
  }, 3000);
  setTimeout(2500);
  $('.red-bell').addClass('red-bell-ring-scale');
  setTimeout(function(){
    $('.red-bell').removeClass('red-bell-ring-scale');
  }, 1000);
}
$('.more-button').click(clone_elem);
$('.delete-button').click(delete_elem);

function trigger_upload()
{
  $(this).parent().find('input[type=file]').trigger('click');
}
function display_img(event)
{
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = $(this).parents('.thumbnail').first().next('.thumb-holder').find('.preview').first();
    $(preview).attr('src', src);
    $(this).parents('.thumbnail').first().next('.thumb-holder').show();
   }
}
function delete_elem()
{
  var currItem = $(this).parents('.formset-item');
  /*var count_not_hidden = $('.formset-item:not(.hidden-formset-item)').length;
  if(count_not_hidden == 1)
  {
    return;
  }*/
  $(currItem).find('input[type=checkbox]').prop('checked', true);
  $(currItem).addClass('hidden-formset-item');
  $(currItem).hide();
  var count_not_hidden = $('.formset-item:not(.hidden-formset-item)').length;
  if(count_not_hidden == 0)
  {
    $(currItem).find('.more-button').trigger('click');
  }
}
function clone_elem()
{
  var item_to_clone = $(this).parents('.formset-item').first();
  var service = String($(item_to_clone).attr('service'));
  cloneMore($(item_to_clone).parents('.formset-papa').find('.formset-item').last(), service);
}
function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();

    newElement.find(':input').each(function() {
      try
      {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        //$(this).attr({'name': name, 'id': id}).removeAttr('checked');
      }
      catch(ex)
      {
        console.log(ex)
        return true
      }
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });

    total++;
    $(newElement).removeClass('hidden-formset-item');
    $(newElement).show();
    $(newElement).find('img').attr('src', '');
    $(newElement).find('.more-button').unbind('click');
    $(newElement).find('.more-button').on('click', clone_elem);
    $(newElement).find('.delete-button').unbind('click');
    $(newElement).find('.delete-button').on('click', delete_elem);
    $(newElement).find('.trigger-upload').unbind('click');
    $(newElement).find('.trigger-upload').on('click', trigger_upload);
    $(newElement).find('input[type=file]').unbind('change');
    $(newElement).find('input[type=file]').on('change', display_img);
    $('#id_' + type + '-TOTAL_FORMS').val(total);
     $(selector).after(newElement);
}