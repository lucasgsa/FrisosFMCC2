#!/bin/bash

echo 'Configurando a biblioteca numpy'
if pip3 install numpy; then
	echo 'Numpy instalado com sucesso.'
else
	echo 'Não foi possível instalar a biblioteca numpy do python'
fi
