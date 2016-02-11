# -*-coding:Utf-8 -*

class Character:
	'''Just a character'''
	
	pass
	
	
class Living(Character):
	'''Just alive'''
	
	def __init__(self, mediclorian):
		self.med = mediclorian
		

class Unliving(Character):
	'''Not alive'''
	
	def __init__(self):
		pass
		

class Wookie(Living):
	'''Grrrrr'''
	
	pass
		
		
class Droide(Unliving):
	'''Just Droide'''
	
	pass
	
	
class Master_of_the_force_of_the_death_unbelievable(Living):
	'''Yeah'''
	
	def __init__(self, med, balance):
		self.title = None
		self._balance = 0
		
		def getBalance(self):
			return self._balance
		def setBalance(self, balance):
			if balance < -1 or balance > 1:
				raise ValueError('Balance value must be in [-1, 1]')
				
			self._balance = balance
			if self._balance == 0:
				self.title = 'neutre'
			elif self._balance < 0:
				self.title = 'sith'
			else:
				self.title = 'jedi'

		self.balance = property(getBalance, setBalance)
		setBalance(self, balance)
	
		Living.__init__(self, med)

		
		

if __name__ == '__main__':
	chewbacca = Wookie(0.15)
	try:
		m = Master_of_the_force_of_the_death_unbelievable(2, 3)
	except ValueError as e:
		
	