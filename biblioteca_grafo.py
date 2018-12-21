from TDAgrafo import Grafo
import heapq
from collections import deque

def bfs(grafo, origen):
	visitados= set()
	padres= {}
	orden= {}
	cola= deque()
	
	visitados.add(origen)
	orden[origen]= 0
	padres[origen]= None
	cola.append(origen)
	
	while cola:
		vertice= cola.popleft()
		
		for w in grafo.obtener_adyacentes(vertice):
			if w not in visitados:
				visitados.add(w)
				padre[w]= vertice
				orden[w]= orden[vertice] + 1
				cola.append(w)
	
	return padre, orden

def recorrido_dfs(grafo, origen):
	visitados= set()
	padres= {}
	orden= {}
	padres[origen]= None
	orden[origen]= 0
	dfs(grafo, origen, visitados, padres, orden)
	return padres, orden
	

def dfs(grafo, vertice, visitados, padres, orden):
	visitados.add(vertice)
	
	for w in grafo.obtener_adyancentes(vertice):
		if w not in visitados:
			padres[w]= vertice
			orden[w]= orden[vertice]+1
			dfs(grafo, w, visitados, padres, orden);
			
def orden_topologico(grafo):
	grado= {}
	cola= deque()
	result= []
	
	for vertice in grafo.obtener_vertices(): 
		grado[vertice]= 0
	
	for v in grafo.obtener_vertices():
		for w in grafo.obtener_adyacentes(v):
			grado[w] += 1
			
	for x in grado:
		if grado[x] == 0:
			cola.append(x)
			
	while cola:
		v= cola.popleft()
		result.append(v)
		
		for w in grafo.obtener_adyacentes(v):
			grado[w] -= 1
			if grado[w] == 0:
				cola.append(w)
				
	return result
			
def camino_minimo(grafo, origen):
	dist= {}
	padres= {}
	heap_min= []
	
	for v in grafo: dist[v] = 99999
	
	dist[origen]= 0
	padres[origen]= None
	heapq.heappush(heap_min, [origen, dist[origen]])
	
	while heap_min:
		(vertice, distancia)= heapq.heappop(heap_min)
		
		for w in grafo.obtener_adyacentes(vertice):
			if dist[vertice] + grafo.peso_union(vertice, w) < dist[w]:
				dist[w]= dist[vertice] + grafo.peso_union(vertice, w)
				padres[w]= vertice
				heapq.heappush(heap_min, [w, dist[w]])
				
	return padres, dist	
 
def prim(grafo, origen):
	visitados= set()
	heap_min= []
	arbol_de_tendido_min= Grafo()
	
	visitados.add(origen)
	
	for w in grafo.obtener_adyacentes(origen):
		distancia= grafo.peso_union(origen, w)
		heapq.heappush(heap_min, [origen, w, distancia])
	
	for vertice in grafo.obtener_vertices():
		arbol.agregar_vertices(vertice)
	
	while heap_min:
		(vertice, adyacente, distancia)= heapq.heappop(heap_min)
		
		if adyacente in visitados: continue
	
		arbol_de_tendido_min.agregar_arista(vertice, adyacente, distancia)
		visitados.add(adyacente)
		
		for x in grafo.obtener_adyacentes(adyacente):
			if x not in visitados:
				heapq.heappush(heap_min, [adyacente, x, grafo.peso_union(adyacente, x)])
	
	return arbol_de_tendido_min
