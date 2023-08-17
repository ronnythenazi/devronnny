const ws_arr = {};

$(document).ready(function(){

   if(!$('#curr-username-cn').length)
   {
     return;
   }
   connect_to_your_chat_rooms($('#curr-username-cn').val());
});

function load_chat_message(e, username, chatId, roomName)
{
   const data = JSON.parse(e.data);
   var msg = data['message'];
   var author = data['author'];
   if(author == username)
   {
     return;
   }
   open_chat(username, chatId, roomName);

   if(data['command'] == 'new_message')
   {
     $('.update_audio').first()[0].play();
   }


}


function connect_to_room(username, chatId, roomName)
{
  if(is_debug(window.location.host))
  {

    url = 'ws://'+window.location.host+'/ws/chat/'+ roomName + '/';



  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/chat/'+ roomName + '/';

  }

  ws_arr[roomName] = new WebSocket(url);
  ws_arr[roomName].onmessage  = function(e){load_chat_message(e, username, chatId, roomName);};


  ws_arr[roomName].onclose = function(){
    setTimeout(function() {
     connect_to_room(username, chatId, roomName);
        }, 1000);


    }
}
function connect_to_your_chat_rooms(username)
{

   var rooms = get_you_rooms_ajax(function(rooms){
      for(var i=0;i<rooms.length;i++)
      {
        var room = rooms[i];
        var roomName = room['roomName'];
        var chatId   = room['chatId'];
        connect_to_room(username, chatId, roomName);

      }
   });
}
