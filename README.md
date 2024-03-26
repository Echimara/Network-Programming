# Network-Programming

This project uses two simple U
You will create a simple client server program with a language of your choice (Python is recommended) where a server is running and a client connects, sends a ping message, the server responds with a pong message or drops the packet.
You can have this program run on your machine or on the cse machines. Note that you will run two instances of your shell / IDE / whatever and they will communicate locally (though over the INET domain) - you can connect to your localhost (127.0.0.1 or make use of the gethostname() function in Python). 
Use UDP (SOCK_DGRAM) sockets for this assignment (parameter passed to socket()).

useful links:

Python socket libraryLinks to an external site. (probably use: socket(), bind(), gethostname(), recvfrom(), sendto(), SOCK_DGRAM, and AF_INET)

Python docs exampleLinks to an external site.

Details
client.py

Create a UDP socket (hostname and port are command line arguments).
Send 10 (probably in a loop) 'PING' message (hint: messages are bytes objectsLinks to an external site.).
Wait for the response back from the server for each with a timeout (see settimeout()Links to an external site.).
If the server times out, report that to the console, otherwise report the 'PONG' message received.
server.py

Create a UDP socket and bind it to the hostname of your machine and the same port as the client using command line args (or ENV vars).
Infinitely wait for a message from the client.
When receiving a 'PING', respond back with a 'PONG' 70% of the time and artificially "drop" the packet 30% of the time (just don't send anything back).
Hint: for the dropping of packets, use random number generationLinks to an external site. 
Server should report each ping message and each dropped packet to the console (just print it
