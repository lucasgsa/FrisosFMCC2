#!/bin/bash

if python index.py $1 $2; then
	echo 'Fim script.!'
else
	echo 'Não foi possível executar o script devido a um erro.'
fi
