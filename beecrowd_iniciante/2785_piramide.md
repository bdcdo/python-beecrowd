# 2785 - Pirâmide

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 4
**Autor:** Por OBI  Brasil
**Timelimit: 1**

---

## Descricao

No depósito da fábrica, encostada numa parede, existe uma matriz de **N** linhas por **N** colunas de caixas empilhadas. Cada caixa possui um peso inteiro positivo associado. O inspetor da fábrica precisa retirar algumas caixas da matriz de modo a deixar uma espécie de pirâmide de caixas satisfazendo as seguintes restrições:


• Se uma caixa está na pirâmide, a caixa imediatamente abaixo dela também deve estar na pirâmide;


• Na **i**-ésima linha de caixas (a linha 1 é a do topo da matriz), a pirâmide deve ter exatamente **i** caixas consecutivas.


Dados os pesos de todas as caixas na matriz, seu programa deve calcular o peso total mínimo que uma pirâmide poderá ter, se o inspetor retirar algumas caixas segundo as restrições acima.

## Entrada

A primeira linha da entrada contém um inteiro **N**(1 ≤ **N** ≤ 100), indicando a dimensão da matriz. As **N** linhas seguintes contêm, cada uma, **N** inteiros representando os pesos das caixas em cada linha da matriz de caixas.


Os valores dos elementos da matriz estão entre 1 e 100, inclusive.

## Saida

Seu programa deve produzir uma única linha, contendo um inteiro, indicando o peso total mínimo que a pirâmide poderá ter.

## Exemplo 1

**Entrada:**
```
3
5 2 4
3 6 7
10 5 10
```

**Saida:**
```
36
```

## Exemplo 2

**Entrada:**
```
4
45 8 3 1
1 10 5 67
4 4 3 18
10 4 7 12
```

**Saida:**
```
62
```
