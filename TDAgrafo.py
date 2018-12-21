class Vertice:
	
	def __init__(self, nombre, arista):
		self.nombre= nombre
		self.dicc_ady= {}
		
	def agregar_adyacente(self, nombre, arista):
		self.dicc_ady[nombre]= arista
		
	def adyacente(self):
		return self.dicc_ady
	
class Grafo(object):
	
	def __init__(self):
		self.vertices= {}
		self.cantidad= 0
		
	# Descripcion: metodo usado por los metodos agregar vertices y aristas, verifica si el vertice existe.
	# Pre: Recibe el vertice.
	# Pos: Retorna verdadero en caso de existir, falso si no existe. 	
	def esta_en_vertices(self, nombre):
		if nombre in self.vertices:
			return True
		return False
	
	# Descripcion: Agrego un vertice.
	# Pre: Se recibe un vertice para agregar al conjunto de vertices.
	# Pos: Si el vertice ya existe, se retorna false, en caso contrario se agrega al conjunto de vertices
	# se aumenta la cantidad de vertices y se retorno true.	
	def agregar_vertices(self, nombre):
		if self.esta_en_vertices(nombre):
			return False
		self.vertices[nombre]= Vertice(nombre)
		self.cantidad +=1
		return True
		
	def agregar_arista(self, inicio, fin, peso=0):
		if not(self.esta_en_vertices(inicio)) or not (self.esta_en_vertices(fin)) and not hay_arista(inicio, fin):
			return False
		
		self.vertices[inicio].agregar_adyacente(nombre, peso)
		self.vertices[fin].agregar_adyacente(fin, peso)
		return True
	
	def hay_arista(self, nombre1, nombre2):
		ady_nombre1= self.vertices[nombre1].dicc_ady
		if nombre2 in ady_nombre1:
			return True
		return False
			
	def obtener_adyacentes(self, nombre):
		lista_ady= []
		
		if not self.esta_en_vertices(nombre):
			return None
			
		ady_nombre= self.vertices[nombre].dicc_ady
		
		for w in ady_nombre:
			lista_ady.append(w)
		return lista_ady
	
	def peso_union(self, inicio, fin):
		if not self.hay_arista(inicio, fin):
			return -1
		return self.vertices[inicio].dicc_ady[fin]
			
	def cantidad_vertices(self):
		return self.cantidad
		
	def obtener_vertices(self):
		return self.vertices.keys()		
