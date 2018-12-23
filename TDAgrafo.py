import random

class Vertice(object):
	
	def __init__(self,ciudad, aeropuerto, lat, lng):
		self.ciudad= ciudad
		self.aeropuerto= aeropuerto
		self.lat= lat
		self.lng= lng
		self.dicc_ady= {}

	def agregar_adyacente(self, aeropuerto, tiempo, precio, num_vuelos):
		self.dicc_ady[aeropuerto]= [tiempo, precio, num_vuelos]
		
	def dar_ciudad(self):
		return self.ciudad
		
	def obtener_aeropuerto(self):
		return self.aeropuerto
	
	def dar_precio(self, aerpuerto):
		if aeropuerto in self.dicc_ady:
			info_vuelo= self.dicc_ady.get(aeropuerto)
			return info_vuelo[1]
		return None
		
	def dar_num_vuelos(self, aeropuerto):
		if aeropuerto in self.dicc_ady:
			info_vuelo= self.dicc_ady.get(aeropuerto)
			return info_vuelo[2]
		return None
		
	def dar_tiempo(self, aeropuerto):
		if aeropuerto in self.dicc_ady:
			info_vuelo= self.dicc_ady.get(aeropuerto)
			return info_vuelo[0]
		return None
		
	def estan_conectados(self, aeropuerto):
		if aeropuerto in self.dicc_ady:
			return True
		return False
		
	def dar_adyacentes(self):
		return self.dicc_ady

class Grafo(object):
	
	def __init__(self):
		self.vertices= {}
		self.list_ciudad= []
		self.cantidad= 0
		
	# Descripcion: metodo usado por los metodos agregar vertices y aristas, verifica si el vertice existe.
	# Pre: Recibe el vertice.
	# Pos: Retorna verdadero en caso de existir, falso si no existe. 	
	def esta_en_vertices(self, aeropuerto):
		if aeropuerto in self.vertices:
			return True
		return False
	
	# Descripcion: Agrego un vertice.
	# Pre: Se recibe un vertice para agregar al conjunto de vertices.
	# Pos: Si el vertice ya existe, se retorna false, en caso contrario se agrega al conjunto de vertices
	# se aumenta la cantidad de vertices y se retorno true.	
	def agregar_vertices(self, ciudad, aeropuerto, lat, lng):
		if self.esta_en_vertices(aeropuerto):
			return False
		self.vertices[aeropuerto]= Vertice(ciudad, aeropuerto, lat, lng)
		self.list_ciudad.append(ciudad)
		self.cantidad += 1
		return True
		
	def agregar_arista(self, aeropuerto1, aeropuerto2, tiempo, precio, num_vuelos):
		self.vertices[aeropuerto1].agregar_adyacente(aeropuerto2, tiempo, precio, num_vuelos)
		self.vertices[aeropuerto2].agregar_adyacente(aeropuerto1, tiempo, precio, num_vuelos)
		return True
	
	def hay_conexion(self, aeropuerto1, aeropuerto2):
		return self.vertices[aeropuerto1].estan_conectados(aeropuerto2)
			
	def obtener_aeropuerto_ady(self, ciudad):
		lista_aero= []

		for clave, valor in self.vertices.items():
			if valor.dar_ciudad() == ciudad:
				lista_aero.append(clave)
		
		return lista_aero
	
	def obtener_aero_aleatorio_ciudad(self, ciudad):
		lista_aero= []

		for clave, valor in self.vertices.items():
			if valor.dar_ciudad() == ciudad:
				lista_aero.append(clave)
		
		return random.choice(lista_aero)
		
	def obtener_adyacentes(self, aeropuerto):
		return self.vertices[aeropuerto].dar_adyacentes().keys()
			
	def obtener_vertices(self):
		return self.vertices.keys()		
	
	def obtener_vertices_aleatorio(self):
		lista= []
		for v in self.vertices.keys():
			lista.append(v)
		return random.choice(lista)
	
	def obtener_tiempo(self, aeropuerto1, aeropuerto2):
		return self.vertices[aeropuerto1].dar_tiempo(aeropuerto2)
		
	def obtener_precio(self, aeropuerto1, aeropuerto2):
		return self.vertices[aeropuerto1].dar_precio(aeropuerto2)
		
	def obtener_num_vuelo(self, aeropuerto1, aeropuerto2):
		return self.vertices[aeropuerto1].dar_num_vuelos(aeropuerto2)
		
	def obterner_cantidad(self):
		return self.cantidad
		
	def obtener_ciudad(self, aeropuerto):
		return self.vertices[aeropuerto].dar_ciudad()
		
	def __iter__(self):
		return iter(self.vertices)
