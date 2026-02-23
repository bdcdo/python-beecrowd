# 2167 - Falha do Motor

**Categoria:** Iniciante
**Assunto:** Ad hoc, Vetor
**Nivel:** 2
**Autor:** Por M.C. Pinto, UNILA  Brazil
**Timelimit: 1**

---

## Descricao

Ao observar a curva de velocidade de um motor, o engenheiro Zé percebeu que sempre ocorria uma queda quando as medidas eram feitas em intervalos de 10 ms. Mas esta queda acontecia em medidas diferentes a cada novo teste do motor.


Zé ficou curioso com essa falta de padrão e quer saber, para cada teste do motor, qual a primeira medida em que ocorre uma queda de velocidade.

## Entrada

A entrada é um teste do motor e é dada em duas linhas. A primeira tem o número **N** de medidas de velocidade do motor (1 < **N** ≤ 100). A segunda linha tem **N** inteiros: o número de RPM (rotações por minuto) **R_i** de cada medida (0 ≤ **R_i** ≤ 10000, para todo **R_i**, tal que 1 ≤ **i** ≤ **N**). Uma medida é considerada uma queda se é menor que a medida anterior.

## Saida

A saída é o índice da medida em que houve a primeira queda de velocidade no teste. Caso não aconteça uma queda de velocidade a saída deve ser o número zero.

## Exemplo 1

**Entrada:**
```
3
1 4 2
```

**Saida:**
```
3
```

## Exemplo 2

**Entrada:**
```
5
100 199 199 198 0
```

**Saida:**
```
4
```

## Exemplo 3

**Entrada:**
```
4
1 2 2 2
```

**Saida:**
```
0
```
