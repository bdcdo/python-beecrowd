# 3230 - Senhores da Guerra Galácticos

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** By Unknown  Finlândia
**Timelimit: 1**

---

## Descricao

A galáxia verá a paz finalmente? Todos os senhores da guerra se reuniram para dividir todo o espaço entre eles. As negociações foram muito longe e os senhores da guerra finalmente concordaram em uma maneira pacífica de decidir quem fica com o quê. O mapa galáctico bidimensional deve primeiro ser dividido em setores, dividindo-o ao longo de um conjunto de linhas infinitas. O senhor da guerra com a maior frota de batalha escolherá um setor, então o senhor da guerra com a segunda maior frota escolherá algum outro setor e assim por diante, até que todos tenham obtido um setor. Isso é então repetido até que não haja mais setores.


Diferentes conjuntos de linhas foram sugeridos e cabe a você apresentar essas alternativas na reunião. Para ter certeza de que haverá paz, você está pronto para modificar ligeiramente as sugestões. Você tem alguma experiência com senhores da guerra e sabe que nenhum senhor da guerra se contentará com menos espaço do que qualquer outro, então, para que haja paz, todos eles devem ter exatamente a mesma área no mapa. Como o espaço é infinito, o mapa também o é. Alguns setores, portanto, terão área infinita, de modo que é a quantidade de espaço que todos vão querer. Quantas linhas extras você terá que adicionar para garantir que cada senhor da guerra possa obter pelo menos um setor com área infinita?

## Entrada

A primeira linha de entrada contém dois inteiros positivos **W** e **N**, (1 ≤ **W**, **N** ≤ 100) denotando o número de senhores da guerra e o número de linhas na divisão de espaço sugerida. Ela é seguida por **N** linhas, cada uma contendo quatro inteiros **x_1**, **y_1** , **x_2** e **y_2**, cada um com um valor absoluto não superior a 10.000. Isso significa que uma linha está cruzando os dois pontos (**x_1, y_1**) e (**x_2, y_2**) no mapa galáctico. Esses dois pontos não serão iguais.

## Saida

Imprima o número de linhas que você terá que adicionar a esta sugestão para satisfazer todos os senhores da guerra.

## Exemplo 1

**Entrada:**
```
Input Samples
```

**Saida:**
```
Output Samples
```

## Exemplo 2

**Entrada:**
```
2 1
1 1 -2 0
```

**Saida:**
```
0
```

## Exemplo 3

**Entrada:**
```
5 3
0 5 5 5
0 0 1 1
2 2 3 3
```

**Saida:**
```
1
```
