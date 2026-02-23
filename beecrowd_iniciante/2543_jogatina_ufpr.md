# 2543 - Jogatina UFPR

**Categoria:** Iniciante
**Assunto:** Iniciante
**Nivel:** 1
**Autor:** Por Ricardo Oliveira, UFPR  Brazil
**Timelimit: 1**

---

## Descricao

Assim como a maioria dos estudantes de computação, você vive jogando os jogos eletrônicos mais populares atualmente: Liga of Legendas (LOL) e Contra-Strike (CS). Embora você também jogue LOL, você gosta mais é de usar todas suas grandes habilidades para derrotar a equipe terrorista em Contra-Strike! Você é tão empenhado no combate ao terror que é frequentemente comparado com o presidente dos EUA que anunciou a captura e derrota de um grande terrorista da vida real.


Por ser bastante habilidoso, os vídeos de suas jogadas (seus famosos *gameplays*) vivem aparecendo na *Jogatina UFPR*, uma página na internet que publica *gameplays* de alunos da universidade.


A página publica muitos vídeos diariamente. Por isso, pode ser dificil encontrar e contar todos os seus vídeos na página. Entretanto, como você também é programador, você decidiu escrever um programa para auxiliá-lo nesta tarefa. Dada a lista de *gameplays* publicados na página, determine quantos *gameplays* seus de Contra-Strike foram publicados.

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso contém dois inteiros **N** e **I** (1 ≤ **N** ≤ 10^4, 1000 ≤ **I** ≤ 9999), o número de *gameplays* publicados na página e o seu identificador na universidade, respectivamente.


As próximas **N** linhas descrevem os *gameplays* publicados. Cada *gameplay* é descrito por dois inteiros **i** e **j** (1000 ≤ **i** ≤ 9999, **j**=0 ou 1), onde **i** é o identificador na universidade do autor do *gameplay*, e **j**=0 se o *gameplay* é de Contra-Strike, ou **j**=1 se é de Liga of Legendas.


A entrada termina com fim-de-arquivo (EOF).

## Saida

Para cada caso de teste, imprima uma única linha com um número indicando quantos *gameplays* seus de Contra-Strike foram publicados na página.

## Exemplo

**Entrada:**
```
7 5558
5693 1
5558 0
6009 1
5558 1
1566 0
5558 0
8757 1
```

**Saida:**
```
2
```
