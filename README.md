# FrisosFMCC2

Gerador dos 7 tipos diferentes de frisos passada uma imagem png.
Bibliotecas utilizadas:
- NumPY para manipular arrays.
- PIL para carregar e salvar a imagem depois de feita.
- Sys para receber os argumentos passados no terminal.
- OS para fazer o sistema de verificação da pasta de destino e cria-lá se necessário.

Exemplo do que são frisos:

__Para ver mais exemplos vá até a pasta Frisos que contém os resultados diretos de todos os contidos na pasta Motivos para exemplos__

**Motivo do friso:**

<img src="./Motivos/grafico.png" width="150" height="150">

1º Friso:

<img src="./Frisos/Grafico/friso1.png">


2º Friso:

<img src="./Frisos/Grafico/friso2.png">


3º Friso:

<img src="./Frisos/Grafico/friso3.png">


4º Friso:

<img src="./Frisos/Grafico/friso4.png">


5º Friso:

<img src="./Frisos/Grafico/friso5.png">


6º Friso:

<img src="./Frisos/Grafico/friso6.png">


7º Friso:

<img src="./Frisos/Grafico/friso7.png">


**Detalhes sobre como usar:**

- Comando para executar no windows: python index.py caminhoImagem caminhoPastaSaida

- Use os comandos ./build.sh para baixar as bibliotecas necessárias.

- O programa roda em python 3, e portanto a biblioteca PIL já está presente.

- Para executar, utilize ./run.sh caminhoImagem caminhoPastaSaida

Problemas:
- Imagens JPG não é suportada por enquanto mas funciona na maioria dos casos.
- Não sei se caso haja imagem com fundo branco por exemplo, como a parte vazia da imagem em um exemplo de meia rotação ou reflexao deslizante deveria ficar. obs: deixei por padrao pixeis com transparência total.


Bug fixes: 

- As vezes dependendo da imagem se for baixada ele não consegue transformar direito e dá erro, mas se abrir em um editor e salvar novamente funciona. 
**CORRIGIDO**
Foi adicionado na abertura da imagem para converter para o tipo RGBA.

- Se nao existir a pasta de destino o programa quebra. 
**CORRIGIDO**
Quando a pasta não existe, ela é criada agora. Sendo checado antes de tentar salvar.

- Problema na versao que o python roda, nao sei bem usar o build.sh para baixar a biblioteca numpy e PIL dependendo da versão.
**Não corrigido**
