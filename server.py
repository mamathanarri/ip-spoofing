from scapy.all import *

def icmp_echo_request(destination_ip, ttl):
    icmp_packet = IP(dst=destination_ip) / ICMP(type=8, code=0) #create icmp request packet with recieved ip address and type = 8 for echo request
    
    reply = sr1(icmp_packet) #send the packet
    
    if reply and ICMP in reply and reply[ICMP].type == 0:  # ICMP Echo Reply type = 0 for echo reply.
        print("Received ICMP Echo Reply:") 
        print(reply.summary()) # summary of the reply received from client
        print(reply.ttl) # recieved ttl
        if reply.ttl == ttl: #compare with recieved ttl and the ttl already extracted at initial client request
            print("packet is not spoofed")
        else:
            print("packet is spoofed")    	
    elif reply and ICMP in reply and reply[ICMP].type == 3:  # Destination Unreachable
        print("Received Destination Unreachable Message:") 
        print(reply.summary()) 
        print("packet is spoofed") #packet is spoofed if no reply is destination unreachable
    else:
        print("No ICMP Echo Reply received.")


def tcp_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) as server_socket: #create a tcp raw socket
        server_socket.bind((host, port))  #bind ip address and port number.
        print(f"Server listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(4096) # recieve the data from client
            print(f"Received {len(data)} bytes from {client_address}")
            
            ttl = data[8]  #extract the ttl from the data received
            print(f"TTL: {ttl}")
            
            icmp_echo_request(client_address[0], ttl) # send the 

if __name__ == "__main__": #program starts from here
    server_host = '10.0.1.2' # ip address of the server 
    server_port = 1229  #service is running on port number 1229.
    tcp_server(server_host, server_port) #method to create socket and send icmp request.
