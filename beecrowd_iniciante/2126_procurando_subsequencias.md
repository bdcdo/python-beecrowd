# 2126 - Procurando Subsequências

**Categoria:** Iniciante
**Assunto:** Subsequências Contíguas, Bi…
**Nivel:** 2
**Autor:** Por Igor Gomes, UEVA  Brazil
**Timelimit: 1**

---

## Descricao

Dados dois números naturais **N_1** e **N_2**, diz-se que **N_1** é *subsequência contígua* de **N_2** se todos os dígitos de **N_1** aparecem, na mesma ordem e de forma contígua, em **N_2**. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

## Entrada

A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural **N_1**(1 < **N_1** < 10^10), a segunda linha é composta por um valor **N_2**( **N_1 <****N_2**< 10^32).

## Saida

Para cada caso de teste imprima a quantidade de *subsequências contíguas*e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.

## Exemplo

**Entrada:**
```
78954
7895478954789547895447895478954
464133
1331646546874694
12
1231321455123214565423112
```

**Saida:**
```
Caso #1:
Qtd.Subsequencias: 6
Pos: 27
Caso #2:
Nao existe subsequencia
Caso #3:
Qtd.Subsequencias: 3
Pos: 24
```
