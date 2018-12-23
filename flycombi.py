from biblioteca_grafo import *
from TDAgrafo import *
import sys
import csv

def cargar_grafo(grafo, aeropuertos, vuelos):
	with open(aeropuertos) as arch_aeropuertos:
		for aeropuerto in arch_aeropuertos:
			campos= aeropuerto.split(",")
			ciudad, aero, lat, lng= campos[0], campos[1], campos[2], campos[3]
			grafo.agregar_vertices(ciudad, aero, lat, lng)
			
	with open(vuelos) as arch_vuelos:
		for vuelo in arch_vuelos:
			campos= vuelo.split(",")
			aeropuerto_i,aeropuerto_j,tmp_prom,precio,cant_vuelos= campos[0],campos[1],campos[2],campos[3],campos[4]	
			grafo.agregar_arista(aeropuerto_i, aeropuerto_j, tmp_prom, precio, cant_vuelos)
			
def camino_escalas(linea, grafo, dicc):
	parametro= linea[15:].split(",")
	ciudad_origen= parametro[0]
	ciudad_dest= parametro[1]
	
	# Voy a guardar los distintos caminos que hay entre ciudad_origen y ciudad_dest
	distintos_caminos= []
	# Voy a quedarme con el mejor dicc de padre 
	mejor_padre= {}
	# Voy a quedarme con el mejor aeropuerto de destino
	mejor_aero= None
	# mejor_dist va a ser el camino mac corto entre ciudad_origen y ciudad_dest.
	# Lo inicializo con un numero muy grande
	mejor_orden= 99999 
	
	for partida_aero in dicc[ciudad_origen]:
		# Como en una ciudad hay distintos aeropuertos calculo para cada uno el camino minimo
		padre, orden= bfs(grafo, origen)
		if padre != None:
			distintos_caminos.append([padre, orden])
	
	for destino_aero in dicc[ciudad_dest]:
		# Filtro entre los distintos caminos cual es el de minimo
		for padre, orden in distintos_caminos:
			if orden[destino_aero] < mejor_dist:
				mejor_padre= padre
				mejor_aero= destino_aero
				mejor_dist= orden[destino_aero]
	
	camino= reconstruir_camino(mejor_aero, mejor_padre)
	imprimir_camino(camino)
	return True

def camino_mas(linea, grafo):
	parametro= linea[11:].split(",")
	forma= parametro[0] #Tengo la forma, si es rapido o barato
	
	#Las unicas dos opciones que permite este comando
	opciones= ["rapido", "barato"]
	if forma not in opciones: return False
	
	ciudad_origen= parametro[1]
	ciudad_dest= parametro[2]
	
	padres, dist= dijkstra(grafo, ciudad_origen, ciudad_dest, forma)
	
	lista= []
	lista.append(grafo.obtener_aeropuerto(destino))
	v= lista[0]
	
	while v != origen:
		v = padre[v]
		lista.append(v)
		
	while lista:
		if len(lista) == 1:
			print(lista.pop())
		else:
			print(lista.pop(), "->")
	return True
	
def centralidad_aprox(linea, grafo):
	parametro= linea[18:].split(",")
	
	cantidad_aero= int(parametro[0]) 
	
	centr= centralidad(grafo)
	cont= 1
	
	for aero in cent:
		print(centr[aero])
		
		if cont < cantidad_aero:
			print(',')
		cont += 1
		if cont == cantidad_aero:
			break
			
def _vacaciones(grafo, vertice, cant, dicc):
				
	lista_recorrido= []
	
	for w in dicc[vertice]:
		visitados= {}
		lista_recorrido_aux= []
		
		if dfs(grafo, w, visitados, lista_recorrido_aux, cant, 1):
			return lista_recorrido_aux
			
	return lista_recorrido
			
			
def vacaciones(linea, grafo, dicc):
	parametro= linea[11:].split(",")
	origen= parametro[0]
	cant= int(parametro[1])
	
	recorrido= _vacaciones(grafo, origen, cant, dicc)
	
	largo= len(recorrido)
	
	if largo <= cant:
		print("Error")
	else:
		imprimir_camino(recorrido)
		
	return True
	
def lista_operaciones():
	print("camino_mas")
	print("camino_escalas")
	print("centralidad_aprox")
	print("vacaciones")

def comandos(comando, linea, grafo):
	
	if comando == "listar_operaciones": return lista_operaciones()
	if comando == "camino_mas": return camino_mas(linea, grafo)
	if comando == "camino_escalas": return camino_escalas(linea, grafo, dicc)
	if comando == "centralidad_aprox": return centralidad_aprox(linea, grafo)
	if comando == "vacaciones": return vacaciones(linea, grafo, dicc)
	
	return False
	

def main():
	archivos= sys.argv
	aeropuertos= archivos[1]
	vuelos= archivos[2]
	
	grafo= Grafo()
	
	cargar_grafo(grafo, aeropuertos, vuelos)
	
	linea= sys.stdin.readline().rstrip('\n')
	
	while len(linea) > 0:
		
		argumentos= linea.split(" ")
		comando= argumentos[0]
		
		comandos(comando, linea, grafo)
		
		try:
			linea= sys.stdin.readline().rstrip('\n')
		except EOFError:
			break

main()
