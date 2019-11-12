from PIL import Image
import numpy

def abreImagem(caminho):
	"""
	Abre um arquivo de imagem e retorna.
	"""
	return Image.open(caminho)
	
def reflexaoVertical(friso):
	friso1 = friso.reflexaoVertical()
	return friso.addDireita(friso1)
	
def reflexaoHorizontal(friso):
	friso1 = friso.reflexaoHorizontal()
	return friso.addBaixo(friso1)
	
def darMeiaVolta(friso):
	tempMatriz1 = numpy.array(friso.imagem)
	matrizVazia = tempMatriz1.copy()
	for i in range(len(matrizVazia)):
		for j in range(len(matrizVazia[i])):
			if matrizVazia[i][j].tolist() != [255, 255, 255]:
				matrizVazia[i][j] = numpy.array([255,255,255])
	novo = numpy.concatenate((tempMatriz1, matrizVazia),axis=1)
	return addBaixo(Friso(Image.fromarray(novo)), (Friso(Image.fromarray(novo)).reflexaoVertical().reflexaoHorizontal()))
	
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
	
class Friso():
	def __init__(self, imagem):
		self.imagem = imagem
	def getImagem(self):
		return self.imagem
	def salvarImagem(self, caminho):
		self.imagem.save(caminho)
	def addDiagonal(self, outro):
		tempMatriz1 = numpy.array(self.imagem)
		tempMatriz2 = numpy.array(outro.imagem)
		
		new = numpy.concatenate((tempMatriz1, tempMatriz2))
		return Friso(Image.fromarray(new))
	def reflexaoVertical(self):
		tempMatriz = numpy.array(self.imagem)
		for i in range(len(tempMatriz)):
			tempMatriz[i] = tempMatriz[i][::-1]
		return Friso(Image.fromarray(tempMatriz))
	def reflexaoHorizontal(self):
		tempMatriz = numpy.array(self.imagem)
		tempMatriz2 = tempMatriz[::-1]
		return Friso(Image.fromarray(tempMatriz2))

imagem = abreImagem("pe.png")

#OBS: Essa quantidade eh de quantas vezes ira dobrar, portando utilizar 2**x vezes.
quantidadeRepeticoes = 1

friso = Friso(imagem)

friso1 = darMeiaVolta(friso)

friso1.imagem.show()
#friso2 = friso.addDireita(friso.reflexaoHorizontal())
#friso3 = reflexaoVertical(friso.reflexaoVertical())
#friso4 = reflexaoHorizontal(friso)
#friso5 = friso.addDireita(friso.reflexaoHorizontal().reflexaoVertical())
#friso6 = reflexaoVertical(friso).addDireita(reflexaoVertical(friso).reflexaoHorizontal())
#friso7 = reflexaoHorizontal(reflexaoVertical(friso))

listaDeFrisos = [friso1]

for i in range(len(listaDeFrisos)):
	for j in range(quantidadeRepeticoes):
		listaDeFrisos[i] = listaDeFrisos[i].addDireita(listaDeFrisos[i])
		
#Salvando
for i in range(len(listaDeFrisos)):
	listaDeFrisos[i].salvarImagem("frisos/friso"+str(i+1)+".png")
