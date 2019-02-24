class Usuario():

	def __init__(self, nombre, pasword, edad):
		self.nombre=nombre
		self.pasword=pasword
		self.edad=edad

	def getInfo(self):
		print("Mi nombre es "+str(self.nombre) + " y tengo "+str(self.edad))

	def getNombre(self):
		return self.nombre

	def getPasword(self):
		return self.pasword

	def cuenta(self):
		pass