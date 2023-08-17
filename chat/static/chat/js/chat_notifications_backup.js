let ws;

const ws_arr = {};

$(document).ready(function(){

  var ntfs_roomName = get_your_room_notifications();

  connect_to_notification_room(ntfs_roomName, yours_room = true);
});

function load_chat_message(e, roomName)
{

   var data = JSON.parse(e.data);
   var chatId = data['chatId'];
   var roomName = data['roomName'];
   var username_login = $('#curr-username-cn').val();


   open_chat(username_login, chatId, roomName);


}

function get_room_notifications(username)
{
  // ntfs is acronym for notifications
  var ntfs_roomName = 'notifications' + username;
  return ntfs_roomName;
}
function get_your_room_notifications()
{
   //cn is acronym to Chat Notifications
   var username_login = $('#curr-username-cn').val();
   return get_room_notifications(username_login);

}

function connect_to_notification_room(roomName, yours_room = false, dict={}, key='')
{
  var url="";
  if(is_debug(window.location.host))
  {

    url = 'ws://'+window.location.host+'/ws/notifications/'+ roomName + '/';



  }
  else
  {
    url = 'wss://'+window.location.host+'/ws/notifications/'+ roomName + '/';

  }



  if(yours_room == true)
  {

    ws = new WebSocket(url);
    ws.onmessage =  function(e){
    load_chat_message(e, roomName);};
    ws.onclose = function(){
    setTimeout(function() {
      connect_to_notification_room(roomName);
          }, 1000);


      }


  }
  else
  {


    ws_arr[key] = new WebSocket(url);
    ws_arr[key].onopen  = function(){
    ws_arr[key].send(JSON.stringify(dict));};


    ws_arr[key].onclose = function(){
      setTimeout(function() {
       connect_to_notification_room(roomName);
          }, 1000);


      }

  }




}

function notify_participants(username, chatId, roomName, data, participants)
{

  var msg = data['message'];

  var author = msg['author'];
  var avatar = msg['avatar'];
  var name   = msg['name'];

  if(author != username)
  {

    return;
  }

  var command = 'notify_user';
  var notificationId = data['notificationId'];

  var content = msg['content']; //maybe msg.content



  for(var i=0;i<participants.length;i++)
  {
     var participant = participants[i]['username'];
     if(participant == username)
     {

       continue;
     }


     var participantNotificationroomName = get_room_notifications(participant);


     dict =  {
      'command':command,
      'chatId':chatId,
      'roomName':roomName,
      'author' :author,
      'avatar' :avatar,
      'name'   :name,
      'content':content,
      'notificationId': notificationId,

    };
     connect_to_notification_room(participantNotificationroomName, false, dict, participant);

      //socket.close();
  }






}
