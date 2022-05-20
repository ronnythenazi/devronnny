//$('.btnedit').click(editFrm)
//$('.btnCancel, .btnSave').click(cancelEdit);
$(document).ready(ready);

function ready()
{

   $('.hidden').hide();
   $('.post-output').each(function(){

    var status =  $(this).find('.publishstatus:first-child').text();
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



  $(ParentFrm).find('.btndelete').hide();
  $(ParentFrm).find('.btnedit').hide();
  $(ParentFrm).find('.btnCancel').show();
  $(ParentFrm).find('.btnSave').show();

  var PostOutput = $(ParentFrm).children('.post-output');
  $(PostOutput).hide();


}

function cancelEdit()
{

  var ParentFrm = $(this).parents('form').first();
  var editFrm = $(ParentFrm).children('.editfrm');
  $(editFrm).hide();


    $(ParentFrm).siblings().show();
    $(ParentFrm).parent().removeClass('widden')



  $(ParentFrm).find('.btndelete').show();
  $(ParentFrm).find('.btnedit').show();
  $(ParentFrm).find('.btnCancel').hide();
  $(ParentFrm).find('.btnSave').hide();

  //  $(ParentFrm).siblings().css('visibility', 'visible');
    var PostOutput = $(ParentFrm).children('.post-output');
    $(PostOutput).show();

}
