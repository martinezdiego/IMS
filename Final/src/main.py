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

from utils import compute_min_semesters, output, get_variables, build_carrers_map

os.system('clear')
NUM_SECRETARIAS = int(input('\n\n Antes de empezar por favor ingrese el numero de secretarias que atenderan: '))
TIEMPO_ATENCION_MIN = int(input('\n\n Por favor ingrese el tiempo minimo de atencion: '))
TIEMPO_ATENCION_MAX = int(input('\n\n Por favor ingrese el tiempo maximo de atencion: '))
T_LLEGADAS = int(input('\n\n Por favor el tiempo promedio de llegadas del estudiante: '))
data = pd.read_excel(join('./db','students_list.xlsx'))
T_ESPERA = []
T_LLEGADA_EST = []
T_ATENCION = []
T_SALIDA = []
S_MIN = []
max_courses = []

carrers_map = build_carrers_map('./db/carrers_list.xlsx')

te  = 0.0 # tiempo de espera total
dt  = 0.0 # duracion de servicio total
fin = 0.0 # minuto en el que finaliza

def atencion(estudiante,i,max_courses):
	global dt  #Para poder acceder a la variable dt declarada anteriormente
	R = random.random()  # Obtiene un numero aleatorio y lo guarda en R
	tiempo = TIEMPO_ATENCION_MAX - TIEMPO_ATEMCION_MIN  
	tiempo_atencion = TIEMPO_ATEMCION_MIN + (tiempo*R) # Distribucion uniforme
	yield env.timeout(tiempo_atencion) # deja correr el tiempo n minutos
	#time.sleep(1)
	S_min_grado = compute_min_semesters(max_courses[i], carrers_map[ESTUDIANTE_CARRERA[i]])
	print("\t[PROCESADO] %s esta listo en %.2f minutos" % (estudiante,tiempo_atencion))
	T_ATENCION.append(tiempo_atencion)
	print("\t[PROCESADO] Y la cantidad de semestres para graduarse serian: " + str(S_min_grado))
	S_MIN.append(S_min_grado)
	dt = dt + tiempo_atencion # Acumula los tiempos de uso 

def estudiante (env, name, personal,i,max_courses):
	global te
	global fin
	llega = env.now # Guarda el minuto de llegada del estudiante
	print ("[LLEGA] %s en el minuto %.2f" % (name, llega))
	T_LLEGADA_EST.append(llega)
	with personal.request() as request: # Espera su turno
		yield request # Obtiene turno
		pasa = env.now # Guarda el minuto cuado comienza a ser atendido
		espera = pasa - llega # Calcula el tiempo que espero
		te = te + espera # Acumula los tiempos de espera
		print ("[PASA] %s en el minuto %.2f habiendo esperado %.2f minutos" % (name, pasa, espera))
		T_ESPERA.append(espera)
		yield env.process(atencion(name,i,max_courses)) # Invoca al proceso de atencion
		#time.sleep(1)
		deja = env.now #Guarda el minuto en que termina el proceso de atencion
		print ("[SALE] %s en el minuto %.2f" % (name, deja))
		T_SALIDA.append(deja)
		fin = deja # Conserva globalmente el ultimo minuto de la simulacion
	

def principal (env, personal):
	llegada = 0
	i = 0
	for i in range(TOT_ESTUDIANTES): # Para n Estudiantes
		#	time.sleep(5)
		R = random.random()
		max_courses.append(random.randint(1,6))
		llegada = -T_LLEGADAS * math.log(R) # Distribucion exponencial
		yield env.timeout(llegada)  # Deja transcurrir un tiempo entre uno y otro
		#time.sleep(1)
		env.process(estudiante(env, ESTUDIANTE_NOMBRE[i], personal,i,max_courses))
		i += 1

os.system('clear')
print ("\n\n\t\t------------------- Bienvenido Simulacion OREFI ------------------")
TOT_ESTUDIANTES,ESTUDIANTE_NOMBRE, ESTUDIANTE_CARRERA = get_variables(data)
env = simpy.Environment() # Crea el objeto entorno de simulacion
personal = simpy.Resource(env, NUM_SECRETARIAS) #Crea los recursos (Secretarias)
env.process(principal(env, personal)) #Invoca el proceso principal
env.run() #Inicia la simulacion
output(ESTUDIANTE_NOMBRE,ESTUDIANTE_CARRERA,max_courses,S_MIN,T_ESPERA,T_LLEGADA_EST,T_ATENCION,T_SALIDA,TOT_ESTUDIANTES)
print ("\n---------------------------------------------------------------------")
print ("\nIndicadores obtenidos: ")

lpc = te / fin
print ("\nLongitud promedio de la cola: %.2f" % lpc)
tep = te / TOT_ESTUDIANTES
print ("Tiempo de espera promedio = %.2f" % tep)
upi = (dt / fin) / NUM_SECRETARIAS
print ("Uso promedio de la instalacion = %.2f" % upi)
print ("\n---------------------------------------------------------------------")
