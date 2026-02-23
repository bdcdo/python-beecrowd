# 2534 - Exame Geral

**Categoria:** Iniciante
**Assunto:** Ordenação
**Nivel:** 2
**Autor:** Por Flávio Zavan, UFPR  Brazil
**Timelimit: 1**

---

## Descricao

Todo ano bissexto é realizado o exame geral de matemática da Nlogônia. Todos os cidadãos da nação são avaliados a fim de se estudar o desenvolvimento lógico e matemático do país ao longo dos anos.


Após as correções, os cidadãos são ordenadados de acordo com suas notas (quanto maior, melhor) e recebem descontos no imposto de renda de acordo com sua qualificação.


O Escritório Central de Estatística (ECE) é encarregado de processar os dados das notas obtidas no exame. Entretanto este ano, Vasya, um dos responsáveis, está internado no hospital com gripe H1N1 e você foi contratado para realizar o seu trabalho.


Escreva um programa que dado o número de habitantes da Nlogônia e todas as notas obtidas, responda as consultas para retornar a nota do cidadão que ficou em determinada posição.

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso contém dois inteiros **N** (1 ≤ **N** ≤ 100), **Q** (1 ≤ **Q** ≤ 100), o número de habitantes do país e o número de consultas, respectivamente.


As **N** linhas seguintes contém, cada uma, a nota **n_i** obtida pelo *i*-ésimo cidadão (0 ≤ **n_i** ≤ 30000).


As próximas **Q** linhas contém cada uma uma consulta, a posição **p_i** (1 ≤ **p_i** ≤ **N**) a qual a ECE está interessada em saber a nota.


A entrada termina com fim-de-arquivo (EOF).

## Saida

Para cada caso de teste, imprima, para cada consulta, uma linha contendo a nota do cidadão que ficou classificado na posição **p_i**.

## Exemplo

**Entrada:**
```
6 5
30
30
40
250
100
15
1
5
3
2
4
```

**Saida:**
```
250
30
40
100
30
```
