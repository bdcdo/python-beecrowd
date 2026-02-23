# 3164 - Fiscalizando Empresa

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** Por Elder Sobrinho, UFTM  Brazil
**Timelimit: 3**

---

## Descricao

Mario é fiscal do meio ambiente, todo dia ele visita uma empresa e solicita a eles uma lista contendo o peso das árvores cortadas pela empresa nos últimos 30 dias. Por meio da observação empírica, sabe-se que os dados sempre seguem uma distribuição normal e a empresa pagará uma multa **X** quando o conjunto de dados apresentar valores extremos conforme regras estatísticas do gráfico boxplot. Sendo que **X** é calculado da seguinte forma: **X = PV**, onde **P** é o número de observações consideradas extremas pelo boxplot e **V** é o valor unitário da penalidade estabelecida na normativa de fiscalização. Sua tarefa é calcular o valor da multa conforme um dado conjunto de dados e o valor unitário da multa.


**Background p/ Boxplot:**


O boxplot (gráfico de caixa) é um gráfico utilizado para avaliar a distribuição empírica de um conjunto de dados. Este é formado pelo primeiro e terceiro quartil, apresentando a mediana (**Q_2**) entre estes quartis (veja figura abaixo). As hastes inferiores e superiores que se estendem do quartil inferior (**Q_1**) e do quartil superior (**Q_3**), denotam os limites mínimos e máximos. Portanto, valores fora desta faixa são considerados valores extremos (outliers).


![3462_a.png](https://resources.beecrowd.com/gallery/images/contests/3462_a.png)


Em síntese, os quartis são valores dados a partir de um conjunto de observações ordenadas em ordem crescente, que dividem a distribuição em quatro partes iguais. O primeiro quartil, **Q_1**, é o número que deixa 25% das observações abaixo e 75% acima, enquanto que o terceiro quartil, **Q_3**, deixa 75% das observações abaixo e 25% acima. Já **Q_2** é a mediana, deixa 50% das observações abaixo e 50% das observações acima. A figura abaixo demonstra essa relação conforme a distribuição dos dados, neste caso, uma distribuição normal.


![3462_b.png](https://resources.beecrowd.com/gallery/images/contests/3462_b.png)


De forma objetiva, o cálculo dos limiares (**Q_1**, **Q_2** e **Q_3**) do boxplot é dado por:  Seja ***n*** o número total de elementos da amostra, calcule **j(n+1)/4**, para **j**=1,2 e 3. Desta forma **Q_j** será um elemento entre **X_k** e **X_k+1**, onde **k** é o maior inteiro menor ou igual a **j(n+1)/4** e será calculado da seguinte forma:


![3462_c.png](https://resources.beecrowd.com/gallery/images/contests/3462_c.png)


Podemos observar que quando **k** é um valor inteiro, o quantil será o próprio **X_k**, isto é, **Q_j = X_k**, onde:


![3462_d.png](https://resources.beecrowd.com/gallery/images/contests/3462_d.png)


Além disso, o limite inferior e superior do boxplot é calculado como:  **Q_1 – 1.5(Q_3 – Q_1)** e **Q_3 – 1.5(Q_3 – Q_1).**

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso contém dois números **N** (1 ≤ **N** ≤ 10^6) e **P** (1 ≤ **P** ≤ 10^6), representando a quantidade de elementos da lista que contém os pesos das árvores cortadas e o valor unitário da penalidade estabelecida na normativa de fiscalização, respectivamente. A segunda linha de cada caso contém os ***n***-ésimos pesos das árvores cortadas pela empresa (0 ≤ **n_i** ≤ 90000). A entrada termina com fim-de-arquivo (EOF).

## Saida

Para cada caso de teste, imprima o valor da multa **X_i** que a empresa irá pagar (0 ≤ **X_i** ≤ 10^9).

## Exemplo

**Entrada:**
```
27 350
836962 670005 760702 418543 305993 586022 439392 806735 789441 805297 693606 641947 731631 762916 687297 577964 608574 338189 742702 740253 414602 422863 842306 796430 783221 410343 507054
125 1846
466565 533097 662830 747738 538861 785591 732920 516169 381282 332191 650453 511281 512419 407361 629718 496882 687915 466148 658433 330061 602968 695330 400290 877885 450114 803743 563465 545334 630502 740911 616578 536530 730177 647438 602675 488436 644958 743645 746834 606122 640365 431670 453651 581547 736512 588121 425169 484183 518946 326952 304295 507567 560948 413374 609377 318756 387983 669662 559285 713625 470320 486861 597232 587713 395933 797989 876572 575586 879872 694684 766020 692250 707191 873597 344292 564383 525518 806957 669805 829583 330544 670811 742504 591918 852958 788451 650196 435672 413123 585054 424806 691486 708922 592543 372976 692536 630824 569753 724519 718326 402952 794537 503779 675800 386097 809345 662112 468372 474019 671663 464763 814395 547938 890146 472567 557276 578567 790490 595460 330056 734208 480924 552863 821822 686318
```

**Saida:**
```
0
27690
```
