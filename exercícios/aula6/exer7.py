def gerarSequencia(numMaximo):
	penultimoNum = 0	
	ultimoNum = 1
	sequenciaList = [penultimoNum, ultimoNum]
	while numMaximo > 1:
		proximoNum = ultimoNum + penultimoNum
		sequenciaList.append(proximoNum)
		penultimoNum = ultimoNum
		ultimoNum = proximoNum
		numMaximo -= 1
	return sequenciaList

print(gerarSequencia(10))
