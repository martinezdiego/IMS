

def get_variables(data):
	num = len(data)
	Estudiantes=[]
	CM_Inscritas = []
	CM_Aprobadas = []
	CS_Cursados = []
	for index, row in data.iterrows():
		CM_Inscritas.append(row['Cantidad de Materias Inscritas'])
		CM_Aprobadas.append(row['Cantidad de Materias Aprobadas'])
		CS_Cursados.append(row['Semestres Cursados'])
		Estudiantes.append(row['Nombre'])
	return num,Estudiantes,CM_Inscritas,CM_Aprobadas,CS_Cursados
