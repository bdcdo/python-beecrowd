# 2542 - Iu-Di-Oh!

**Categoria:** Iniciante
**Assunto:** Matrizes
**Nivel:** 4
**Autor:** Por Ricardo Oliveira, UFPR  Brazil
**Timelimit: 1**

---

## Descricao

*Iu-di-oh!* é um jogo de cartas que virou uma verdadeira febre entre os jovens! Todo jogador de *Iu-di-oh!* tem seu próprio baralho, contendo várias cartas do jogo. Cada carta contém **N** atributos (como força, velocidade, inteligência, etc.). Os atributos são numerados de 1 a **N** e são dados por inteiros positivos.


Uma partida de *Iu-di-oh!* é sempre jogada por dois jogadores. Ao iniciar a partida, cada jogador escolhe exatamente uma carta de seu baralho. Após as escolhas, um atributo é sorteado. Vence o jogador cujo atributo sorteado em sua carta escolhida é maior que na carta escolhida pelo adversário. Caso os atributos sejam iguais, a partida empata.


Marcos e Leonardo estão na grande final do campeonato brasileiro de *Iu-di-oh!*, cujo prêmio é um Dainavision (que é quase um Plaisteition 2!). Dados os baralhos de ambos, a carta escolhida por cada um e o atributo sorteado, determine o vencedor!

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro **N** (1 ≤ **N** ≤ 100), o número de atributos de cada carta. A segunda linha contém dois inteiros **M** e **L** (1 ≤ **M**, **L** ≤ 100), o número de cartas no baralho de Marcos e de Leonardo, respectivamente.


As próximas **M** linhas descrevem o baralho de Marcos. As cartas são numeradas de 1 a **M**, e a *i*-ésima linha descreve a *i*-ésima carta. Cada linha contém **N** inteiros **a_i,1**,**a_i,2**,..., **a_i,N** (1 ≤ **a_i,j** ≤ 10^9). O inteiro **a_i,j** indica o atributo *j* da carta *i*. As próximas **L** linhas descrevem o baralho de Leonardo. As cartas são numeradas de 1 e **L** e são descritas de maneira análoga.


A próxima linha contém dois inteiros **C_M** e **C_L** (1 ≤ **C_M** ≤ **M**, 1 ≤ **C_L** ≤ **L**), as cartas escolhidas por Marcos e Leonardo, respectivamente. Por fim, a última linha contém um inteiro **A** (1 ≤ **A** ≤ **N**) indicando o atributo sorteado.


A entrada termina com fim-de-arquivo (EOF).

## Saida

Para cada caso de teste, imprima uma linha contendo “Marcos” se Marcos é o vencedor, “Leonardo” se Leonardo é o vencedor, ou “Empate” caso contrário (sem aspas).

## Exemplo

**Entrada:**
```
3
2 2
3 8 1
6 7 9
1 2 3
8 4 1
1 2
2
```

**Saida:**
```
Marcos
```
