function get_css_variable_val(css_var_name)
{
  var bodyStyles = window.getComputedStyle(document.body);
  var val = bodyStyles.getPropertyValue(css_var_name); //get
  return val;

}

function set_css_variable_val(css_var_name, new_val)
{
  var bodyStyles = window.getComputedStyle(document.body);
  var val = bodyStyles.getPropertyValue(css_var_name); //getvar bodyStyles = window.getComputedStyle(document.body);
  document.body.style.setProperty(css_var_name, new_val);//set
}

function is_elem_exists(selector)
{
  var count_items = $(selector).length;
  if(count_items <= 0)
  {
    return false;
  }
  return true;
}

function is_attr_exist(selector, name)
{
  var attr = $(selector).attr(name);
  if (typeof attr !== 'undefined' && attr !== false)
  {
      return true;
  }
  return false;
}

function is_elem_displayed(selector)
{
    var elem = $(selector);
    var displayed_status = $(elem).css('display');
    if(displayed_status == 'none')
    {
      return false;
    }
    return true;
}

function fadeInImg(id_name)
{
  $('#' + id_name).css('opacity', '1');
}
