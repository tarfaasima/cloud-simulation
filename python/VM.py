class VM:

	def __init__ (self,cpu,storage):
		self.cpu = cpu;
		self.storage = storage;

	def deallocate(self):
		del self;