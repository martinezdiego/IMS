###########################################
#		PROYECTO DE SIMULACION			  #
#			FABRICIO ARAUJO				  #
#			DIEGO MARTINEZ				  #
###########################################

import random
import math
import simpy
import time
import string
import os
from os.path import join
from os import listdir
import pandas as pd
import csv
from pandas import read_csv
from Variables import get_variables
from Generate_output import output
from Graph import pensum_graph

os.system('clear')
NUM_SECRETARIAS = int(input('\n\n Antes de empezar por favor ingrese el numero de secretarias que atenderan: '))
TIEMPO_ATEMCION_MIN = 10
TIEMPO_ATENCION_MAX = 15
T_LLEGADAS = 3
data = pd.read_excel(join('./db','Students_List.xlsx'))
T_ESPERA = []
T_LLEGADA_EST = []
T_ATENCION = []
T_SALIDA = []
S_MIN = []
min_semesters = []
 
te  = 0.0 # tiempo de espera total
dt  = 0.0 # duracion de servicio total
fin = 0.0 # minuto en el que finaliza

def atencion(estudiante,i):
	global dt  #Para poder acceder a la variable dt declarada anteriormente
	R = random.random()  # Obtiene un numero aleatorio y lo guarda en R
	tiempo = TIEMPO_ATENCION_MAX - TIEMPO_ATEMCION_MIN  
	tiempo_atencion = TIEMPO_ATEMCION_MIN + (tiempo*R) # Distribucion uniforme
	yield env.timeout(tiempo_atencion) # deja correr el tiempo n minutos
	#time.sleep(1)
	min_semesters.append(random.randint(1,6))
	S_min_grado = pensum_graph(min_semesters[i])
	print(" \t\t\t %s esta listo en %.2f minutos" % (estudiante,tiempo_atencion))
	T_ATENCION.append(tiempo_atencion)
	print(" \t\t\t Y la cantidad de semestres para graduarse serian: " + str(S_min_grado))
	S_MIN.append(S_min_grado)
	a = 10
	b = 5
	dt = dt + tiempo_atencion # Acumula los tiempos de uso 

def estudiante (env, name, personal,i):
	global te
	global fin
	llega = env.now # Guarda el minuto de llegada del estudiante
	print ("%s llego a OREFI en minuto %.2f" % (name, llega))
	T_LLEGADA_EST.append(llega)
	with personal.request() as request: # Espera su turno
		yield request # Obtiene turno
		pasa = env.now # Guarda el minuto cuado comienza a ser atendido
		espera = pasa - llega # Calcula el tiempo que espero
		te = te + espera # Acumula los tiempos de espera
		print ("\t\t %s pasa con una secretaria en el minuto %.2f habiendo esperado %.2f minutos" % (name, pasa, espera))
		T_ESPERA.append(espera)
		yield env.process(atencion(name,i)) # Invoca al proceso de atencion
		#time.sleep(1)
		deja = env.now #Guarda el minuto en que termina el proceso de atencion
		print ("\t %s deja OREFI en el minuto %.2f" % (name, deja))
		T_SALIDA.append(deja)
		fin = deja # Conserva globalmente el ultimo minuto de la simulacion
	

def principal (env, personal):
	llegada = 0
	i = 0
	for i in range(TOT_ESTUDIANTES): # Para n Estudiantes
		#	time.sleep(5)
		R = random.random()
		llegada = -T_LLEGADAS * math.log(R) # Distribucion exponencial
		yield env.timeout(llegada)  # Deja transcurrir un tiempo entre uno y otro
		#time.sleep(1)
		env.process(estudiante(env, ESTUDIANTE_NOMBRE[i], personal,i))
		i += 1

os.system('clear')
print ("\n\n\t\t------------------- Bienvenido Simulacion OREFI ------------------")
TOT_ESTUDIANTES,ESTUDIANTE_NOMBRE = get_variables(data)
env = simpy.Environment() # Crea el objeto entorno de simulacion
personal = simpy.Resource(env, NUM_SECRETARIAS) #Crea los recursos (Secretarias)
env.process(principal(env, personal)) #Invoca el proceso principal
env.run() #Inicia la simulacion
output(ESTUDIANTE_NOMBRE,min_semesters,S_MIN,T_ESPERA,T_LLEGADA_EST,T_ATENCION,T_SALIDA,TOT_ESTUDIANTES)
print ("\n---------------------------------------------------------------------")
print ("\nIndicadores obtenidos: ")

lpc = te / fin
print ("\nLongitud promedio de la cola: %.2f" % lpc)
tep = te / TOT_ESTUDIANTES
print ("Tiempo de espera promedio = %.2f" % tep)
upi = (dt / fin) / NUM_SECRETARIAS
print ("Uso promedio de la instalacion = %.2f" % upi)
print ("\n---------------------------------------------------------------------")