from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.cli import CLI

def create_topology():
    net = Mininet() 

    # Create router
    router = net.addHost('router', cls=Node) #create a host and it is converted to router
 
    # Create hosts in network 1
    host1 = net.addHost('host1', ip='10.0.0.2/24') #create host1 in 10.0.0.0 network

    # Create hosts in network 2
    host2 = net.addHost('host2', ip='10.0.1.2/24') #create host2 in 10.0.1.2 network

    # Add links between router and hosts with IP addresses
    Link(host1, router, intfName2='router-eth0', params2={'ip': '10.0.0.1/24'}) # link between host1 and router
    Link(host2, router, intfName2='router-eth1', params2={'ip': '10.0.1.1/24'}) # link between host2 and router

    # Enable IP forwarding on the router
    router.cmd('sysctl net.ipv4.ip_forward=1') # make router to forward the packets

    # Start network
    net.start()

    # Add routes on host1 and host2 for each other's networks via router
    host1.cmd('ip route add 10.0.1.0/24 via 10.0.0.1') # add route table for host1
    host2.cmd('ip route add 10.0.0.0/24 via 10.0.1.1') # add route table for host2

    # Test connectivity using pingall
    net.pingAll() # just for checking connectivity

    # Start CLI for interactive testing
    CLI(net)

    # Stop network
    net.stop()

if __name__ == '__main__':
    create_topology()
