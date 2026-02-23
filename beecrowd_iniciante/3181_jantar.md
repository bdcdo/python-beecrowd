# 3181 - Jantar

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 3
**Autor:** Por Andreas Björklund  Finland
**Timelimit: 1**

---

## Descricao

Por vários anos agora, a NCPC (Nordic Conference on Partitions and Combinatorics), ganhou um grande número de participantes. Este ano a equipe organizadora espera um recorde histórico na casa das centenas. Devido à política de organizar este evento de prestígio, o local da conferência foi decidido há muito tempo para ser no Grand Hôtel em Estocolmo. O hotel tem dois salões de jantar gigantes, mas infelizmente, cada uma dessas salas sozinhas só pode acomodar até dois terços dos participantes do NCPC, portanto, eles terão que ser divididos em dois grupos.


Esta restrição exige um pouco de reflexão em nome da equipe organizadora do jantar da conferência. Poderiam eles dividir os participantes em duas partes, sendo nenhuma delas maior que 2/3 do grupo todo, conhecendo algum método de divisão inteligente e adequado para a ocasião, onde eles poderiam contar aos participantes para sua diversão? Afinal, desde que haja alguma grande regra lógica para qual das duas salas de jantar você está sentado, você (como matemático) ficaria feliz! Eles pensaram por um tempo e surgiram com a seguinte ideia para a divisão:  Existe um ano **Y** e uma divisão de participantes em duas partes, de modo que cada par na primeira parte se reuniu pela primeira vez algum tempo antes do ano **Y**, e todo par da segunda parte se reuniu pela primeira vez algum depois do ano **Y**? Agora, isso claramente se qualificava como uma regra apropriada para todos eles, mas a questão era se isso seria possível?

## Entrada

A primeira linha da entrada consiste de um inteiro**N** (4 ≤ **N** ≤ 400), que é o número de participantes, e C, que é o número de primeiros encontros conhecidos. As próximas C linhas são no formato **A B Y**, que representa os participantes**A** e **B** (1 ≤ **A** < **B** ≤ **N**) que se encontraram pela primeira vez no ano **Y** (1948 ≤ **Y** < 2008). Nenhum par de participantes vai aparecer mais de uma vez na lista, e presume-se que cada par de participantes que não estejam na lista se reuniu apenas agora (no ano de 2008).

## Saida

Para cada caso de teste, imprima o menor ano **Y**, de modo que seja possível dividir os participantes em duas partes, onde nenhum dos quais contém mais de 2**N**/3 pessoas, de forma que todo mundo da primeira parte se encontrou pela primeira vez antes do ano **Y**, e todas as pessoas da segunda parte se encontraram pela primeira vez no ano **Y** ou depois. Se não houver esse ano, imprima a string “Impossible”.

## Exemplo 1

**Entrada:**
```
4 6
1 2 1987
2 3 1987
1 3 1987
2 4 1987
1 4 1987
3 4 1987
```

**Saida:**
```
Impossible
```

## Exemplo 2

**Entrada:**
```
6 3
1 2 1970
3 4 1980
5 6 1990
```

**Saida:**
```
1971
```
