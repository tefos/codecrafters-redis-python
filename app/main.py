# Uncomment this to pass the first stage
import socket
import threading

def respond_to_ping(socket: socket.socket):
    try:
        while(socket.recv(1024)):
            socket.send(b'+PONG\r\n')
    except (ConnectionResetError, BrokenPipeError) as e:
        pass
    socket.close()

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client_socket, _ = server_socket.accept() # wait for client
        client_thread = threading.Thread(target=respond_to_ping, args=(client_socket,), daemon=True)
        client_thread.start()


if __name__ == "__main__":
    main()
