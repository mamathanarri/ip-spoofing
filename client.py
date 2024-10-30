from scapy.all import *

def send_tcp_packet():
    # Construct the packet with source and destination ports and some payload (data)
    packet = IP(ttl=64, src="10.0.0.2", dst="10.0.1.2") / TCP(sport=12345, dport=1229) / "Hello, TCP server!"

    # Send the packet
    send(packet)

if __name__ == "__main__":
    send_tcp_packet()

