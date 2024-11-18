import socket

def start_server():
    # Create a socket object using IPv4 and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name (hostname)
    host = socket.gethostname()
    port = 1234

    # Bind to the host and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Establish connection with client
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        
        # Send a message to the client
        message = 'Thank you for connecting! connection established and succesfull!'
        client_socket.send(message.encode('utf-8'))

        # Close the connection with the client
        client_socket.close()

# Run the server function
if __name__ == '__main__':
    start_server()
