# Desafio 03 - Validação de Cadastro

## Objetivo
Desenvolver funções reutilizáveis para formatação de nomes e validação de e-mails em um sistema de cadastro de clientes.

## Desafio
Você foi contratado por uma consultoria em TI para ajudar a organizar o sistema de cadastro de clientes. O time percebeu que o código está ficando difícil de manter, pois várias operações simples, como padronizar nomes e validar e-mails, estão espalhadas e duplicadas em diferentes partes do projeto. Sua missão é criar funções reutilizáveis que centralizem essas operações, facilitando futuras manutenções e evitando erros. Para isso, você deve implementar uma função que receba um nome completo e um e-mail, valide se o e-mail contém exatamente um caractere '@' e pelo menos um ponto '.' após o '@', e retorne o nome formatado (primeira letra de cada palavra em maiúsculo) seguido de ' - OK' se o e-mail for válido, ou ' - ERRO' caso contrário. Essa abordagem ajudará a equipe a manter o código limpo e eficiente, além de garantir que os dados dos clientes estejam sempre padronizados.
Implemente a função principal que leia uma linha contendo o nome completo e o e-mail separados por uma vírgula e um espaço. Utilize funções auxiliares para validar o e-mail e formatar o nome. Não utilize bibliotecas externas.

## Entrada
Uma única linha contendo o nome completo e o e-mail, separados por uma vírgula e um espaço. O nome pode conter uma ou mais palavras, e o e-mail pode conter letras, números, pontos e o caractere '@'.

## Saída
Uma única linha com o nome formatado (primeira letra de cada palavra em maiúsculo), seguido de ' - OK' se o e-mail for válido, ou ' - ERRO' caso contrário.

## Conceitos Utilizados
- Funções em Python
- Manipulação de strings
- Métodos `split()` e `count()`
- Estruturas condicionais (`if/else`)
- Boas práticas de reutilização de código

## Regras de Validação
Um e-mail é considerado válido quando:
- Possui exatamente um caractere '@'
- Possui pelo menos um ponto '.' após o '@'

## Aprendizados
Este desafio permitiu praticar a criação de funções auxiliares, validação de dados e organização de código para facilitar manutenção e reutilização.
