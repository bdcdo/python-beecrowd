# 3250 - Problema no Elevador

**Categoria:** Iniciante
**Assunto:** BFS
**Nivel:** 1
**Autor:** Por Pål Grønås Drange  Norway
**Timelimit: 1**

---

## Descricao

Você está a caminho de sua primeira entrevista de emprego como testador de programa e já está atrasado. A entrevista é em um arranha-céu e você está no andar **s**, onde vê um elevador. Ao entrar no elvator, você aprende que ele possui apenas dois botões, marcados “UP **u**” e “DOWN **d**”. Você conclui que o botão UP leva o elevador **u** andares para cima (se não houver andares suficientes, pressionar o botão UP não faz nada, ou pelo menos é o que você supõe), enquanto o botão DOWN leva você **d** andares para baixo (ou nenhum se não houver o suficiente). Sabendo que a entrevista é no andar **g** e que há apenas **f** andares no prédio, você rapidamente decide escrever um programa que fornece a quantidade de apertos de botão que você precisa para executar. Se você simplesmente não conseguir chegar ao andar correto, seu programa é interrompido com a mensagem “use as escadas”.


Dada a entrada **f**, **s**, **g**, **u** e **d** (andares, início, meta, cima, baixo), encontre a sequência mais curta de pressionamentos de botão que você deve pressionar para ir de **s** para **g**, em um edifício de **f** andares, ou a saída “use as escadas” se você não puder ir de **s** para **g** pelo elevador fornecido.

## Entrada

A entrada consistirá em uma linha, ou seja, **f** **s** **g** **u** **d**, onde 1 ≤ **s**, **g** ≤ **f** ≤ 1000000 e 0 ≤ **u**, **d** ≤ 1000000. Os pisos são indexados em um, ou seja, se houver 10 andares, **s** e **g** estarão em [1, 10].

## Saida

Você deve responder com o número mínimo de empurrões que você deve fazer para ir de **s** para **g**, ou a saída "use the stairs" se for impossível dada a configuração do elevador.

## Exemplo 1

**Entrada:**
```
10 1 10 2 1
```

**Saida:**
```
6
```

## Exemplo 2

**Entrada:**
```
100 2 1 1 0
```

**Saida:**
```
use the stairs
```
