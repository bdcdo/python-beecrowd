# 3162 - Comunicação Espacial

**Categoria:** Iniciante
**Assunto:** Matriz
**Nivel:** 4
**Autor:** Por Daniel Lago, CEFET-MG  Brazil
**Timelimit: 1**

---

## Descricao

O ano é 2337. Milhares de naves de tripulações humanas viajam pelo espaço de forma alucinada para lá e para cá. E o melhor: as naves conseguem se comunicar através de rádio, é possível até mesmo que tripulações entre naves distintas jogarem truco.


No entanto, infelizmente a qualidade do sinal esvanece com a distância. Enquanto naves próximas conseguem se comunicar bem, as naves que estão distantes possuem péssima intensidade de sinal para se comunicar. Por esse motivo, as naves comunicam-se preferencialmente com a nave mais próxima.


Considerando um trecho do espaço onde as naves podem ser consideradas pontos no espaço, portanto com coordenadas tridimensionais, com cada eixo podendo ter valor entre 0 e 100 u.m. Sabe-se que a intensidade do sinal de comunicação se dá pela distância entre as naves; de modo que naves que distam entre si até 20 u.m. possuem uma intensidade alta; acima de 20 u.m. e até 50 u.m. possuem uma intensidade média; enquanto a intensidade do sinal acima de 50 u.m. é tão baixa que não possibilita a comunicação entre as naves.


Dadas as informações passadas, ajude os tripulantes destas naves a conseguirem saber a intensidade do sinal entre cada uma delas e a nave mais próxima, para informá-los se eles vão conseguir ter uma boa comunicação entre si.

## Entrada

A primeira linha da entrada possui um número inteiro **N** (2 <= **N** <= 10), que representa o número de naves no espaço a ser analisado. As **N** linhas seguintes receberão 3 valores inteiros, separados por espaço, indicando as coordenadas discretas **x**, **y** e **z** de cada nave.

## Saida

Uma linha para cada nave, indicando uma letra para a intensidade de sinal entre ela e a nave mais próxima. “A” representa intensidade alta; “M” representa intensidade média e “B” representa intensidade baixa.

## Exemplo

**Entrada:**
```
4
50 55 55
15 28 79
45 48 37
25 50 32
```

**Saida:**
```
A
B
A
M
```
