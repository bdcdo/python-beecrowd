# 2770 - Tamanho da Placa

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 7
**Autor:** Por João Gustavo Rogel de Oliveira, INATEL  Brazil
**Timelimit: 1**

---

## Descricao

Existe uma tradicional indústria no Brasil que produz equipamentos musicais. Atualmente eles estão totalmente imergidos com a era da Indústria 4.0 e a sua principal atuação é a criação de pedais de efeitos para guitarra, que existem em uma diversidade incrível, cada um para um tipo de cliente. Esta indústria implementou um sistema em que o seu cliente cria seu próprio pedal através de um protótipo 3D e interativo, inclusive com sons, simulando o pedal real. Sendo assim, após o cliente gerar seu modelo o mesmo é enviado para a empresa, onde será fabricado.


Acontece que para ser fabricado, o circuito do pedal é impresso em uma PCI(placa de circuito impresso), que tem um certo tamanho. Porém com a criatividade dos clientes, as placas estão tomando dimensões inimagináveis, tal fato faz com que a placa disponível na empresa não sirva. Como você é um excelente programador e um amante da música, cabe a você criar um programa em que dada as dimensões do circuito do cliente e a dimensão da placa disponível, diga se é possível utilizar ou não aquela placa.

## Entrada

A primeira linha de cada caso de teste consiste de três inteiros **X**, **Y**, **M**(**M**≤10^5) representando respectivamente as dimensões da placa da empresa e a quantidade de pedidos. Para cada uma das próximas **M**linhas será fornecido dois inteiros **X_i**e **Yi**representando as dimensões da PCI do cliente.


É garantido que as dimensões são valores inteiros maiores que 0 e menor ou igual a 64.


A entrada termina com EOF.

## Saida

Para cada circuito determine se é possível utilizar a PCI da empresa ou não.

## Exemplo

**Entrada:**
```
10 10 3
5 5
10 10
5 25
2 3 1
3 2
```

**Saida:**
```
Sim
Sim
Nao
Sim
```
