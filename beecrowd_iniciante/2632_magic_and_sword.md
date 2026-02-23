# 2632 - Magic and Sword

**Categoria:** Iniciante
**Assunto:** -
**Nivel:** 8
**Autor:** Por Edson Alves da Costa Júnior, UNB  Brazil
**Timelimit: 1**

---

## Descricao

No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar as unidades inimigas. As magias são elementais: fogo, água, ar e terra, e a região afetada é determinada por um círculo cujo raio depende do nível da magia.


A tabela abaixo lista cada magia, o dano e o respectivo raio por nível:


![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2632.png)


As unidades inimigas são delimitadas por um retângulo de largura w e altura h, com canto inferior esquerdo posicionado no ponto (x0, y0). O inimigo sofrerá dano caso seu retângulo delimitador tenha qualquer intercessão com a área deﬁnida pelo círculo da magia.


Dada a posição e o retângulo delimitador da unidade inimiga, o centro da explosão e o identiﬁcador e o nível da magia, determine o dano sofrido pela unidade. Caso a unidade esteja fora do alcance da magia, o dano sofrido é igual a zero.

## Entrada

A entrada consiste em **T** (1 ≤ **T** ≤ 1000) casos de teste, onde o valor de **T** é informado na primeira linha da entrada. Cada caso de teste é composto por duas linhas. A primeira contém quatro número inteiros que repre-sentam as dimensões **w** e **h** (1 ≤ **w**, **h** ≤ 1000) do retângulo e as coordenadas **x0** e **y0** (0 ≤ **x0**, **y0** ≤ 1000) do canto inferior esquerdo. A segunda linha do caso de teste contém uma string com o identiﬁcador da magia (ﬁre para fogo, water para água, earth para terra e air para ar), o nível N desta magia (1 ≤ **N** ≤ 3) e as coordenadas **cx** e **cy** (0 ≤ **cx**, **cy** ≤ 1000) do centro da área da explosão.

## Saida

Para cada caso de teste, a saída deve ser o valor do dano recebido pela unidade, seguido de uma quebra de linha.

## Exemplo

**Entrada:**
```
4
10 10 50 50
fire 1 85 55
10 10 50 50
fire 2 85 55
10 10 50 100
water 3 100 100
10 10 50 100
air 3 100 100
```

**Saida:**
```
0
200
300
100
```
