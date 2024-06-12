# websockets-and-webhooks

## Setup steps

Step 1: Clone this repo and cd into it

```bash
git clone https://github.com/xanderstevenson/websockets-and-webhooks.git
cd websockets-and-webhooks
```
<br>

Step 2: Activat the Python virtual environment

- Mac/Linux
```bash
source venv/bin activate
```
- Windows
```bash
venv\Scripts\activate
```

> **Note:** Optional: In VS Code you can open all files in this repo with this command
```bash
code .
```


## WebSocket Demo


* To run the server and client, you will need Python 3.7 or higher

Step 1: Change directories into websockets and install the dependencies

```bash
cd websockets
pip install -r requirements.txt
```

Step 2: Observe and run the server

- Open [python websocket_server.py](https://github.com/xanderstevenson/websockets-and-webhooks/blob/main/websockets/websocket_server.py) and observe it's contents. 

- Run the Server

```bash
python websocket_server.py
```

Step 3: Open a new terminal, observe the client, and run the client

- Open [websocket_client.py](https://github.com/xanderstevenson/websockets-and-webhooks/blob/main/websockets/websocket_client.py) and observe it's contents. 

- Run the Server

```bash
python websocket_client.py
```

You should see the following output: **Received from server: Echo: Hello, World!**

