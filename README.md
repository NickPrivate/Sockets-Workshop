## TCP Chat Program

This project demonstrates a simple TCP server and client implementation in Python. The server and client can exchange messages back and forth until either party sends `exit` to terminate the connection.

### Features
- Server listens for a single client connection.
- Messages can be sent back and forth between server and client.
- Clean termination of connection when `exit` is sent by either side.

---

### Prerequisites

- **Python Version**: 3.6 or higher
- Works on Linux, macOS, and Windows.

---

### Setup Instructions

### Step 1: Clone or Download the Project
Clone this repository or download the files `server.py` and `client.py` into your desired directory.

```
git clone https://github.com/NickPrivate/Sockets-Workshop.git
cd Sockets-Workshop
```
## Step 2: Verify Python Installation
Make sure Python 3.6 or higher is installed. Check the version by running:
```
python3 --version
```
[Download Python 3](https://www.python.org/downloads/)

## Step 3: Run the Server
Open a terminal or command prompt.

Start the server by running:

```
python3 server.py
```
The server will start and listen for incoming client connections on 127.0.0.1:12345.

## Step 4: Run the Client
Open another terminal or command prompt.

Start the client by running:

```
python3 client.py
```
The client will connect to the server at 127.0.0.1:12345.
