from mininet.topo import Topo
class MyTopo ( Topo ):
	def __init__( self ):
		Topo.__init__( self )
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )
		SwitchList = (s1, s2, s3, s4)
		for index in range ( 0, len(SwitchList)):
			for index2 in range ( index+1, len(SwitchList)):
				self.addLink( SwitchList[index], SwitchList[index2])
		self.addLink(h1, s1)
		self.addLink(h2, s2)
topos = { 'mytopo': ( lambda: MyTopo() ) }
