class Dog:
	def _init_(self, name):
		self.name = name
		slef.energy = 5

def bark(self):
		print(self.name, “says woof”)

	def walk(self):
		if self.energy > 0:
			self.energy = self.energy -  1
			print(self.name, “went on walk. Energy:”, self.energy)
		else:
			print(self.name, “is too tired to walk”)
tim = Dog(“Tim”)
