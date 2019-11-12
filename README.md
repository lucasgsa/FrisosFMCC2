# FrisosFMCC2

Gerador dos 7 tipos diferentes de frisos passada uma imagem png.

- Comando para executar no windows: python index.py caminhoImagem caminhoPastaSaida

- Use os comandos ./build.sh para baixar as bibliotecas necessárias.

- O programa roda em python 3, e portanto apenas biblioteca PIL já está presente.

- Para executar, utilize ./run.sh caminhoImagem caminhoPastaSaida

Bibliotecas utilizadas: numpy e PIL

Problemas:
- Imagens JPG podem dar problema por enquanto.
- Não sei se caso haja imagem com fundo branco por exemplo, como a parte vazia da imagem em um exemplo de meia rotação ou reflexao deslizante deveria ficar. obs: deixei por padrao pixeis com transparência total.
- Bug fixes: as vezes dependendo da imagem se for baixada ele não consegue transformar direito e dá erro, mas se abrir em um editor e salvar novamente funciona. CORRIGIDO
