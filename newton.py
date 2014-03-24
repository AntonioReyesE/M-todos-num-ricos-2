#Clase que implementa los métodos necesarios para solucionar por el método de Newton
class newton:
	#Matriz que recibe a partir de archivo leido
	matriz = [0][0]

	#Contructor de la clase que inicializa la matriz
	def __init__(self, matriz):
		matriz = matriz

	#Primera forma de calcular las diferencias finitas de la función tabular
	#Regresa el orden de la función
	def DiferenciasFinitas():
		igual = iguales() #Para la primera comparación
		y = matriz[0][1] #Obtenr el valor de la tabulación en y
		#Hasta que todos los valores del arreglo sean iguales
		while igual == true:
			i = 0
			j = 1
			resultado = [0]
			#Suma de los valores de y
			for x in xrange(0,len(y)):
				suma = y[i++] + y[j++]
				resultado.append(suma)
			igual = iguales(resultado)
			y = resultado

	
	#Función que identifica si todos los elementos de un arreglo son iguales
	def iguales(resultado):
		f = resultado[0]
		for x in xrange(0,len(resultado)):
			if resultado[x] != f:
				return False
			else:
				pass	
		return True
		
