# -*- encoding: utf-8 -*-
#Archivo principal main
from newton import *
from lector import *

#Creación de clase lector con la dirección del archivo a leer
lector = lector("holis.txt") 

#Creación de objeto newton
FuncionNewton = newton(lector.lee())

#Llamada a metodo Diferencia infinitas

FuncionNewton.DiferenciasFinitas()



