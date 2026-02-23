# 2787 - Xadrez

**Categoria:** Iniciante
**Assunto:** Seleção
**Nivel:** 1
**Autor:** Por OBI  Brasil
**Timelimit: 1**

---

## Descricao

No tabuleiro de xadrez, a casa na linha 1, coluna 1 (canto superior esquerdo) é sempre branca e as cores das casas se alternam entre branca e preta, de acordo com o padrão conhecido como... xadrez! Dessa forma, como o tabuleiro tradicional tem oito linhas e oito colunas, a casa na linha 8, coluna 8 (canto inferior direito) será também branca. Neste problema, entretanto, queremos saber a cor da casa no canto inferior direito de um tabuleiro com dimensões quaisquer: **L** linhas e **C** colunas. No exemplo da figura, para **L** = 6 e **C** = 9, a casa no canto inferior direito será preta!


![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2787.png)

## Entrada

A primeira linha da entrada contém um inteiro **L** (1 ≤ **L** ≤ 1000) indicando o número de linhas do tabuleiro. A segunda linha da entrada contém um inteiro **C** (1 ≤ **C** ≤ 1000) representando o número de colunas.

## Saida

Imprima uma linha na saída. A linha deve conter um inteiro, representando a cor da casa no canto inferior direito do tabuleiro: 1, se for branca; e 0, se for preta.

## Exemplo 1

**Entrada:**
```
6
9
```

**Saida:**
```
0
```

## Exemplo 2

**Entrada:**
```
8
8
```

**Saida:**
```
1
```

## Exemplo 3

**Entrada:**
```
5
91
```

**Saida:**
```
1
```
