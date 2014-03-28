# -*- encoding: utf-8 -*-
#Archivo principal main
from newton import *
from Lector import *
from Lagrange import *

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

menu = True;
print ' Hola, favor de introducir los comandos que desee:'
print ' Para interpopacion/extrapolacion exacta, escribe --> "1"'
print ' Para interpopacion/extrapolacion aproximada, escribe --> "2"'
print ' Escribe "salir" para salir del programa'
print ""

#Creación de clase lector con la direscción del archivo a leer
lector = Lector("datos.txt") 
#Creación de objeto newton
FuncionNewton = newton(lector.lee())
FuncionLagrange = Lagrange(lector.lee())
#validar entrada para ver si se puede ejecutar newton

#print str(validarNewton)
while menu:


	opcion = raw_input(">>>")
	
	if opcion == '1':
		inpu = (raw_input("introduce el valor a calcular: "))
		if is_number(inpu):

			FuncionLagrange.formula(float(inpu))
		else:
			print "Valor incompatible"
		FuncionLagrange.kill()
	elif opcion == '2':
		if FuncionNewton.DiferenciasFinitas() != -1:
			xusuario = raw_input("introduce el valor a aproximar: ") 
			orden = int(raw_input("introduce el orden a aproximar (1,2,3...): "))
			#validar orden que no sea negativo
			while (orden<=0):
				orden = int(raw_input("vuelve a introducir el orden a aproximar (1,2,3...): "))
			print "orden escogido: " + str(orden)
			FuncionNewton.formula(float(xusuario),orden)
			
		else:
			print " Los valores de entrada no son constantes, no se puede extrapolar/interpolar por newton"
		FuncionNewton.kill()
	elif opcion == 'salir':
		menu = False;
		print " Adios..."
	else:
		print "revisa la opción que escogiste"
	if menu:
		print ""
		print ("****************************************************************")
		print ""
		print ' Para interpopacion/extrapolacion exacta, escribe --> "1"'
		print ' Para interpopacion/extrapolacion aproximada, escribe --> "2"'
		print ' Escribe "salir" para salir del programa'



