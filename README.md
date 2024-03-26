# Network-Programming

- This project uses **UDP** to communicate over the INET domain between a server and a client.
- In the client-server _Python_ program, `server.py` runs and waits for `client.py` to connect.
- If the connection is successful, `client.py` sends 10 ping messages and waits for `server.py` with a timeout.
- When receiving a 'PING', `server.py` responds with a 'PONG' 70% of the time and artificially "drops" the packet 30% of the time.
- If `server.py` times out, the time out is printed on the terminal. Otherwise, 'PONG' is printed on the screen.
- `server.py` waits infinitely for a message from `client.py`.


Some python functions used include: socket(), gethostname(), recvfrom(), sendto(), and SOCK_DGRAM

## _**Usage**_
- Change the directory to the location of `client.py` and `server.py` on your computer using `cd`
- Run server.py using: `python server.py 8008`
- Run client.py using: `python client.py 8008`
- **Ensure that server.py is run before client.py**
