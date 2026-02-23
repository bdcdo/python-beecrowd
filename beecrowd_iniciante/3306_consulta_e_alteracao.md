# 3306 - Consulta e Alteração

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 2
**Autor:** Por Abner Samuel P. Palmeira, Instituto Federal do Sul de Minas Gerais  Brazil
**Timelimit: 1**

---

## Descricao

Dado um vetor com **N** elementos responda **Q** queries dos tipos:


**1 A B V:** Somar **V** em todos os elementos da posição **A** até a posição **B**do vetor.


**2 A B:** Retorna o Máximo Divisor Comum de todos os elementos das posições **A** até **B** no vetor

## Entrada

A entrada consiste em diversos casos de teste. A primeira linha de cada caso de teste contém dois inteiros **N** **Q**, representando respectivamente o tamanho do vetor e a quantidade de queries. A segunda linha da entrada contém **N** inteiros representando os elementos do vetor. As próximas **Q** linhas contém as queries como descrito anteriormente.


Limites:


1 ≤ **N**; **Q** ≤ 10^5

## Saida

Para cada query do tipo dois imprima o MDC de todas as posições do vetor que estão no intervalo **AB**

## Exemplo 1

**Entrada:**
```
7 4
1 8 4 16 6 13 20
2 2 4
2 5 7
1 5 7 1
2 5 7
```

**Saida:**
```
4
1
7
```

## Exemplo 2

**Entrada:**
```
5 1
4 6 8 10 12
2 1 5
```

**Saida:**
```
2
```
