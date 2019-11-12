from PIL import Image
import numpy

from Friso import Friso, reflexaoVertical, reflexaoHorizontal, darMeiaVolta, reflexaoDeslizante, addDireita, addBaixo

def abreImagem(caminho):
	"""
	Abre um arquivo de imagem e retorna.
	"""
	return Image.open(caminho)

imagem = abreImagem("pe.png")

quantidadeRepeticoes = 3

friso = Friso(imagem)

friso1 = friso
friso2 = reflexaoDeslizante(friso)
friso3 = reflexaoVertical(friso)
friso4 = reflexaoHorizontal(friso)
friso5 = darMeiaVolta(friso)
friso6 = darMeiaVolta(reflexaoVertical(friso))
friso7 = reflexaoHorizontal(reflexaoVertical(friso))

listaDeFrisos = [friso1, friso2, friso3, friso4, friso5, friso6, friso7]

for i in range(len(listaDeFrisos)):
	atual = listaDeFrisos[i]
	for j in range(quantidadeRepeticoes):
		listaDeFrisos[i] = addDireita(listaDeFrisos[i],atual)
		
#Salvando
for i in range(len(listaDeFrisos)):
	listaDeFrisos[i].salvarImagem("frisos/friso"+str(i+1)+".png")
