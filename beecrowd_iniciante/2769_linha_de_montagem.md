# 2769 - Linha de Montagem

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 4
**Autor:** Por André Fillipi, INATEL  Brazil
**Timelimit: 1**

---

## Descricao

Com o advento dos conceitos da Indústria 4.0 e a evolução da internet das coisas, se tornou simples acompanhar todas as etapas da produção de um produto em uma linha de montagem. De posse das informações, é possível otimizar a produção e diminuir o tempo gasto até que esteja pronta.


Uma indústria apresenta o seguinte esquema de produção:


![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2769.png)


Sabendo o tempo gasto em cada estação, e o tempo para trocar entre as duas linhas de montagem, calcule o menor tempo em que é possível realizar a produção de um item.

## Entrada

A entrada possui vários casos de teste (EOF). A primeira linha contém um inteiro **N**, o número de etapas na linha de produção. A segunda linha contém dois inteiros **e_1**e **e_2**, o tempo gasto para a entrada em cada uma das linhas de produção. A próxima linha possui **N** valores, **a_11**, **a_12**, ..., **a_1n**, representando o tempo gasto para executar a iésima etapa na linha 1. A próxima também conterá  **N** valores, **a_21**, **a_22**, ..., **a_2n** com os tempos de cada etapa na linha 2. As próximas duas conterá **N-1** inteiros representando os tempos de transição da linha 1 para a linha 2,  **t_11**, **t_12**, ..., **t_1n-1** e da linha 2 para a linha 1,  **t_21**, **t_22**, ..., **t_2n-1**, respectivamente. Por fim, mais dois inteiros **x_1** e **x_2**_ representando o tempo de saída de cada linha.


Considere que número de etapas por caso de teste estará entre 1 e 1000 e os demais valores entre 0 e 10^5.

## Saida

A saída deve mostrar o tempo mínimo gasto na produção.

## Exemplo

**Entrada:**
```
3
1 1
1 2 3
3 2 1
1 2
2 1
1 1
```

**Saida:**
```
7
```
