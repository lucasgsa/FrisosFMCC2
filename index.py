print ("Carregando bibliotecas...")

from PIL import Image
import numpy
import sys
import os

from Friso import Friso, reflexaoVertical, reflexaoHorizontal, darMeiaVolta, reflexaoDeslizante, addDireita, addBaixo

def abreImagem(caminho):
	"""
	Abre um arquivo de imagem e retorna.
	"""
	return Image.open(caminho).convert('RGBA')
def geraFrisos(caminhoEntrada, caminhoSaida, repeticoes):
	try:
		imagem = abreImagem(caminhoEntrada)
	except(Exception):
		print ("Imagem inexistente!!!")
		quit()

	friso = Friso(imagem)

	print ("Gerando friso 1")
	friso1 = friso
	print ("Gerando friso 2")
	friso2 = reflexaoDeslizante(friso)
	print ("Gerando friso 3")
	friso3 = reflexaoVertical(friso)
	print ("Gerando friso 4")
	friso4 = reflexaoHorizontal(friso)
	print ("Gerando friso 5")
	friso5 = darMeiaVolta(friso)
	print ("Gerando friso 6")
	friso6 = darMeiaVolta(reflexaoVertical(friso))
	print ("Gerando friso 7")
	friso7 = reflexaoHorizontal(reflexaoVertical(friso))

	listaDeFrisos = [friso1, friso2, friso3, friso4, friso5, friso6, friso7]

	print ("Repetindo frisos gerados...")
	for i in range(len(listaDeFrisos)):
		atual = listaDeFrisos[i]
		for j in range(repeticoes):
			listaDeFrisos[i] = addDireita(listaDeFrisos[i],atual)
			
	#Salvando
	for i in range(len(listaDeFrisos)):
		try:
			print ("Salvando friso "+str(i+1))
			listaDeFrisos[i].salvarImagem(caminhoSaida+"/friso"+str(i+1)+".png")
		except(Exception):
			os.makedirs(caminhoSaida)
			listaDeFrisos[i].salvarImagem(caminhoSaida+"/friso"+str(i+1)+".png")
	print ("Todos os 7 frisos foram gerados com sucesso!")
		
arquivo, caminhoEntrada, caminhoSaida = sys.argv
geraFrisos(caminhoEntrada, caminhoSaida, 10)
