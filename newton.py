# -*- encoding: utf-8 -*-
#Clase que implementa los métodos necesarios para solucionar por el método de Newton
class newton:

	k = 0  #El orden 
	lista = [] #La lista que guarda los valores iniciales y los generados a partir de ellos
	intervalo = 0 #La diferencia general entre los valores de x
	xAnterior = 0 #La x0 de la formula de Newton


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
				resta = float(y[j]) - float(y[i])
				i = i + 1
				j = j + 1
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
	
	#La primera función a llamar para hacer la validación principal
	#Función que detecta si h es constante, y si lo es regresa la distancia, sino regresa -1
	def intervalo(self):
		i = 0
		j = 1
		resta = abs(abs(float(self.matriz[0][j])) - abs(float(self.matriz[0][i])))
		while j < len(self.matriz[0]):
			resta2 = abs(abs(float(self.matriz[0][j])) - abs(float(self.matriz[0][i])))
			i = i + 1
			j = j + 1
			if(resta != resta2):
				self.intervalo = -1
				return -1
		self.intervalo = resta
		return resta
	
	#Función que calcula la k
	def fraccionIntervalo(self,x0):
		valor = float(self.matriz[0][0])
		if valor == x0:
			valor = x0
		elif x0 % self.intervalo == 0:
			valor = x0
		elif x0 > valor:
			while valor < x0:
				valor = valor + self.intervalo
			valor = valor - self.intervalo
		elif x0 < valor:
			while x0 < valor:
				valor = valor - self.intervalo
			valor = valor + self.intervalo
		fraccIn = (x0 - valor) / self.intervalo
		return fraccIn
