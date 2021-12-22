$('.btnedit').click(editFrm)
$('.btnCancel, .btnSave').click(cancelEdit);
$(document).ready(ready);

function ready()
{
   $('form').each(function(){
    var status =  $(this).find('select').val();
    if(status == 'public')
    {
         $(this).find('.public').show();
         $(this).find('.private').hide();
    }
    else if(status == 'private')
    {
      $(this).find('.public').hide();
      $(this).find('.private').show();
    }
   });

}
function editFrm()
{

  var ParentFrm = $(this).parents('form').first();
  var editFrm = $(ParentFrm).children('.editfrm');
  $(editFrm).show();


  $(ParentFrm).siblings().hide();

  $(ParentFrm).parent().addClass('widden');


  var PostOutput = $(ParentFrm).children('.post-output');
  $(PostOutput).hide();
  $(ParentFrm).find('.btndelete').hide();
  $(ParentFrm).find('.btnedit').hide();
  $(ParentFrm).find('.btnCancel').show();
  $(ParentFrm).find('.btnSave').show();


}

function cancelEdit()
{

  var ParentFrm = $(this).parents('form').first();
  var editFrm = $(ParentFrm).children('.editfrm');
  $(editFrm).hide();


    $(ParentFrm).siblings().show();
    $(ParentFrm).parent().removeClass('widden')


//  $(ParentFrm).siblings().css('visibility', 'visible');
  var PostOutput = $(ParentFrm).children('.post-output');
  $(PostOutput).show();
  $(ParentFrm).find('.btndelete').show();
  $(ParentFrm).find('.btnedit').show();
  $(ParentFrm).find('.btnCancel').hide();
  $(ParentFrm).find('.btnSave').hide();

}
