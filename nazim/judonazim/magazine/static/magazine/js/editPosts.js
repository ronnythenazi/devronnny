$('.btnedit').click(editFrm)


function editFrm()
{

  var ParentFrm = $(this).parents('form').first();
  var editFrm = $(ParentFrm).children('.editfrm');
  $(editFrm).show();
  var PostOutput = $(ParentFrm).children('.post-output');
  $(PostOutput).hide();

}
