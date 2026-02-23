# 1037 - Intervalo

**Categoria:** Iniciante
**Assunto:** Seleção
**Nivel:** 3
**Autor:** Adaptado por Neilor Tonin, URI  Brasil
**Timelimit: 1**

---

## Descricao

Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.


O símbolo ( representa "maior que". Por exemplo:

                    [0,25]  indica valores entre 0 e 25.0000, inclusive eles.

                    (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

## Entrada

O arquivo de entrada contém um número com ponto flutuante qualquer.

## Saida

A saída deve ser uma mensagem conforme exemplo abaixo.

## Exemplo 1

**Entrada:**
```
25.01
```

**Saida:**
```
Intervalo (25,50]
```

## Exemplo 2

**Entrada:**
```
25.00
```

**Saida:**
```
Intervalo [0,25]
```

## Exemplo 3

**Entrada:**
```
100.00
```

**Saida:**
```
Intervalo (75,100]
```

## Exemplo 4

**Entrada:**
```
-25.02
```

**Saida:**
```
Fora de intervalo
```
