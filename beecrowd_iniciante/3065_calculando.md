# 3065 - Calculando

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 4
**Autor:** Por  Brazil
**Timelimit: 1**

---

## Descricao

A disseminação dos computadores se deve principalmente à capacidade de eles se comportarem como outras máquinas, vindo a substituir muitas destas. Esta flexibilidade é possível porque podemos alterar a funcionalidade de um computador, de modo que ele opere da forma que desejarmos: essa é a base do que chamamos programação.


Sua tarefa é escrever um programa que faça com que o computador opere como uma calculadora simples. O seu programa deve ler expressões aritméticas e produzir como saída o valor dessas expressões, como uma calculadora faria. O programa deve implementar apenas um subconjunto reduzido das operações disponíveis em uma calculadora: somas e subtrações.

## Entrada

A entrada é composta de vários conjuntos de testes. A primeira linha de um conjunto de testes contém um número inteiro **m** (1 ≤ **m** ≤ 100), indicando o número de operandos da expressão a ser avaliada. A segunda linha de um conjunto de testes contém a expressão aritmética a ser avaliada, no seguinte formato:


**X_1 s_1 X_2 s_2 ... X_m-1 s_m-1 X_m**


onde


• **X_i**, 1 ≤ **i** ≤ **m**, é um operando (0 ≤ **X_i** ≤ 100);


• **s_j**, 1 ≤ **j** < **m**, é um operador, representado pelos símbolos ‘+’ ou ‘–’;


• não há espaços em branco entre operandos e operadores. O final da entrada é indicado pelo valor **m** = 0.

## Saida

Para cada conjunto de testes da entrada seu programa deve produzir três linhas. A primeira linha deve conter um identificador da expressão, no formato “Teste n”, onde n é numerado a partir de 1. Na segunda linha deve aparecer o resultado encontrado pelo seu programa. A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente

## Exemplo

**Entrada:**
```
3
3+7-22
3
5-10-77
10
1+2+3+4+5+6+7+8+9+10
0
```

**Saida:**
```
Teste 1
-12
Teste 2
-82
Teste 3
55
```
