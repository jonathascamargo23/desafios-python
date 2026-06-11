## Desafio 01 - Clientes Exclusivos

## Objetivo
Identificar clientes exclusivos entre dois projetos utilizando conjuntos (sets) em Python.

## Desafio
Você foi contratado por uma consultoria para organizar dados de clientes de diferentes projetos. Cada projeto fornece uma lista de nomes de clientes, mas há duplicatas e inconsistências entre os projetos. Seu objetivo é identificar rapidamente quais clientes são exclusivos de cada projeto, facilitando a análise e evitando redundâncias. Para isso, você deverá utilizar conjuntos para processar as listas e encontrar os nomes que aparecem apenas em um dos projetos, garantindo que a equipe trabalhe com dados limpos e sem repetições desnecessárias.
Implemente um programa que receba duas listas de nomes de clientes, separadas por espaço, representando os clientes de dois projetos distintos. Seu programa deve exibir, em ordem alfabética, os nomes que aparecem em apenas uma das listas (ou seja, que não estão presentes em ambas). Se não houver nomes exclusivos, exiba a palavra "Nenhum". Não utilize bibliotecas externas.

## Entrada
Duas linhas. Cada linha contém uma lista de nomes (strings sem espaços internos), separados por espaço, representando os clientes de cada projeto. As listas podem estar vazias.

## Saída
Uma linha com os nomes exclusivos de cada projeto, separados por espaço e em ordem alfabética. Se não houver nomes exclusivos, exiba "Nenhum".

## Conceitos Utilizados

- set()
- symmetric_difference()
- sorted()
- Estruturas condicionais
- Manipulação de strings

## Autor
Jonathas Camargo Oliveira Barboza

## Como Executar

```python
python main.py
