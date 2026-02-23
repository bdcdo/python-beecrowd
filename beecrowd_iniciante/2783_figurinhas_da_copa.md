# 2783 - Figurinhas da Copa

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 2
**Autor:** Por OBI  Brasil
**Timelimit: 1**

---

## Descricao

Em ano de Copa do Mundo de Futebol, o álbum de figurinhas oficial é sempre um grande sucesso entre crianças e também entre adultos. Para quem não conhece, o álbum contém espaços numerados de 1 a **N** para colar as figurinhas; cada figurinha, também numerada de 1 a **N**, é uma pequena foto de um jogador de uma das seleções que jogará a Copa do Mundo. O objetivo é colar todas as figurinhas nos respectivos espaços no álbum, de modo a completar o álbum (ou seja, não deixar nenhum espaço sem a correspondente figurinha).


Algumas figurinhas são carimbadas (efetivamente têm um carimbo impresso sobre a fotografia do jogador) e são mais raras, mais difíceis de conseguir. As figurinhas são vendidas em envelopes fechados, de forma que o comprador não sabe quais figurinhas está comprando, e pode ocorrer de comprar uma figurinha que ele já tenha colado no álbum.


Para ajudar os usuários, a empresa responsável pela venda do álbum e das figurinhas quer criar um aplicativo que permita gerenciar facilmente as figurinhas que faltam para completar o álbum.


Dados o número total de espaços e figurinhas do álbum (N), a lista das figurinhas carimbadas e uma lista das figurinhas já compradas (que pode conter figurinhas repetidas), sua tarefa é determinar quantas figurinhas carimbadas faltam para completar o álbum.

## Entrada

A primeira linha contém três números inteiros **N**(1 ≤ N ≤ 100) , **C**(1 ≤ C ≤ N/2) e **M** (1 ≤ M ≤ 300) indicando respectivamente o número de figurinhas (e espaços) do álbum, o número de figurinhas carimbadas do álbum e o número de figurinhas já compradas. A segunda linha contém **C** números inteiros distintos **Xi** indicando as figurinhas carimbadas do álbum. A terceira linha contém **M** números inteiros **Yi** (1 ≤ Xi , Yi ≤ N) indicando as figurinhas já compradas.

## Saida

Seu programa deve produzir um inteiro representando o número de figurinhas carimbadas que falta para completar o álbum.

## Exemplo 1

**Entrada:**
```
10 2 5
4 7
7 1 2 8 3
```

**Saida:**
```
1
```

## Exemplo 2

**Entrada:**
```
10 2 6
4 7
7 1 8 4 9 3
```

**Saida:**
```
0
```

## Exemplo 3

**Entrada:**
```
8 4 10
2 4 6 8
3 1 1 5 1 1 7 7 1 1
```

**Saida:**
```
4
```
