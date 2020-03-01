import random
import math
import simpy
import time
import string
from os.path import join
from os import listdir
import pandas as pd
import csv
from pandas import read_csv
from Datos_Estudiante import get_variables
import Calculo


NUM_SECRETARIAS = 2
TIEMPO_ATEMCION_MIN = 5
TIEMPO_ATENCION_MAX = 10
T_LLEGADAS = 3
#TIEMPO_SIMULACION = 120
#TOT_ESTUDIANTES = 10
data = pd.read_excel(join('./raw_data','Estudiantes.xlsx'))
 
te  = 0.0 # tiempo de espera total
dt  = 0.0 # duracion de servicio total
fin = 0.0 # minuto en el que finaliza

def atencion(estudiante,i):
	global dt  #Para poder acceder a la variable dt declarada anteriormente
	R = random.random()  # Obtiene un numero aleatorio y lo guarda en R
	tiempo = TIEMPO_ATENCION_MAX - TIEMPO_ATEMCION_MIN  
	tiempo_atencion = TIEMPO_ATEMCION_MIN + (tiempo*R) # Distribucion uniforme
	yield env.timeout(tiempo_atencion) # deja correr el tiempo n minutos
	S_min_grado = Calculo.get_semestres(CM_Inscritas[i],CM_Aprobadas[i],CS_Cursados[i])
	#print(i)
	print(" \t\t\t %s esta listo en %.2f minutos" % (estudiante,tiempo_atencion))
	print(" \t\t\t Y la cantidad de semestres para graduarse serian: " + str(S_min_grado))
	a = 10
	b = 5
	dt = dt + tiempo_atencion # Acumula los tiempos de uso de la i


def estudiante (env, name, personal,i):
	global te
	global fin
	llega = env.now # Guarda el minuto de llegada del cliente
	print ("%s llego a OREFI en minuto %.2f" % (name, llega))
	with personal.request() as request: # Espera su turno
		yield request # Obtiene turno
		pasa = env.now # Guarda el minuto cuado comienza a ser atendido
		espera = pasa - llega # Calcula el tiempo que espero
		te = te + espera # Acumula los tiempos de espera
		print ("\t\t %s pasa con una secretaria en el minuto %.2f habiendo esperado %.2f minutos" % (name, pasa, espera))
		yield env.process(atencion(name,i)) # Invoca al proceso cortar
		deja = env.now #Guarda el minuto en que termina el proceso cortar 
		print ("\t %s deja OREFI en el minuto %.2f" % (name, deja))
		fin = deja # Conserva globalmente el ultimo minuto de la simulacion
	

def principal (env, personal):
	llegada = 0
	i = 0
	for i in range(TOT_ESTUDIANTES): # Para n clientes
		#	time.sleep(5)
		R = random.random()
		llegada = -T_LLEGADAS * math.log(R) # Distribucion exponencial
		yield env.timeout(llegada)  # Deja transcurrir un tiempo entre uno y otro
		env.process(estudiante(env, ESTUDIANTE_NOMBRE[i], personal,i))
		i += 1


print ("------------------- Bienvenido Simulacion OREFI ------------------")
TOT_ESTUDIANTES,ESTUDIANTE_NOMBRE,CM_Inscritas,CM_Aprobadas,CS_Cursados = get_variables(data)
#random.seed (SEMILLA)  # Cualquier valor
env = simpy.Environment() # Crea el objeto entorno de simulacion
personal = simpy.Resource(env, NUM_SECRETARIAS) #Crea los recursos (peluqueros)
env.process(principal(env, personal)) #Invoca el proceso princial
env.run() #Inicia la simulacion
print ("\n---------------------------------------------------------------------")
print ("\nIndicadores obtenidos: ")

lpc = te / fin
print ("\nLongitud promedio de la cola: %.2f" % lpc)
tep = te / TOT_ESTUDIANTES
print ("Tiempo de espera promedio = %.2f" % tep)
upi = (dt / fin) / NUM_SECRETARIAS
print ("Uso promedio de la instalacion = %.2f" % upi)
print ("\n---------------------------------------------------------------------")