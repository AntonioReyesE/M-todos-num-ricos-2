# -*- encoding: utf-8 -*-
#Clase que implementa los métodos necesarios para solucionar por el método de Lagrange
class Lagrange:
	matriz = []

	def __init__(self, matriz):
		self.matriz = matriz;
	#formula que calcula lagrange, recibe input de usuario	
	def formula(self, xuser):
		#print xuser
		result = 0
		
		
		for i in range (0, len(self.matriz[0])):
			num = 1
			den = 1
			for j in range(0, len(self.matriz[0])):
			
				if(j != i):
					num = num * (xuser - self.matriz[0][j] )
					den = den * (self.matriz[0][i] - self.matriz[0][j])
			num = num * self.matriz[1][i]
			#print num
			#print den
			#print num/den
			result = result + (num/den)
		
		print result
		return result

	def kill(self):
		del self
