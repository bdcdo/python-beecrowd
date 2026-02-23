# 3256 - Divisão Inimiga

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 1
**Autor:** Por Lukáš Poláček  Norway
**Timelimit: 1**

---

## Descricao

O capitão Keram tem que tomar uma decisão difícil. É o ano de 2147 e há uma grande guerra no mundo. Seus soldados estão juntos desde o início da guerra, há dois anos, e alguns deles se tornaram inimigos. Felizmente, cada soldado tem no máximo 3 inimigos.


Eles precisam atacar outro país em breve, e Keram teme que os soldados inimigos possam não cooperar bem durante a batalha. Ele decidiu dividi-los em grupos de forma que cada soldado tenha no máximo um inimigo em seu grupo. Ele também quer simplificar, então quer usar o mínimo de grupos possível. Você pode dividir os soldados em grupos para ele?

## Entrada

Na primeira linha existem dois inteiros **n** e **m**, 2 ≤ **n** ≤ 100 000,0 ≤ **m** ≤ 3**n** / 2, onde **n** é o número de soldados e **m** é o número de pares de inimigos. Em seguida, seguem **m** linhas, cada uma contendo dois inteiros separados por espaço **a_i**, **b_i**, denotando que os soldados **a_i** e **b_i** são inimigos, onde 1 ≤ **a_i** <**b_i** ≤ **n**. Você pode assumir que todos os soldados têm no máximo 3 inimigos.

## Saida

A primeira linha de saída contém o número mínimo de grupos de soldados **k**. Cada uma das próximas **k** linhas contém uma lista separada por espaços de soldados em um grupo único.

## Exemplo

**Entrada:**
```
4 4
1 2
2 3
3 4
1 4
```

**Saida:**
```
2
1 3
2 4
```
