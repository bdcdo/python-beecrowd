# 2163 - O Despertar da Força

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 4
**Autor:** Por M.C. Pinto, UNILA  Brazil
**Timelimit: 1**

---

## Descricao

Há muito tempo atrás, em uma galáxia muito, muito distante...


Após o declínio do Império, sucateiros estão espalhados por todo o universo procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo para um terreno 4 x 7 com um sabre de luz nele (na posição (2, 4)).


![](https://resources.beecrowd.com/gallery/images/contests/935.png)


Você deve escrever um programa que, dado um terreno N x M, procura pelo padrão do sabre de luz nele. Nenhuma varredura tem mais do que um padrão de sabre de luz.

## Entrada

A primeira linha da entrada tem dois números positivos **N** e **M**, representando, respectivamente, o número de linhas e de colunas varridos no terreno (3 ≤ **N**, **M** ≤ 1000). Cada uma das próximas **N** linhas tem **M** inteiros, que descrevem os valores lidos em cada célula do terreno (-100 ≤ **T_ij** ≤ 100, para 1 ≤ **i** ≤ **N** e 1 ≤ **j** ≤ **M**).

## Saida

A saída é uma única linha com 2 inteiros **X** e **Y** separados por um espaço. Eles representam a coordenada (**X**,**Y**) do sabre de luz, caso encontrado. Se o terreno não tem um padrão de sabre de luz, **X** e **Y** são ambos zero.

## Exemplo 1

**Entrada:**
```
4 7
11 12 7 7 7 13 14
15 6 7 42 7 7 42
98 -5 7 7 7 42 7
-1 42 3 9 7 7 7
```

**Saida:**
```
2 4
```

## Exemplo 2

**Entrada:**
```
4 7
11 12 7 7 7 13 14
15 6 7 12 7 7 42
98 -5 7 7 7 42 7
-1 42 3 9 7 7 7
```

**Saida:**
```
0 0
```

## Exemplo 3

**Entrada:**
```
3 3
7 7 7
7 42 7
7 7 7
```

**Saida:**
```
2 2
```
