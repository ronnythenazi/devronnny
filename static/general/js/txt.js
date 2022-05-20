function get_tagged_username(word)
{
   if(word.charAt(0) != '@')
   {
     return '';
   }
   return word.substring(1);
}

function reverseString(str)
{
    return str.split("").reverse().join("");
}

function slice_str(str, end, start=0)
{
   return str.slice(start, end);
}

function strip_tags(str)
{
  return str.replace( /(<([^>]+)>)/ig, '');

}
