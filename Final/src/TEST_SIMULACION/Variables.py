

def get_variables(data):
	num = len(data)
	Estudiantes=[]
	for index, row in data.iterrows():
		Estudiantes.append(row['Nombre'])
	return num,Estudiantes
