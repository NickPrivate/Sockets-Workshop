import socket


def start_client():
    host = "127.0.0.1"  # Server's address
    port = 12345  # Server's port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        # Send a message to the server
        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == "exit":
            print("Connection closed by client.")
            break

        # Receive response from the server
        response = client_socket.recv(1024).decode()
        if not response or response.lower() == "exit":
            print("Connection closed by server.")
            break
        print(f"Server: {response}")

    # Close the socket
    client_socket.close()


if __name__ == "__main__":
    start_client()
