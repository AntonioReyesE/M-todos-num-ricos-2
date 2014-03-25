# -*- encoding: utf-8 -*-
#Archivo principal main
from newton import *
from Lector import *

menu = True;
print 'Hola, favor de introducir los comandos que desee:'
print 'para interpopación/extrapolación exacta, escribe "exacto"'
print 'para interpopación/extrapolación exacta, escribe "aproximado"'
print 'escribe "salir" para salir del programa'


while menu:


	opcion = raw_input(">>>")
	print opcion
	if opcion == 'exacto':
		print "exacto"
	elif opcion == 'aproximado':

    	#Creación de clase lector con la direscción del archivo a leer
		lector = Lector("holis.txt") 

		#Creación de objeto newton
		FuncionNewton = newton(lector.lee())
		xusuario = raw_input("introduce el valor a aproximar: ") 
		orden = int(raw_input("introduce el orden a aproximar (1,2,3...): "))
		#validar orden que no sea negativo
		while (orden<=0):
			orden = int(raw_input("vuelve a introducir el orden a aproximar (1,2,3...): "))
		print "orden escogido: " + str(orden)
		FuncionNewton.formula(float(xusuario),orden)
		FuncionNewton.kill()

	elif opcion == 'salir':
		menu = False;
	else:
		print "revisa la opción que escogiste"




