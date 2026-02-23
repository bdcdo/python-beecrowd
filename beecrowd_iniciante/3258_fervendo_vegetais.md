# 3258 - Fervendo Vegetais

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 4
**Autor:** Por Andreas Björklund & Lukáš Poláček  Finland
**Timelimit: 1**

---

## Descricao

O truque para ferver vegetais é garantir que todos os pedaços tenham aproximadamente o mesmo tamanho. Se não estiverem, os pequenos ficam muito moles ou os grandes ficam mal cozidos (ou ambos). Felizmente, você já ouviu falar da faca de cozinha, mas os avisos de seus pais sobre o uso de instrumentos afiados ainda ecoam em sua cabeça. Portanto, é melhor você usá-lo o mínimo possível. Você pode pegar um pedaço de um vegetal de peso **W** e cortá-lo arbitrariamente em dois pedaços de peso **W**esquerdo e **W**direito, onde **W**esquerdo + **W**direito = **W**. Esta operação constitui um “corte”. Dado um conjunto de pedaços de vegetais, determine o número mínimo de cortes necessários para fazer a proporção entre o menor e o maior pedaço resultante ficar acima de um determinado limite.

## Entrada

A entrada começa com um número de ponto flutuante **T** com 2 dígitos decimais, 0,5 <**T** <1, e um inteiro positivo **N** ≤ 1 000. Em seguida, siga **N**pesos inteiros positivos **W**₁, **W**₂, ..., **WN**. Todos os pesos são menores que 10⁶.

## Saida

Produza o número mínimo de cortes necessários para fazer a proporção entre a peça de peso mínimo resultante e a peça de peso máximo resultante estar acima de **T**. Você pode presumir que o número de cortes necessários seja inferior a 500.


Para evitar problemas com números de ponto flutuante, você pode assumir que a resposta ótima para a proporção **T** é a mesma que para a proporção **T**+ 0,0001.

## Exemplo 1

**Entrada:**
```
0.99 3
2000 3000 4000
```

**Saida:**
```
6
```

## Exemplo 2

**Entrada:**
```
0.80 2
1000 1400
```

**Saida:**
```
3
```
