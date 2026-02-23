# 2780 - Basquete de Robôs

**Categoria:** Iniciante
**Assunto:** Seleção
**Nivel:** 1
**Autor:** Por OBI  Brasil
**Timelimit: 1**

---

## Descricao

A organização da OIBR, Olimpíada Internacional de Basquete de Robô, está começando a ter problemas com dois times: os Bit Warriors e os Byte Bulls. É que os robôs desses times acertam quase todos os lan- çamentos, de qualquer posição na quadra! Pensando bem, o jogo de basquete ficaria mesmo sem graça se jogadores conseguissem acertar qualquer lançamento, não é mesmo? Uma das medidas que a OIBR está implantando é uma nova pontuação para os lançamentos, de acordo com a distância do robô para o início da quadra. A quadra tem 2000 centímetros de comprimento, como na figura.


![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2780.png)


Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:


• Se **D** ≤ 800, a cesta vale 1 ponto;


• Se 800 < **D** ≤ 1400, a cesta vale 2 pontos;


• Se 1400 < **D** ≤ 2000, a cesta vale 3 pontos.


A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da distância **D**, você deve escrever um programa para calcular o número de pontos do lançamento.

## Entrada

A primeira e única linha da entrada contém um inteiro **D**(0 ≤ **D** ≤ 2000) indicando a distância do robô para o início da quadra, em centímetros, no momento do lançamento.

## Saida

Seu programa deve produzir uma única linha, contendo um inteiro, 1, 2 ou 3, indicando a pontuação do lançamento.

## Exemplo 1

**Entrada:**
```
1720
```

**Saida:**
```
3
```

## Exemplo 2

**Entrada:**
```
250
```

**Saida:**
```
1
```

## Exemplo 3

**Entrada:**
```
1400
```

**Saida:**
```
2
```
