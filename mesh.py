from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def emptyNet():
	net = Mininet ( controller=RemoteController )
	info()
	net.addController( 'c0' , controller=RemoteController,ip="10.0.0.11",port=6633)
	info()
	net.addHost( 'h1' )
	net.addHost( 'h2' )
	info()
	s1 = net.addSwitch( 's1' )
	s2 = net.addSwitch( 's2' )
	s3 = net.addSwitch( 's3' )
	s4 = net.addSwitch( 's4' )
	info()
	net.addLink( h1, s1)
	net.addLink( h2, s3)
	SwitchList = (s1, s2, s3, s4)
	for index in range( 0, len(SwitchList)):
		for index2 in range( index+1 , len(SwitchList)):
			net.addLink(SwitchList[index] , Switchlist[index2])
	info()
	net.start()
	info()
	CLI( net )
	info()
	net.stop()
if __name__ == '__main__':
	setLogLevel( 'info' )
	emptyNet() 
