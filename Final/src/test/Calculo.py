import math

def get_rend(CM_Inscritas,CM_Aprobadas):
	rend = float(CM_Aprobadas/CM_Inscritas)
	return rend

def get_semestres(CM_Inscritas,CM_Aprobadas,CS_Cursados):
	if CM_Inscritas == 0:
		S_min_grado = 50/5
		return S_min_grado
	else:
		CM_Inscritas = int(CM_Inscritas)
		CM_Aprobadas = int(CM_Aprobadas)
		CS_Cursados = int(CS_Cursados)
		rend = get_rend(CM_Inscritas,CM_Aprobadas)
		CM_Inscritas_por_S = CM_Inscritas/CS_Cursados
		CM_por_Semestre_Ideal = int(rend*CM_Inscritas_por_S)
		materias_rest = 50 - CM_Aprobadas
		S_min_grado = materias_rest/CM_por_Semestre_Ideal
		S_min_grado = math.ceil(S_min_grado)
		return S_min_grado