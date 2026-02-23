# 1973 - Jornada nas Estrelas

**Categoria:** Iniciante
**Assunto:** Simulação
**Nivel:** 7
**Autor:** Por Leandro Zatesko, UFFS  Brazil
**Timelimit: 1**

---

## Descricao

Após comprar vários sítios adjacentes na região do oeste catarinense, a família Estrela construiu uma única estrada que passa por todos os sítios em sequência. O primeiro sítio da sequência foi batizado de Estrela 1, o segundo de Estrela 2, e assim por diante. Porém, o irmão que vive em Estrela 1 acabou enlouquecendo e resolveu fazer uma Jornada nas Estrelas para roubar carneiros das propriedades de seus irmãos. Mas ele está definitivamente pirado. Quando passa pelo sítio Estrela **i**, ele rouba apenas um carneiro daquele sítio (se o sítio tem algum) e segue ou para Estrela **i** + 1 ou para Estrela **i** - 1, dependendo se o número de carneiros em Estrela **i** era, respectivamente, ímpar ou par. Se não existe a Estrela para a qual ele deseja seguir, ele interrompe sua jornada. O irmão louco começa sua Jornada em Estrela 1, roubando um carneiro do seu próprio sítio.

## Entrada

A primeira linha da entrada consiste de um único inteiro **N** (1 ≤ **N** ≤ 10^6), o qual representa o número de Estrelas. A segunda linha da entrada consiste de **N** inteiros, de modo que o **i**-ésimo inteiro, **X_i** (1 ≤ **X_i** ≤ 10^6), representa o número inicial de carneiros em Estrela **i**.

## Saida

Imprima uma linha contendo dois inteiros, de modo que o primeiro represente o número de Estrelas atacadas pelo irmão louco e o segundo represente o número total de carneiros *não* roubados.

## Exemplo 1

**Entrada:**
```
8
1 3 5 7 11 13 17 19
```

**Saida:**
```
8 68
```

## Exemplo 2

**Entrada:**
```
8
1 3 5 7 11 13 16 19
```

**Saida:**
```
7 63
```
