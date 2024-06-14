# Websockets and Webhooks Demo

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
<br>

## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone this repo and cd into it

```bash
git clone https://github.com/xanderstevenson/websockets-and-webhooks.git
cd websockets-and-webhooks
```
<br>

### **Step 2**: Create and activate a Python virtual environment

- Mac/Linux
```bash
python3 -m venv venv
source venv/bin activate
```
- Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```

> **Note:** Optional: In VS Code you can open all files in this repo with this command
```bash
code .
```
> **Note:** You'll then see the file manager on the left-hand side. Simply choose **Terminal > New Terminal** from the VS Code menu to pen a new Terminal.
<br>

## WebSocket Demo

### **Step 1**: Change directories into the **websockets** directory and install the dependencies

```bash
cd websockets
pip install -r requirements.txt
```
<br>

### **Step 2**: Observe and run the server

- Open **python websocket_server.py** and observe it's contents. 

- Run the Server

```bash
python3 websocket_server.py
```
<br>

### **Step 3**: Open a new terminal, observe the client, and run the client

- Open **websocket_client.py** and observe it's contents. 

- Run the Client

```bash
python3 websocket_client.py
```

You should see the following output: **Received from server: Echo: Hello, World!**
<br>
<br>

### **Step 4**: Change the message the client will send

- Open **websocket_client.py** in your IDE and change line 8, inserting your own message. Don't forget to save it!
  
```
await websocket.send("<Insert your message here>")
```

- Send the new message to the server
  
```bash
python3 websocket_client.py
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

### **Step 5**: Communicate through the websocket via a browser

- Open websocket_server.**html** and observe the HTML with JavaScript code.

- In the terminal where the websocket client was running previously (websocket server should still be running in another terminal window), run the HTTP server:

```bash
python3 -m http.server
```

> **Note:** If prompted, allow incoming network connections

- Navigate in your browser of choice to [http://localhost:8000/websocket_client.html](http://localhost:8000/websocket_client.html), enter a message of your choice and click "Send". The message should be Echoed in the browser.

- Navigate to the terminal where **websocket server** is running and you should see the messages you've sent through the browser, e.g.:

**Received message: ok** 
<br>
**Received message: Adrian is a genius**
<br>
**Received message: hahaha**

<br>

### **Step 6**: Monitor WebSocket activity using the Admin Panel

With the WebSocket server running in one terminal (python3 websocket_server.py) and the HTTP server running in the other (python3 -m http.server), you can now use the Admin Panel to monitor client connections and messages in real-time.

- Prepare the Admin Panel: open the *admin_panel.html**, **js/admin_panel.js**, and **styles/admin_panel.css** files are in the IDE.

- Access the Admin Panel: Open your web browser and navigate to [http://localhost:8000/admin_panel.html](http://localhost:8000/admin_panel.html)

- Interact with the Admin Panel: Use the "Show Clients" and "Show Messages" buttons to view the list of connected WebSocket clients and the history of messages exchanged. The Admin Panel will automatically update the statistics as new clients connect and messages are sent via the WebSocket Client at [http://localhost:8000/websocket_client.html](http://localhost:8000/websocket_client.html)

- Observe Server Activity: As you interact with the Admin Panel, observe the terminal where the WebSocket server is running. You should see logs indicating that the server is processing requests from the Admin Panel, such as fetching the list of clients or retrieving message history.


