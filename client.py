# Name: Chimara Okeke

import socket
import sys

# Get the hostname
hostname = socket.gethostname()

def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_port>")
        return

    server_port = int(sys.argv[1])

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        
        print( hostname, " python server.py", server_port)

        try:
            server_address = ('localhost', server_port)  # Server running locally

            # Send 10 'PING' messages
            for i in range(10):
                message = b'PING'
                client_socket.sendto(message, server_address)
                client_socket.settimeout(1)  # Set timeout to 1 second

                try:
                    # Wait for response
                    data, _ = client_socket.recvfrom(8008)
                    print( i+1, " : sent PING... received ", data.decode())
                except socket.timeout:
                    # Report timeout
                    print( i+1, " : sent PING... Timed Out")

        except KeyboardInterrupt:
            print("Client closed")

if __name__ == "__main__":
    main()
