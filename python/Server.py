from VM import VM;

class Server:

	def __init__ (self,cpu,storage,vms):
		self.cpu = cpu;
		self.total_cpu = cpu;
		self.storage = storage;
		self.total_storage = storage
		self.vms = vms;


	def allocate_cpu(self,vm,cpu):
		if self.cpu >= cpu:
			vm.cpu = cpu;
			self.cpu -= cpu;
			return True;
		return False;

	def allocate_storage(self,vm,storage):
		if self.storage >= storage:
			vm.storage = storage;
			self.storage -= storage;
			return True;
		return False;

	def create_vm(self,cpu,storage):
		if self.cpu >= cpu and self.storage >= storage:
			vm = VM(cpu,storage);
			self.cpu -= cpu;
			self.storage -= storage;
			self.vms.append(vm);
			return True;
		return False;

	def destroy_vm(self,vm):
		self.cpu += vm.cpu;
		self.storage += storage;
		self.vms.remove(vm);
		return True;
		
