# 3348 - Jogo das Aranhas

**Categoria:** Iniciante
**Assunto:** Problema de Josefo
**Nivel:** 3
**Autor:** Por Leandro Zatesko, Federal University of Technology of Paraná  Brazil
**Timelimit: 1**

---

## Descricao

Em todo o Sul do Brasil é possível encontrar várias espécies de aracnídeos do gênero Loxosceles, conhecidas popularmente pelo nome de *aranha-marrom*. Apesar de não serem agressivas, essas aranhas inoculam um veneno necrosante bastante forte e são responsáveis pelo maior número de acidentes com aranhas no Brasil. Acidentes com aranhas-marrons ocorrem geralmente quando elas se escondem dentro de calçados e roupas ou embaixo de lençóis.


Algumas pessoas confundem as aranhas-marrons com as aranhas do gênero Nesticodes, conhecidas popularmente pelo nome de *aranha-vermelha-comum*, também muito comuns no Sul do Brasil. Inofensivas aos seres humanos, as aranhas do gênero Nesticodes são predadoras naturais das aranhas do gênero Loxosceles e não devem ser eliminadas.


Arthur e Merlin resolveram jogar um jogo perigoso com aranhas, o qual não recomendamos que você reproduza em casa. Arthur começa coletando **N** ≥ 1 aranhas do gênero Nesticodes e **N** aranhas do gênero Loxosceles, dispondo as 2 × **N** aranhas em um círculo de modo que as aranhas inofensivas ocupem as **N** primeiras posições, e as aranhas-marrons as **N** últimas. Em seguida, Merlin informa um inteiro positivo **K** a Arthur, o qual entra num processo de matar cada **K**-ésima aranha ainda viva no círculo até que exatamente **N** aranhas tenham sido mortas. O objetivo de Merlin é que apenas aranhas-marrons sejam mortas. Por exemplo, se **N** = 3 e **K** = 5, as aranhas nas posições 5, 4, 6 são eliminadas, nesta ordem, e Merlin atinge seu objetivo, vencendo o jogo. Se **N** = 2 e **K** = 7, as aranhas nas posições 3, 4 são eliminadas,
                    nesta ordem, e Merlin também vence o jogo. Porém, se **N** = 3 e **K** = 10, as aranhas nas posições 4, 3, 6 são eliminadas, nesta ordem, e, portanto, Arthur vence o jogo.

## Entrada

A entrada consiste unicamente no número **N** (**N** ≤ 19), um inteiro positivo.

## Saida

Imprima um inteiro positivo **K** < 10^16 que faça Merlin ganhar o jogo.

## Exemplo 1

**Entrada:**
```
1
```

**Saida:**
```
2
```

## Exemplo 2

**Entrada:**
```
1
```

**Saida:**
```
4
```

## Exemplo 3

**Entrada:**
```
2
```

**Saida:**
```
7
```

## Exemplo 4

**Entrada:**
```
2
```

**Saida:**
```
12
```

## Exemplo 5

**Entrada:**
```
3
```

**Saida:**
```
5
```
