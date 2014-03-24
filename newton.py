# -*- encoding: utf-8 -*-
#Clase que implementa los métodos necesarios para solucionar por el método de Newton
class newton:

	k = 0  #El orden 
	lista = []

	#Contructor de la clase que inicializa la matriz
	def __init__(self, matriz):
		#Matriz que recibe a partir de archivo leido
		self.matriz = matriz

	#Primera forma de calcular las diferencias finitas de la función tabular
	#Regresa el orden de la función
	def DiferenciasFinitas(self):
		lista = []
		y = self.matriz[1] #Obtenr el valor de la tabulación en y
		lista.append(self.matriz[0])
		lista.append(y)
		igual = self.iguales(y) #Para la primera comparación
		#Hasta que todos los valores del arreglo sean iguales
		k = 0
		while igual != True:
			k = k + 1
			i = 0
			j = 1
			resultado = []
			#resta de los valores de y
			while j < len(y):
				resta = int(y[j]) - int(y[i])
				i=i+1
				j=j+1
				resultado.append(resta)
			igual = self.iguales(resultado)
			y = resultado
			lista.append(resultado)
		self.k = k
		self.lista = lista

	
	#Función que identifica si todos los elementos de un arreglo son iguales
	def iguales(self,resultado):
		f = resultado[0]
		for x in xrange(0,len(resultado)):
			if resultado[x] != f:
				return False	
		return True
		
