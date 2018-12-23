from __future__ import print_function
from TDAgrafo import *
import heapq
from collections import deque
import math
	
def bfs(grafo, origen):
	visitados= {}
	padres= {}
	orden= {}
	cola= deque()
	
	visitados[origen]= origen
	orden[origen]= 0
	padres[origen]= None
	cola.append(origen)
	
	while cola:
		vertice= cola.popleft()
		
		for w in grafo.obtener_adyacentes(vertice):
			if w not in visitados:
				visitados[w]= w
				padre[w]= vertice
				orden[w]= orden[vertice] + 1
				cola.append(w)
	
	return padre, orden

def creo_recorrido(grafo, vertice, visitados, lista_rec, cont):
	if vertice in visitados and len(visitados) == cont and lista_rec[0] == vertice:
		lista_rec.append(vertice)
		return True
	return False

def dfs(grafo, vertice, visitados, lista_rec, cont, iteracion):
	
	if iteracion > cont: return False
	
	visitados[vertice]= vertice
	# Agrego a la lista la ciudad que visito
	lista_rec.append(vertice)
	
	for v in grafo.obtener_adyacentes(vertice):
		if creo_recorrido(grafo, v, visitados, lista_rec, cont):
			return True
	
		if v not in visitados:
			if dfs(grafo, v, visitados, lista_rec, cont, iteracion+1):
				return True
	
	del visitados[vertice]
	# Si no termina correctamente dejo la lista vacia 
	lista_rec.pop()
	return False
			
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
	
def imprimir_camino(camino):
	largo_camino= len(camino)
	
	for i in range(largo_camino):
		print("{} ->".format(camino[i]), end = "")
	#print(camino[-1])
	
def reconstruir_dist_camino(grafo, camino):
	dist_camino= 0
	largo= len(camino)
	
	for ciudad in range(0, largo):
		actual= camino[ciudad]
		proximo= camino[ciudad+1]
		dis_camino += grafo.peso_union(actual, proximo)
		
	return dist_camino
			
def reconstruir_camino(destino, padre):
	lista= []
	actual= destino
	
	while actual != None:
		lista.append(actual)
		actual= padre[actual]
	# Doy vuelta la lista
	lista.reverse()
	
	return lista
	
def mejor_aeropuerto_de_una_ciudad(grafo, aero, destino, modo):
	# Aca voy a quedarme con el mejor aeropuerto de una ciudad
	mejor_aero= None			
	# Aca voy a guardar el precio, el tiempo o la cantidad de vuelos, dependiendo del modo
	mejor_peso= float('inf')
	
	for destino_aero in grafo.obtener_aeropuerto_ady(destino):
		if modo == "rapido":
			peso= grafo.obtener_tiempo(aero, destino_aero)
		elif modo == "barato":
			peso= grafo.obtener_precio(aero, destino_aero)
		else:
			peso= grafo.obtener_num_vuelo(aero, destino_aero)
				
		if mejor_peso > peso:
			mejor_peso= peso
			mejor_aero= destino_aero
			
	return mejor_aero
	
			
def dijkstra(grafo, origen, destino, modo):
	dist= {}
	padres= {}
	heap_min= []
	visitados= {}
	
	for v in grafo.obtener_vertices():
		# De una ciudad obtengo los aeropuertos 
		for aero in grafo.obtener_aeropuerto_ady(grafo.obtener_ciudad(v)):
			dist[aero]= 99999
	
	aero_origen= grafo.obtener_aero_aleatorio_ciudad(origen)
	
	dist[aero_origen]= 0
	padres[aero_origen]= None
	heapq.heappush(heap_min, [aero_origen, dist[aero_origen]])
	ciudad_origen= grafo.obtener_ciudad(aero_origen)
	visitados[ciudad_origen]= ciudad_origen 
	
	while len(heap_min) != 0:
		vertice= heapq.heappop(heap_min)
		ciudad_actual= grafo.obtener_ciudad(vertice[0])
		visitados[ciudad_actual]= ciudad_actual
		
		if ciudad_actual == destino: return padres, dist
		
		for aero_ady in grafo.obtener_adyacentes(vertice[0]):
				ciudad= grafo.obtener_ciudad(aero_ady)
				
				if ciudad not in visitados:
					aero_dest= mejor_aeropuerto_de_una_ciudad(grafo, aero_ady, ciudad, modo)
					# Dependiendo del modo, voy a quedarme con el que tenga mejor precio o tiempo
					if modo == "rapido":
						mejor_peso= grafo.obtener_tiempo(aero_ady, aero_dest)
					else:
						mejor_peso= grafo.obtener_precio(aero_ady, aero_dest)
					
					dist_optima= vertice[1] + mejor_peso
				
					if dist_optima < dist[aero_ady]:
						dist[aero_ady]= dist_optima
						padres[aero_ady]= vertice[0]
						heapq.heappush(heap_min, [aero_ady, dist[aero_ady]])
				
	return padres, dist
 
def prim(grafo):
	visitados= set()
	heap_min= []
	arbol_tendido_min= Grafo()
	
	origen= grafo.obtener_vertice_aleatorio()
	visitados.add(origen)
	
	for w in grafo.obtener_adyacentes(origen):
		distancia= grafo.peso_union(origen, w)
		heapq.heappush(heap_min, [origen, w, distancia])
	
	for vertice in grafo.obtener_vertices():
		arbol_tendido_min.agregar_vertices(vertice)
	
	while len(heap_min) != 0:
		(vertice, adyacente, distancia)= heapq.heappop(heap_min)
		
		if adyacente in visitados: continue
	
		arbol_tendido_min.agregar_arista(vertice, adyacente, distancia)
		visitados.add(adyacente)
		
		for x in grafo.obtener_adyacentes(adyacente):
			if x not in visitados:
				heapq.heappush(heap_min, [adyacente, x, grafo.peso_union(adyacente, x)])
	
	return arbol_tendido_min

def ordenar(dist):
	heap_min= []
	
	for clave, valor in dist.items():
		heapq.heappush(heap_min, [clave, valor])
	
	return heap_min

def centralidad(grafo):
	cent= {}
	
	for v in grafo: cent[v]= 0
	
	for v in grafo:
		padre, dist= bfs(grafo, v)
		cent_aux= {}
		for w in grafo: centr_aux[w]= 0
		vertices_ordenados= ordenar(dist)
		for w,dist in vertices_ordenados:
			if w == v: continue
			cent_aux[padre[w]] += 1 
			cent_aux[padre[w]] += cent_aux[w]
		for w in grafo:
			if w == v: continue
			cent[w] += cent_aux[w]
	return cent
