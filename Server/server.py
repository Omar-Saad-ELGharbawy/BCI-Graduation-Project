import socket
import threading

# Define the host and port on which the server will listen
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 65432      # Port to listen on (non-privileged ports are > 1023)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            # Receive data from the client (1024 bytes)
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            # Send a response back to the client
            conn.sendall(b'MASTER: STATE;  1')
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed")

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections (5 is the maximum number of queued connections)
    s.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    
    while True:
        # Wait for a connection
        conn, addr = s.accept()
        # Handle the connection in a new thread
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
