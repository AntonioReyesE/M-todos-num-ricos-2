#Clase encargada de leer y acomodar los valores del archivo de entrada
class lector():
	"""docstring for lector"""
	path = ""
	def __init__(self, path):
		self.path = path

	def lee(self):
		f = open("holis.txt", "r")
		x = f.readline()
		x = x.rstrip("\n")
		Ax = x.split(",")
		y = f.readline()
		y = y.rstrip("\n")
		Ay = y.split(",")
		R = (Ax,Ay)
		return R

