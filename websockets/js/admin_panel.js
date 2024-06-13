const ws = new WebSocket('ws://localhost:6789/admin');

ws.addEventListener('message', function (event) {
    const data = JSON.parse(event.data);
    document.getElementById('connectedClients').textContent = data.connected_clients;
    document.getElementById('totalMessages').textContent = data.total_messages;
});

ws.addEventListener('open', function (event) {
    console.log('Connected to the WebSocket server.');
});

ws.addEventListener('close', function (event) {
    console.log('Disconnected from the WebSocket server.');
});

ws.addEventListener('error', function (event) {
    console.error('WebSocket error:', event);
});
