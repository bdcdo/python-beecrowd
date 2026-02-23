# 1958 - Notação Científica

**Categoria:** Iniciante
**Assunto:** Ad-Hoc, Opções do Printf
**Nivel:** 4
**Autor:** Por M.C. Pinto, UNILA  Brazil
**Timelimit: 1**

---

## Descricao

Números em ponto flutuante podem ser bastante extensos para mostrar. Nesses casos, é conveniente usar a notação científica.


Você deve escrever um programa que, dado um número em ponto flutuante, mostre este número na notação científica: sempre mostre o sinal da mantissa; sempre mostre 4 casas decimais na mantissa; use o caractere 'E' para separar a mantissa do expoente; sempre mostre o sinal do expoente; e mostre o expoente com pelo menos 2 dígitos.

## Entrada

A entrada é um número em ponto flutuante de dupla precisão **X** (de acordo com o padrão IEEE 754-2008). Nunca haverá um número com mais de 110 caracteres nem com mais de 6 casas decimais.

## Saida

A saída é o número **X** em uma única linha na notação científica detalhada acima. Veja os exemplos abaixo.

## Exemplo 1

**Entrada:**
```
3.141592
```

**Saida:**
```
+3.1416E+00
```

## Exemplo 2

**Entrada:**
```
1.618033
```

**Saida:**
```
+1.6180E+00
```

## Exemplo 3

**Entrada:**
```
602214085774747474747474
```

**Saida:**
```
+6.0221E+23
```

## Exemplo 4

**Entrada:**
```
-0.000027
```

**Saida:**
```
-2.7000E-05
```

## Exemplo 5

**Entrada:**
```
-10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

**Saida:**
```
-1.0000E+100
```
