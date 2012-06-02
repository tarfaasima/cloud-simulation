from Cloud import Cloud;
from Datacenter import Datacenter;
from Server import Server;
from VM import VM;


vm1 = VM(3.0,40000);

server1 = Server(6.0,120000,[]);
server2 = Server(3,60000,[]);
server3 = Server(6,120000,[]);
server1.vms.append(vm1);

datacenter1 = Datacenter([server1]);
datacenter2 = Datacenter([server2,server3]);

cloud = Cloud([datacenter1,datacenter2]);

cloud.calculate_scores();