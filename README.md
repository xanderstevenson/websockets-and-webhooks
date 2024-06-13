# Websockets and Webhooks Demo

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
<br>

## Setup steps

**Step 1**: Clone this repo and cd into it

```bash
git clone https://github.com/xanderstevenson/websockets-and-webhooks.git
cd websockets-and-webhooks
```
<br>

**Step 2**: Activat the Python virtual environment

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
<br>

## WebSocket Demo


* To run the server and client, you will need Python 3.7 or higher

**Step 1**: Change directories into the **websockets** directory and install the dependencies

```bash
cd websockets
pip install -r requirements.txt
```
<br>

**Step 2**: Observe and run the server

- Open **python websocket_server.py** and observe it's contents. 

- Run the Server

```bash
python websocket_server.py
```
<br>

**Step 3**: Open a new terminal, observe the client, and run the client

- Open **websocket_client.py** and observe it's contents. 

- Run the Client

```bash
python websocket_client.py
```

You should see the following output: **Received from server: Echo: Hello, World!**
<br>
<br>

**Step 4**: Change the message the client will send

- Open **websocket_client.py** in your IDE and change line 8, inserting your own message. Don't forget to save it!
  
```
await websocket.send("<Insert your message here>")
```

- Send the new message to the server
  
```bash
python websocket_client.py
```

Your new message should now be displayed.


- Navigate back to the terminal where the **websocket server** is running and observe a log of all messages sent, e.g.

**Received message: Hello, World!**
<br>
**Received message: Hello, World!**
<br>
**Received message: I am good**
<br>
**Received message: Hello, World!**
<br>
**Received message: Hello, World!**
<br>
**Received message: Hello, World!**
<br>
**Received message: yo!**
<br>

- Leave the websocket server running.

  <br>

**Step 5**: Communicate through the websocket via a browser

- Open websocket_server.**html** and observe the HTML with JavaScript code.

- In the terminal where the websocket client was running previously (websocket server should still be running in another terminal window), run the HTTP server:

```bash
python -m http.server
```

> **Note:** If prompted, allow incoming network connections

- Navigate in your browser of choice to [http://localhost:8000/websocket_client.html](http://localhost:8000/websocket_client.html), enter a message of your choice and click "Send". The message should be Echoed in the browser.

- Navigate to the terminal where **websocket server** is running and you should see the messages you've sent through the browser, e.g.:

**Received message: ok** 
<br>
**Received message: Adrian is a genius**
<br>
**Received message: hahaha**
  
