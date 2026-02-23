# 2203 - Tempestade de Corvos

**Categoria:** Iniciante
**Assunto:** Iniciante, Distância entre …
**Nivel:** 4
**Autor:** Por Ícaro Dantas, UFCG  Brazil
**Timelimit: 1**

---

## Descricao

Fiddlesticks é um campeão do jogo League of Legends e tem como sua habilidade ultimate a "Tempestade de Corvos", ela funciona da seguinte maneira:


Primeiro Fiddlesticks escolhe um local estratégico e prontamente ele se prepara para ressurgir em uma direção até uma certa distância, então ele se enraiza e canaliza a ultimate por exatamente 1.5 segundos, após esse tempo ele ressurge imediatamente no local alvo com uma revoada de corvos voando ao seu redor e causando muito dano.


Fiddlesticks quer sua ajuda para saber se de uma certa posição é possível atingir um invasor com sua habilidade ultimate.


Obs: Considere que Fiddlesticks sempre luta exatamente na direção do invasor e o invasor sempre tenta fugir na direção contrária a Fiddlesticks, em velocidade constante.


![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2203.png)

## Entrada

A entrada é composta de várias linhas, cada linha contém os seguintes valores inteiros: **X_f**, **Y_f**, **X_i**, **Y_i**,**V_i**, **R_1** e **R_2**(0 ≤ **X_f**, **Y_f**, **X_i**, **Y_i**,**_ V**_i,_ **R_1** e **R_2** ≤ 100), representando respectivamente as coordenadas de Fiddlesticks, as coordenadas iniciais do invasor, a velocidade do invasor, o raio de conjuração da ultimate e o raio de voo dos corvos. Considere a unidade de medida como sendo o metro.

## Saida

Na saída você deve imprimir para cada linha o caractere 'Y' caso seja possível atingir o invasor ou 'N' caso contrário, ambos seguidos de uma quebra de linha.

## Exemplo

**Entrada:**
```
4 6 22 6 0 16 2
4 6 22 6 1 16 2
```

**Saida:**
```
Y
N
```
