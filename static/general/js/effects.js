function create_fan_loader()
{
  if($('.curve-stick-item').length > 0)
  {
    return;
  }
  var child = get_fan_half_circ_child();
  $('#animated-fan').append(child);
  for(var i=1;i<4;i++)
  {
    child = get_fan_half_circ_child(i);
    $('#animated-fan .curve-stick-item').last().append(child);
  }
}

function get_fan_half_circ_child(index=0)
{
  var fan_stick = '<div class="curve-stick-item ';
  if(index % 2 == 0)
  {
    fan_stick += 'curve-stick-item-right';
  }
  else
  {
    fan_stick += 'curve-stick-item-left';
  }
  fan_stick += '">';
  fan_stick += '</div>';
  return fan_stick;
}
