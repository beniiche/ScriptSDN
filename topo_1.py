from mininet.topo import Topo 
from mininet.cli import CLI 
from mininet.net import Mininet 
from mininet.link import TCLink 
from mininet.util import irange,dumpNodeConnections 
from mininet.log import setLogLevel 
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
 
class Test_Topo(Topo): #le nom de la topologie#
 
    "Test Topology"
    def __init__(self):
        "Create tree Topology"
        Topo.__init__(self) #initialise la topologie#

        #Add hosts #l’ajout des 4 hotes au topologie et assigne pour chaque hote, un nom, une adresse IP, et une adresse MAC#

        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1',mac='10:00:00:00:00:01', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', mac='10:00:00:00:00:02', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', mac='10:00:00:00:00:03', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', mac='10:00:00:00:00:04', defaultRoute=None)


        #Add switches #l’ajout de 8 switches#
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch, dpid='0000000000000001',protocols='OpenFlow13')
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch, dpid='0000000000000002',protocols='OpenFlow13')
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch, dpid='0000000000000003',protocols='OpenFlow13')
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch, dpid='0000000000000004',protocols='OpenFlow13')
        s5 = self.addSwitch('s5', cls=OVSKernelSwitch, dpid='0000000000000005',protocols='OpenFlow13')
        s6 = self.addSwitch('s6', cls=OVSKernelSwitch, dpid='0000000000000006',protocols='OpenFlow13')
        s7 = self.addSwitch('s7', cls=OVSKernelSwitch, dpid='0000000000000007',protocols='OpenFlow13')
        s8 = self.addSwitch('s8’, cls=OVSKernelSwitch, dpid='0000000000000008’,protocols='OpenFlow13')
      
        #Add links #l’ajout des liens entre les différents nodes (switches et notes), en spécifiant les numéros de ports, la bande passante et le délai pour chaque lien#
        self.addLink(s1, s2, port1=1, bw=10, delay=‘12ms’)
        self.addLink(s1, s3, port1=2, bw=10, delay=‘3ms')
	self.addLink(s1, s6, port1=3, bw=10, delay=‘5ms')
	self.addLink(s1, h1, port1=4, bw=10, delay=‘5ms')
	self.addLink(s1, h2, port1=5, bw=10, delay=‘4ms')
	self.addLink(s2, s8, port1=2, bw=10, delay=‘4ms')
	self.addLink(s8, h3, port1=2, bw=10, delay=‘6ms')
	self.addLink(s8, h4, port1=3, bw=10, delay=‘3ms')
	self.addLink(s3, s4, port1=2, bw=10, delay=‘6ms')
	self.addLink(s4, s5, port1=2, bw=10, delay=‘3ms')
	self.addLink(s5, s8, port1=2, bw=10, delay=‘2ms')
	self.addLink(s6, s7, port1=2, bw=10, delay=‘10ms')
	self.addLink(s7, s8, port1=2, bw=10, delay=‘1ms')


                    
topos = { 'test’: (lambda: Test_Topo() ) }

