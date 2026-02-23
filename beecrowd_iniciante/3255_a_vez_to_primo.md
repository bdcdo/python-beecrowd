# 3255 - A Vez to Primo

**Categoria:** Iniciante
**Assunto:** Prime Sieve of Erahosthenes
**Nivel:** 1
**Autor:** Por Jon Marius Venstad  Norway
**Timelimit: 1**

---

## Descricao

Odd e Even tiveram sua cota de diversão jogando o bom e velho jogo dos primos: eles começam com um número natural arbitrário e se revezam adicionando 1 ou dividindo por um primo (assumindo que o resultado ainda é um número natural), e o um chegar a 1 é o vencedor. No entanto, agora que eles têm um novo amigo, Ingmariay, eles decidiram expandir as regras do jogo para permitir a ação de três jogadores: em vez de determinar um vencedor para cada rodada do jogo, eles marcam pontos; o menor número que cada um deles reivindicou durante a rodada é a quantidade de pontos que eles obtêm. (Se algum deles não teve a oportunidade de reivindicar nenhum número, o número inicial será a pontuação dessa rodada.) No final do dia, o jogador com menos pontos vence. E para evitar desentendimentos entre si, todos concordaram que cada um deles se concentrará apenas em minimizar suas próprias pontuações, e que sempre que um jogador puder escolher números diferentes que resultarão na mesma pontuação, esse jogador
                    escolherá o menor deles números. Eles também concordaram com uma ordem fixa de jogo: Odd → Even → Ingmariay → ..., mas eles alternam quem começa.


Recentemente, você perdeu uma de suas noites emocionantes de jogo, porque teve que criar problemas para o evento NCPC. Felizmente para você, eles registraram os números e os jogadores iniciais de cada rodada e disseram que, como eles sempre jogam da melhor forma, você poderia usar isso para simular o evento para si mesmo. Oh, alegria!


Como uma rodada de exemplo, suponha que Even seja escolhido como o jogador inicial e com o número inicial 15. Então, Even reivindica 16, Ingmariay 8, Odd 4, Even 2 e Ingmariay 1. Odd recebe 4 pontos, Even 2 e Ingmariay 1.

## Entrada

A primeira linha de entrada contém um único inteiro **n** (1 ≤ **n** ≤ 1000), o número de rodadas que eles jogaram naquela noite.


Em seguida, siga **n** linhas, cada uma começando com o primeiro caractere do nome do jogador inicial ('O', 'E' ou 'I'), seguido por um espaço e, em seguida, o número inicial para essa rodada, no intervalo [1 , 10.000].


*Nota: Se o número inicial for 1, todos os jogadores recebem 0 pontos para essa rodada.*

## Saida

Imprima uma única linha com a pontuação no final do dia para cada um dos três competidores, na ordem ”Odd”, ”Even”, ”Ingmariay”.

## Exemplo 1

**Entrada:**
```
1
O 4
```

**Saida:**
```
2 1 4
```

## Exemplo 2

**Entrada:**
```
3
O 13
I 14
E 15
```

**Saida:**
```
6 29 16
```
