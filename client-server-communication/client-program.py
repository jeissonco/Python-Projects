import socket

def connect_to_server():
    # Create a socket object using IPv4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 1234

    # Connection to hostname on the port
    client_socket.connect((host, port))

    # Receive no more than 1024 bytes
    message = client_socket.recv(1024)

    print(f"Received from server: {message.decode('utf-8')}")

    # Close the connection
    client_socket.close()

# Run the client function
if __name__ == '__main__':
    connect_to_server()
