class Cloud:

	def __init__(self,datacenters):
		self.datacenters = datacenters;
		self.scores = [];	

	def calculate_scores(self):
		self.scores = [];
		for datacenter in self.datacenters:
			score = (datacenter.get_max_cpu() / float(datacenter.get_total_cpu())) + (datacenter.get_max_storage() / float(datacenter.get_total_storage()));
			self.scores.append(score);
			self.scores.sort();
			print(self.scores);
			