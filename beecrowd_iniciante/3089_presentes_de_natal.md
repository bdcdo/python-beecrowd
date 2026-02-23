# 3089 - Presentes de Natal

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 7
**Autor:** Por Jorge Menezes, PUC Goiás  Brazil
**Timelimit: 1**

---

## Descricao

Dona Ricota é uma senhora muito meticulosa. Como o natal está se aproximando ela quer distribuir pares de presentes para seus familiares.


Durante sua última viagem, Dona Ricota comprou 2**n** presentes para seus **n** netos. Cada presente custou **x_i** reais (1 ≤ **i** ≤ 2**n**) e, para evitar conflitos, ela planeja formar os pares de presentes de modo a minimizar a diferença entre o valor total do par de presentes mais caro e o valor total do par mais barato.


Como você é uma pessoa gentil, Dona Ricota resolveu pedir sua ajuda para organizar os presentes.

## Entrada

A entrada consiste em vários casos de teste. A primeira linha de um caso de teste possui um inteiro **n** (2 ≤ **n** ≤ 10^4), a quantidade de netos. A segunda linha possui 2**n** inteiros **x_i** (1 ≤ **x_i** ≤ 10^8, em que 1 ≤ **i** ≤ 2**n**) em ordem decrescente e separados por exatamente um espaço em branco. Cada inteiro **x_i** representa o valor do **i**-ésimo presente comprado por Dona Ricota.


A primeira linha do último caso de teste contém **n = 0** e não deve ser processada.

## Saida

Para cada caso de teste imprima uma linha com o preço total do par de presentes mais caro e o preço total do par de presentes mais barato separados por um espaço em branco.

## Exemplo

**Entrada:**
```
1
10 10
1
10 5
2
40 39 20 1
4
1090 300 93 82 71 62 53 41
0
```

**Saida:**
```
20 20
15 15
59 41
1131 153
```
