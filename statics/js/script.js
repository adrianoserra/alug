
   window.onload = function() {

const user_username = JSON.parse(document.getElementById('user_username').textContent);

const roomName = JSON.parse(document.getElementById('room-name').textContent);


    document.querySelector('#submit').onclick = function(e){
        const messageInputDom = document.querySelector('#mensagem');
        const identificador = document.querySelector('#identificador');
        const user_username = identificador.value
        const message = messageInputDom.value;

        chatSocket.send(JSON.stringify({
            'message': message,
            'username': user_username,
        }));

    };




const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
);

mensagem
chatSocket.onmessage = function(e){
    const data = JSON.parse(e.data);

    document.querySelector('#chat-text').value += (data.username +': ' + data.message + '\n')


}


}
