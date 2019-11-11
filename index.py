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
	
class Friso():
	def __init__(self, imagem):
		self.imagem = imagem
	def getImagem(self):
		return self.imagem
	def salvarImagem(self, caminho):
		self.imagem.save(caminho)
		
	def addDireita(self, outro):
		tempMatriz1 = numpy.array(self.imagem)
		tempMatriz2 = numpy.array(outro.imagem)
		new = numpy.concatenate((tempMatriz1, tempMatriz2),axis=1)
		return Friso(Image.fromarray(new))
	def addBaixo(self, outro):
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
friso1 = friso.addDireita(friso)
friso2 = friso.addDireita(friso.reflexaoHorizontal())
friso3 = friso.addDireita(friso.reflexaoVertical())
friso4 = friso.addBaixo(friso.reflexaoHorizontal())
friso5 = friso.addDireita(friso.reflexaoHorizontal().reflexaoVertical())
friso6 = friso.addDireita(friso.reflexaoVertical()).addDireita(friso.addDireita(friso.reflexaoVertical()).reflexaoHorizontal())
friso7 = friso.addDireita(friso.reflexaoVertical()).addBaixo(friso.addDireita(friso.reflexaoVertical()).reflexaoHorizontal())

listaDeFrisos = [friso1, friso2, friso3, friso4, friso5, friso6, friso7]

for i in range(len(listaDeFrisos)):
	for j in range(quantidadeRepeticoes):
		listaDeFrisos[i] = listaDeFrisos[i].addDireita(listaDeFrisos[i])
		
#Salvando
for i in range(len(listaDeFrisos)):
	listaDeFrisos[i].salvarImagem("frisos/friso"+str(i+1)+".png")
