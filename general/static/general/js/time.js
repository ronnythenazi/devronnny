const translate_dict =
{
 'single':{'years':'שנה','months':'חודש','weeks': 'שבוע' , 'days':'יום', 'hours':'שעה', 'miniutes':'דקה'},
 'double':{'years':'שנתים','months':'חודשיים','weeks': 'שבועיים' , 'days':'יומיים', 'hours':'שעתיים', 'miniutes':'שתי דקות'},
 'plural':{'years':'שנים','months':'חודשים','weeks': 'שבועות' , 'days':'ימים', 'hours':'שעות', 'miniutes':'דקות'},
};

function get_friendly_time_format(time_dict)
{
  var unit = time_dict['unit'];
  var cnt  = time_dict['cnt'];
  lbl = "לפני ";
  if(cnt == 1)
  {
    lbl += translate_dict['single'][unit];

  }
  else if(cnt == 2)
  {
    lbl += translate_dict['double'][unit];
  }
  else if(cnt > 2)
  {
    lbl += cnt + ' ';
    lbl += translate_dict['plural'][unit];
  }
  else
  {
    return '';
  }
  return lbl;

}
