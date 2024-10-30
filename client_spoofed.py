from scapy.all import *

def send_tcp_packet():
    # Construct the packet with source and destination ports and some payload (data)
    packet = IP(ttl=64, src="10.0.0.3", dst="10.0.1.2") / TCP(sport=12345, dport=1229) / "Hello, TCP server!" # create a tcpc packet.this host is not present in the network.

    # Send the packet
    send(packet) #send the packet to server.

if __name__ == "__main__":
    send_tcp_packet()

