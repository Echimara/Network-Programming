# Name: Chimara Okeke

import socket
import sys
import random


# Get the hostname
hostname = socket.gethostname()

def main():
    if len(sys.argv) != 2:
        print("Usage: python server.py <server_port>")
        return

    server_port = int(sys.argv[1])

    # Create a UDP socket and bind it to the hostname and port
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('localhost', server_port))  # Server running locally

        print( hostname, " python server.py", server_port)
        print("[server] : ready to accept data...")

        while True:
            # Wait for a message from the client
            data, client_address = server_socket.recvfrom(8008)
            message = data.decode()

            # print("Received:", message, "from", client_address)

            # Simulate dropping packets 30% of the time
            if random.random() < 0.3:
                print("[server] : packet dropped")
            else:
                # Respond back with 'PONG' 70% of the time
                if message == 'PING' and random.random() < 0.7:
                    server_socket.sendto(b'PONG', client_address)
                    print("[client] : PING")

if __name__ == "__main__":
    main()
