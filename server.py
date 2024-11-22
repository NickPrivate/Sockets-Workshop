import socket


def start_server():
    host = "127.0.0.1"  # Localhost
    port = 12345  # Port to listen on

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        # Receive message from the client
        message = conn.recv(1024).decode()
        if not message or message.lower() == "exit":
            print("Connection closed by client.")
            break
        print(f"Client: {message}")

        # Send a response to the client
        response = input("You: ")
        conn.send(response.encode())
        if response.lower() == "exit":
            print("Connection closed by server.")
            break

    # Close the connection
    conn.close()


if __name__ == "__main__":
    start_server()
