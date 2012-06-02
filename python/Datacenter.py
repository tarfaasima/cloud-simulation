from Server import Server;

class Datacenter:

	def __init__ (self,servers):
		self.servers = servers;

	def get_max_cpu(self):
		max = 0;
		for server in self.servers:
			if server.cpu > max:
				max = server.cpu;
		return max;

	def get_total_cpu(self):
		total_cpu = 0;
		for server in self.servers:
			total_cpu += server.total_cpu;
		return total_cpu;

	def get_max_storage(self):
		max = 0;
		for server in self.servers:
			if server.storage > max:
				max = server.storage;
		return max;

	def get_total_storage(self):
		total_storage=0;
		for server in self.servers:
			total_storage += server.total_storage; 
		return total_storage;



	