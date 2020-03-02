import pandas as pd
import time
import csv

def output(ESTUDIANTE_NOMBRE,MAX_MATERIAS,S_min,T_ESPERA,T_LLEGADA_EST,T_ATENCION,T_SALIDA,TOT_ESTUDIANTE):
	Dictionary = {
		'ESTUDIANTE_NOMBRE':[],
		'MAX_MATERIAS':[],
		'S_min':[],
		'T_ESPERA':[],
		'T_LLEGADA_EST':[],
		'T_ATENCION':[],
		'T_SALIDA':[],
	}

	for i in range(0,TOT_ESTUDIANTE):
		T_LL_aux = float("{0:.2f}".format(T_LLEGADA_EST[i]))
		T_ES_aux = float("{0:.2f}".format(T_ESPERA[i]))
		T_AT_aux = float("{0:.2f}".format(T_ATENCION[i]))
		T_SA_aux = float("{0:.2f}".format(T_SALIDA[i]))
		Dictionary['ESTUDIANTE_NOMBRE'].append(ESTUDIANTE_NOMBRE[i])
		Dictionary['MAX_MATERIAS'].append(MAX_MATERIAS[i])
		Dictionary['S_min'].append(S_min[i])
		Dictionary['T_ESPERA'].append(T_ES_aux)
		Dictionary['T_LLEGADA_EST'].append(T_LL_aux)
		Dictionary['T_ATENCION'].append(T_AT_aux)
		Dictionary['T_SALIDA'].append(T_SA_aux)

	ordered = [
		'ESTUDIANTE_NOMBRE',
		'MAX_MATERIAS',
		'S_min',
		'T_LLEGADA_EST',
		'T_ESPERA',
		'T_ATENCION',
		'T_SALIDA',
	]

	output_dataframe = pd.DataFrame(Dictionary)
	output_dataframe[ordered].to_csv('./Report.csv', index=0)