# 2702 - Escolha Difícil

**Categoria:** Iniciante
**Assunto:** Seleção
**Nivel:** 1
**Autor:** Por Inés Kereki  Uruguay
**Timelimit: 1**

---

## Descricao

Em um longo voo, companhias aéreas oferecem uma refeição aos seus passageiros. Geralmente as aeromoças conduzem carrinhos contendo as refeições pelos corredores do avião. Quando o carrinho chega em sua fileira, você é questionado imediatamente: “Frango, bife, ou massa?”. Você sabe suas opções, mas você tem apenas alguns segundos para escolher e você não sabe qual a aparência de sua escolha pois seu vizinho ainda não abriu o embrulho…


A aeromoça deste voo decidiu alterar o procedimento. Primeiro ela vai perguntar a todos os passageiros qual sua escolha de refeição, e depois vai checar se o número de refeições disponíveis neste voo para cada escolha é suficiente.


Por exemplo, considere que o número de refeições de frango, bife e massa disponíveis são respectivamente (80, 20, 40), enquanto o número de passageiros que escolheu frango, bife e massa seja respectivamente (45,23, 48). Neste caso, onze pessoas seguramente ficaram sem suas respectivas escolhas de refeição, já que três passageiros que queriam bife e oito que gostariam de massa não poderão ser atendidos.


Dada a quantidade de refeições disponíveis para cada escolha e o número de refeições pedidas para cada escolha, você poderia por favor ajudar a aeromoça a determinar quantos passageiros seguramente não poderão ser atendidos?

## Entrada

A primeira linha contem três inteiros **C_a**, **B_a** e **P_a** (0 ≤ **C_a**, **B_a**, **P_a** ≤ 100), representando respectivamente o número de refeições disponiveis de frango, bife e massa. A segunda linha contem três inteiros **C_r**, **B_r** e **P_r** (0 ≤ **C_r**, **B_r**, **P_r** ≤ 100), indicando respectivamente o número de refeições requisitadas de frango, bife e massa respectivamente.

## Saida

Imprima uma única linha com um inteiro representando o número de passageiros que seguramente não receberão sua escolha de refeição.

## Exemplo 1

**Entrada:**
```
80 20 40
45 23 48
```

**Saida:**
```
11
```

## Exemplo 2

**Entrada:**
```
0 0 0
100 100 100
```

**Saida:**
```
300
```

## Exemplo 3

**Entrada:**
```
41 42 43
41 42 43
```

**Saida:**
```
0
```
