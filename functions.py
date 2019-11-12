from PIL import Image
import numpy

def reflexaoVertical(friso):
	friso1 = friso.reflexaoVertical().reflexaoVertical()
	return addDireita(friso.reflexaoVertical(), friso1)
	
def reflexaoHorizontal(friso):
	friso1 = friso.reflexaoHorizontal()
	return addBaixo(friso, friso1)
	
def darMeiaVolta(friso):
	tempMatriz1 = numpy.array(friso.imagem)
	matrizVazia = tempMatriz1.copy()
	for i in range(len(matrizVazia)):
		for j in range(len(matrizVazia[i])):
			if matrizVazia[i][j].tolist() != [255, 255, 255]:
				matrizVazia[i][j] = numpy.array([255,255,255])
	novo = numpy.concatenate((tempMatriz1, matrizVazia),axis=1)
	return addBaixo(Friso(Image.fromarray(novo)), (Friso(Image.fromarray(novo)).reflexaoVertical().reflexaoHorizontal()))
	
def reflexaoDeslizante(friso):
	tempMatriz1 = numpy.array(friso.imagem)
	matrizVazia = tempMatriz1.copy()
	for i in range(len(matrizVazia)):
		for j in range(len(matrizVazia[i])):
			if matrizVazia[i][j].tolist() != [255, 255, 255]:
				matrizVazia[i][j] = numpy.array([255,255,255])
	novo = numpy.concatenate((tempMatriz1, matrizVazia),axis=1)
	novo2 = numpy.concatenate((matrizVazia, tempMatriz1), axis=1)
	return addBaixo(Friso(Image.fromarray(novo)), (Friso(Image.fromarray(novo2))).reflexaoHorizontal())
	
def addDireita(friso, outro):
	tempMatriz1 = numpy.array(friso.imagem)
	tempMatriz2 = numpy.array(outro.imagem)
	new = numpy.concatenate((tempMatriz1, tempMatriz2),axis=1)
	return Friso(Image.fromarray(new))
def addBaixo(friso, outro):
	tempMatriz1 = numpy.array(friso.imagem)
	tempMatriz2 = numpy.array(outro.imagem)
	new = numpy.concatenate((tempMatriz1, tempMatriz2))
	return Friso(Image.fromarray(new))
