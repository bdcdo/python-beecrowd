# 3042 - Desviando de Árvores de Natal

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 7
**Autor:** Por Gerson Groth, URI  Brazil
**Timelimit: 1**

---

## Descricao

Papai Noel adora jogos de celular, especialmente se forem com temas natalinos. Ele acaba de instalar um novo jogo para seu celular. O jogo consiste em um personagem correndo infinitamente em um caminho composto de três pistas, tendo que trocar de pista para desviar de obstáculos (árvores de natal) que aparecem no caminho. O personagem sempre começa um jogo na pista do meio, sendo necessário que Papai Noel toque uma vez do lado esquerdo da tela do celular para o personagem se deslocar uma pista para a esquerda e um toque do lado direito da tela para se deslocar uma pista para o lado direito. Ou seja, se o personagem estiver na pista mais à esquerda, precisará de 2 toques do lado direito para chegar até a pista mais à direita.

                    Apesar de parecer simples, Papai Noel está tendo dificuldades em permanecer vivo por muito tempo. Uma coisa que ele notou durante o jogo é que, sempre que há obstáculos, somente uma das pistas está livre para atravessar, enquanto que as outras duas possuem árvores de natal bloqueando os caminhos. Como vocês são grandes amigos, ele pediu sua ajuda para escrever um programa que minimize o número de toques necessários na tela para que ele consiga percorrer M metros no jogo.

## Entrada

A entrada consiste de vários casos de teste. A primeira linha de um caso de teste contém um inteiro **M** (0 ≤ **M** < 10000), representando a distância, em metros, que Papai Noel deseja jogar. As próxima **M** linhas contém, cada uma, 3 inteiros **L**,**C**,**R** representando a pista da esquerda, centro e direita, respectivamente (0 ≤ **L,C,R** ≤ 1). As pistas contém apenas o número 0, caso não tenha nenhum obstáculo, e o número 1, caso haja uma árvore de natal na pista. É garantido que ao menos uma pista sempre estará livre para o personagem passar. Assuma que Papai Noel sempre consegue tocar rápido o suficiente na tela para sair da esquerda até a direita, ou da direita até a esquerda de uma entrada até a outra. O final da entrada é indicado por uma linha que contém apenas um zero.

## Saida

Para cada caso de teste, seu programa deve imprimir uma única linha contendo o menor número de toques na tela que Papai Noel deve fazer para percorrer a distância desejada desviando de todos os obstáculos.

## Exemplo

**Entrada:**
```
5
0 0 0
1 1 0
0 0 0
0 0 0
1 0 1
0
```

**Saida:**
```
2
```
