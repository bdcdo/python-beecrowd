# 2162 - Picos e Vales

**Categoria:** Iniciante
**Assunto:** Ad hoc, Vetor
**Nivel:** 4
**Autor:** Por M.C. Pinto, UNILA  Brazil
**Timelimit: 1**

---

## Descricao

Ao observar a paisagem da Nlogônia, o professor MC percebeu que a cada intervalo de 100 metros existe um pico. E que exatamente na metade de dois picos há um vale. Logo, a cada 50 metros há um vale ou um pico e, ao longo da paisagem, não há um pico seguido por outro pico, nem um vale seguido por outro vale.


O professor MC ficou curioso com esse padrão e quer saber se, ao medir outras paisagens, isso se repete. Sua tarefa é, dada uma paisagem, indicar se ela possui esse padrão ou não.

## Entrada

A entrada é dada em duas linhas. A primeira tem o número **N** de medidas da paisagem (1 < **N** ≤ 100). A segunda linha tem **N** inteiros: a altura **H_i** de cada medida (-10000 ≤ **H_i** ≤ 10000, para todo **H_i**, tal que 1 ≤ **i** ≤ **N**). Uma medida é considerada um pico se é maior que a medida anterior. Uma medida é considerada um vale se é menor que a medida anterior.

## Saida

A saída é dada em uma única linha. Caso a paisagem tenha o mesmo padrão da Nlogônia, deve ser mostrado o número 1. Caso contrário, mostra-se o número 0.

## Exemplo 1

**Entrada:**
```
3
1 4 -2
```

**Saida:**
```
1
```

## Exemplo 2

**Entrada:**
```
5
100 99 112 -8 -7
```

**Saida:**
```
1
```

## Exemplo 3

**Entrada:**
```
4
1 2 2 1
```

**Saida:**
```
0
```
