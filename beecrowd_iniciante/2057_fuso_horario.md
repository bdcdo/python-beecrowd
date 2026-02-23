# 2057 - Fuso Horário

**Categoria:** Iniciante
**Assunto:** Seleção
**Nivel:** 2
**Autor:** Por Neilor Tonin, URI  Brasil
**Timelimit: 1**

---

## Descricao

Paulo e Pedro fizeram uma longa jornada desde que partiram do Brasil para competir na Final Mundial da Maratona, em Phuket, Tailândia. Notaram que a cada escala que faziam, tinham que ajustar seus relógios por causa do fuso horário.


Assim, para melhor se organizarem para as próximas viagens, eles pediram que você faça um aplicativo para celular que, dada a hora de saída, tempo de viagem e o fuso do destino com relação à origem, você informe a hora de chegada de cada vôo no destino.


Por exemplo, se eles partiram às 10 horas da manhã para uma viagem de 4 horas rumo a um destino que fica à leste, em um fuso horário com uma hora a mais com relação ao fuso horário do ponto de partida, a hora de chegada terá que ser: 10 horas + 4 horas de viagem + 1 hora de deslocamento pelo fuso, ou seja, chegarão às 15 horas. Note que se a hora calculada for igual a 24, seu programa deverá imprimir 0 (zero).

## Entrada

A entrada contém 3 inteiros: **S** (0 ≤ **S**≤ 23), **T** (1 ≤ **T** ≤ 12) e **F** (-5 ≤ **F** ≤ 5), separados por um espaço, indicando respectivamente a hora da saída, o tempo de viagem e o fuso horário do destino com relação à origem.

## Saida

Imprima um inteiro que indica a hora local prevista no destino, conforme os exemplos abaixo.

## Exemplo 1

**Entrada:**
```
10 7 3
```

**Saida:**
```
20
```

## Exemplo 2

**Entrada:**
```
22 6 -2
```

**Saida:**
```
2
```

## Exemplo 3

**Entrada:**
```
0 3 -4
```

**Saida:**
```
23
```
