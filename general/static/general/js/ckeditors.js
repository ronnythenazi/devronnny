function replace_html_in_ckeditor(find, replace_with, ck_name)
{
  var editor = CKEDITOR.instances[ck_name];
  var edata = editor.getData();
  var replaced_text = edata.replaceAll(find, replace_with);
  editor.setData(replaced_text);
}
function set_cke_body(s_body, ck_name)
{
  var editor = CKEDITOR.instances[ck_name];
  editor.setData(s_body);
}
/*$.fn.insertAtCaret = function (myValue, ck_name) {
    myValue = myValue.trim();
    CKEDITOR.instances[ck_name].insertHtml(myValue);
};*/

function get_pos_bookmark_className()
{
  return 'pos-bookmark';
}

function create_pos_bookmark()
{
  var bm_name = get_pos_bookmark_className();
  var bookmark = '<img width="0" height="0" src="nothing.jpg" alt="" class="'+ bm_name +'"> </img>';
  return bookmark;
}

function get_pos_bookmark_selector()
{
  return '.' + get_pos_bookmark_className();
}
/*function set_caret_pos(editor)
{
   var bm_selector = get_pos_bookmark_selector();
   editor.insertHtml(create_pos_bookmark());
   var x = $(bm_selector).offset().left;
   var y = $(bm_selector).offset().top;
   $('#caret-x').val(x);
   $('#caret-y').val(y);
   $(bm_selector).remove();
}*/

function get_ckeditor_selector(editor)
{
  var name = editor.name;
  name = name.replace('ck-reply-to-com', 'cke_ck-reply-to-com');
  name = name.replace('ck-reply-to-sub-com', 'cke_ck-reply-to-sub-com');
  name = name.replace('ck-edit-sub-com', 'cke_ck-edit-sub-com');
  name = name.replace('com-edit', 'cke_com-edit');
  name = name.replace('id_com-body', 'cke_id_com-body');
  selector = '#' + name + ' iframe';
  return selector;
}
function get_ckeditor_y(editor)
{
  var selector = get_ckeditor_selector(editor);
  return $(selector).offset().top;
}
function get_ckeditor_x(editor)
{
  var selector = get_ckeditor_selector(editor);
  return $(selector).offset().left;
}
function get_ckeditor_coords(editor)
{
  var selector = get_ckeditor_selector(editor);
  var y = $(selector).offset().top;
  var x = $(selector).offset().left;
  return {'x':x, 'y':y};
}
function getSelectionCoords(win)
{
    win = win || window;
    var doc = win.document;
    var sel = doc.selection, range, rects, rect;
    var x = 0, y = 0;
    if (sel) {
        if (sel.type != "Control") {
            range = sel.createRange();
            range.collapse(true);
            x = range.boundingLeft;
            y = range.boundingTop;
        }
    }
    else if (win.getSelection)
    {
        sel = win.getSelection();
        if (sel.rangeCount) {
            range = sel.getRangeAt(0).cloneRange();
            if (range.getClientRects)
            {
                range.collapse(true);
                rects = range.getClientRects();
                if (rects.length > 0) {
                    rect = rects[0];
                }
                x = rect.left;
                y = rect.top;
            }
            // Fall back to inserting a temporary element
            if (x == 0 && y == 0)
            {
                var span = doc.createElement("span");
                if (span.getClientRects) {
                    // Ensure span has dimensions and position by
                    // adding a zero-width space character
                    span.appendChild( doc.createTextNode("\u200b") );
                    range.insertNode(span);
                    rect = span.getClientRects()[0];
                    x = rect.left;
                    y = rect.top;
                    var spanParent = span.parentNode;
                    spanParent.removeChild(span);

                    // Glue any broken text nodes back together
                    spanParent.normalize();
                }
            }
        }
    }
    return { x: x, y: y };
}

function set_caret_pos(editor)
{

   var win = editor.window.$;
   var coords = getSelectionCoords(win);
   var x = coords['x'];
   var y = coords['y'];
   var  cke_coords = get_ckeditor_coords(editor);
   var cke_x = cke_coords['x'];
   var cke_y = cke_coords['y'];

// new
   $('#caret-x').val(cke_x + x);
   $('#caret-y').val(cke_y + y);
//end new

  /*  //normal com
   if(!editor.name.startsWith('id_'))
   {
     y =  cke_y + y;
     x =  cke_x + x;
     $('#caret-x').val(x);
     $('#caret-y').val(y);
     return;
   }
   //main com
   x = $(document).scrollLeft() +  cke_x + x + 350;
   y = $(document).scrollTop() + cke_y + y + 250;
   $('#caret-x').val(x);
   $('#caret-y').val(y);*/
}


/*CKEDITOR.on('instanceReady', function(evt) {
    var editor = evt.editor;
    editor.on('key', function(e) {
        set_caret_pos(editor);

    });
});*/

function auto_complete_enter_pressed(editor, prefix = '')
{
   var new_word = prefix + get_txt_of_selected_row();
   replace_word_at_caret(editor, new_word);
}

function replace_word_at_caret(editor, new_word)
{
   var curr_word = getWordBeforeCursor(editor);
   selectWordBeforeCursor(editor, curr_word);
   editor.insertText(new_word);
}

function selectWordBeforeCursor(editor, findString)
{
  var sel = editor.getSelection();
  var element = sel.getStartElement();
  sel.selectElement(element);
  var ranges = editor.getSelection().getRanges();
  var startIndex = element.getHtml().indexOf(findString);
   if (startIndex != -1)
   {
      ranges[0].setStart(element.getFirst(), startIndex);
      ranges[0].setEnd(element.getFirst(), startIndex + findString.length);
      sel.selectRanges([ranges[0]]);
   }
}

function getWordBeforeCursor(editor)
{
  var word = '';
  var chr = '';
  var pos = 1;
  while(chr!= ' ' && chr!= null)
  {
    var range = editor.getSelection().getRanges()[ 0 ],
        startNode = range.startContainer;

    if ( startNode.type == CKEDITOR.NODE_TEXT && range.startOffset )
    {
      // Range at the non-zero position of a text node.
      chr = startNode.getText()[ range.startOffset - pos ];
      pos += 1;
      if(chr == ' ' || chr == null || chr == undefined)
      {
         continue;
      }
      word += chr;
    }
    else
    {
      return reverseString(word);
    }
  }

  return reverseString(word);
}

function getPrevChar(editor, chrs_before = -1)
{
    var range = editor.getSelection().getRanges()[ 0 ],
        startNode = range.startContainer;

    if ( startNode.type == CKEDITOR.NODE_TEXT && range.startOffset )
    {
      // Range at the non-zero position of a text node.
      return startNode.getText()[ range.startOffset - 1 ];
    }

    else
    {
        // Expand the range to the beginning of editable.
        range.collapse( true );
        range.setStartAt( editor.editable(), CKEDITOR.POSITION_AFTER_START );

        // Let's use the walker to find the closes (previous) text node.
        var walker = new CKEDITOR.dom.walker( range ),node;


        while ( ( node = walker.previous() ) )
        {
            // If found, return the last character of the text node.
            if ( node.type == CKEDITOR.NODE_TEXT )
            {
              return node.getText().slice( -1 );
            }

        }
    }

    // Selection starts at the 0 index of the text node and/or there's no previous text node in contents.
    return null;
}
