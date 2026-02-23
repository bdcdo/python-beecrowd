# 2774 - Precisão do Sensor

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 4
**Autor:** Por Adriene Magalhães, INATEL  Brazil
**Timelimit: 1**

---

## Descricao

O professor está te ensinando sobre sensores. Este é um elemento muito importante em diversas aplicações. Para aprender melhor os conceitos de precisão o professor pediu para realizar uma montagem prática do sensor Termo Ind v4.0 no novo laboratório de Automação.


Você como bom aluno anotou a fórmula para o cálculo da precisão de um sensor:


**σ=√∑QT1(Xi−¯¯¯¯¯X)2QT−1σ=∑1QT(Xi−X¯)2QT−1\sigma\;=\;\sqrt{\frac{\sum_1^{QT}\left(\;X_i-\overline X\;\right)^2}{QT-1}}**


Onde **QT** é a quantidade de vezes que foi realizado o teste, **XXX** o valor medido em cada teste e **¯¯¯¯¯XX¯\overline X** a média dos valores.


Para realizar o teste você ficou **H** horas fazendo testes, e a cada **M** minutos você verificou o valor **X** da temperatura entregue pelo sensor.


Agora que você tem as medidas, e como você tem a habilidade de programar, faça um programa que entregue a precisão do sensor.

## Entrada

Existem vários casos de teste, cada caso consiste de duas linhas. A primeira contém dois valores **H** e **M**. E a segunda consiste dos valores de ponto flutuante **Xi** indicando o valor de cada medida do sensor.


É garantido que haverão no mínimo 5 e no máximo 10^5 medidas por caso e que estes valores estão no intervalo [0, 255] com duas casas decimais.

## Saida

Para cada caso de teste, imprima uma única linha com um número indicando a precisão do sensor. O valor calculado deve ser apresentado com 5 dígitos após o ponto decimal.

## Exemplo

**Entrada:**
```
1 10
2.99 2.94 3.02 2.91 3.05 3.11
2 16
5.00 5.00 5.00 5.00 5.00 5.00 5.00
```

**Saida:**
```
0.07312
0.00000
```
