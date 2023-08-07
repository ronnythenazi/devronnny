
$('.ronny-style-field').focusin(function(){
  $(this).addClass('chat-input-activate');
});

$('.ronny-style-field').focusout(function(){
  $(this).removeClass('chat-input-activate');
});




$(function() {
  $( "#chat-send-btn" ).click(function() {
    $( "#chat-send-btn" ).addClass( "onclic", 250, validate);
  });

  function validate() {
    setTimeout(function() {
      $( "#chat-send-btn" ).removeClass( "onclic" );
      $( "#chat-send-btn" ).addClass( /"validate", 450, callback );
    }, 2250 );
  }
    function callback() {
      setTimeout(function() {
        $( "#chat-send-btn" ).removeClass( "validate" );
      }, 1250 );
    }
  });
