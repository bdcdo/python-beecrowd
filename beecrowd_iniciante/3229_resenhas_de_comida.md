# 3229 - Resenhas de Comida

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** By Unknown  Finland
**Timelimit: 1**

---

## Descricao

Frida é redatora da Cosmopolitan, que escreve resenhas de restaurantes. Ela gosta muito, mas parece que, ao longo dos anos, fez resenhas de todos os restaurantes do planeta. Agora é hora de subir um nível; ela vai fazer uma resenha da comida servida pelas companhias aéreas, para que os leitores possam tomar melhores decisões sobre os voos.


Seu chefe deu a ela uma lista de conexões de vôo que ela precisa revisar para a próxima edição da Cosmopolitan. Ela sabe que eles servem a mesma comida em ambas as direções em todos os voos, então ela só precisa comer uma vez. Ela percebeu que precisará pegar alguns voos adicionais, pois não pode fazer todas as avaliações usando apenas os voos da lista do chefe. Portanto, ela fez uma pesquisa rápida e fez uma lista de voos adicionais que ela poderia tomar. Ela não revisará a comida nesses voos; eles só serão usados para que ela faça todas as revisões.


O objetivo de Frida é fazer todas as avaliações gastando menos dinheiro nas passagens aéreas. Seu escritório fica em Estocolmo, então ela começa e termina sua jornada lá. Cada vôo é ida e volta entre duas cidades e tem um preço fixo em ambas as direções. Você pode presumir que é possível concluir todas as revisões usando alguns dos vôos adicionais.


Para os fins deste problema, ignoramos o preço que Frida tem de pagar pelo alojamento e também ignoramos os horários de partida e chegada dos voos, pressupondo que todos os voos são frequentemente e razoavelmente curtos. Focamos apenas no preço total dos voos.

## Entrada

A primeira linha contém 2 inteiros separados por espaço, **N** e **R**, (2 ≤ **N** ≤ 13, 0 ≤ **R** ≤ 78), onde **N** é o número de aeroportos mencionados na entrada e **R** é o número de voos a serem analisados. Os aeroportos são numerados 1, ..., **N** e Estocolmo tem o número 1.


As próximas **R** linhas descrevem os voos **R** a serem analisados. Cada linha contém 3 inteiros separados por espaço **a**, **b**, **c**, (1 ≤ **a**, **b** ≤ **N**, 1 ≤ **c** ≤ 10.000), onde **a**, **b** denotam 2 distintos aeroportos e **c** é o custo do voo em coroas suecas em ambas as direções. Nenhum par de 2 cidades é listado duas vezes.


A próxima linha contém um inteiro **F**, (0 ≤ **F** ≤ 200), o número de voos adicionais disponíveis. As próximas linhas **F** contêm descrições de voos no mesmo formato acima e pode haver mais voos entre um par de cidades. Você pode assumir que é possível fazer todas as avaliações usando alguns desses voos adicionais.

## Saida

Produza uma linha com um inteiro - o menor custo total das passagens aéreas, de forma que Frida possa fazer todas as revisões e voltar para Estocolmo.

## Exemplo 1

**Entrada:**
```
5 3
1 2 1000
2 3 1000
4 5 500
2
1 4 300
3 5 300
```

**Saida:**
```
3100
```

## Exemplo 2

**Entrada:**
```
6 5
1 2 1000
2 3 1000
1 3 1000
2 4 1000
5 6 500
2
2 5 300
4 6 300
```

**Saida:**
```
5100
```
