# 2486 - C Mais ou Menos?

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 3
**Autor:** Por João Marcos Salvanini Bellini de Moraes, IFSULDEMINAS  Brazil
**Timelimit: 1**

---

## Descricao

Ultimamente, diversas pessoas estão indo à Dra. Cláudia Café com Leite para saber se estão consumindo a quantidade recomendada diária de vitamina C. Isso tem a deixado exausta, e por isso ela lhe pediu para escrever um programa que, dado o consumo diário de alimentos ricos em vitamina C por uma pessoa, indique o quanto essa pessoa deve consumir a mais ou a menos para atingir o recomendado.


Para tal, você poderá utilizar a tabela a seguir:



                    .cmm {
                        border: 1px solid #c0c0c0;
                        border-collapse: collapse;
                        padding: 5px;
                        width: 100%;
                    }
                    .cmm th {
                        border: 1px solid #c0c0c0;
                        padding: 5px;
                        background: #f0f0f0;
                    }
                    .cmm td {
                        border: 1px solid #c0c0c0;
                        text-align: center;
                        padding: 5px;
                    }
                    .desc-example {
                        font-family: "Courier New", Courier, "Nimbus Mono L", monospace;
                    }
                



Alimentos ricos em Vitamina C
Quantidade de Vitamina C




suco de laranja
120 mg


morango fresco
85 mg


mamao
85 mg


goiaba vermelha
70 mg


manga
56 mg


laranja
50 mg


brocolis
34 mg




Considere que o consumo diário recomendado de vitamina C está entre 110 mg e 130 mg, inclusive.

## Entrada

Cada caso de teste é composto um inteiro **T** (1 ≤ **T** ≤ 7) indicando que a pessoa consome diariamente **T** alimentos entre os 7 alimentos da tabela. Em seguida, haverá **T** linhas com um inteiro **N** e um alimento (totalmente em caixa baixa e sem acentuações), indicando que a pessoa consome uma quantidade **N**daquele alimento. A entrada termina com **T** = 0.

## Saida

Para cada caso de teste (**T**), se o consumo ultrapassou o limite recomendado, imprima "Menos X mg", em que X representa a quantidade a menos a ser consumida para atingir o limite recomendado; se o consumo não atingiu o recomendado, imprima "Mais X mg", em que X representa a quantidade a mais para atingir o recomendado; se o consumo está dentro do intervalo recomendado, imprima "X mg", em que X representa a quantidade consumida diariamente pela pessoa.

## Exemplo 1

**Entrada:**
```
suco de laranja
```

**Saida:**
```
120 mg
```

## Exemplo 2

**Entrada:**
```
morango fresco
```

**Saida:**
```
85 mg
```

## Exemplo 3

**Entrada:**
```
mamao
```

**Saida:**
```
85 mg
```

## Exemplo 4

**Entrada:**
```
goiaba vermelha
```

**Saida:**
```
70 mg
```

## Exemplo 5

**Entrada:**
```
manga
```

**Saida:**
```
56 mg
```

## Exemplo 6

**Entrada:**
```
laranja
```

**Saida:**
```
50 mg
```

## Exemplo 7

**Entrada:**
```
brocolis
```

**Saida:**
```
34 mg
```

## Exemplo 8

**Entrada:**
```
2
2 suco de laranja
3 mamao
1
3 brocolis
2
1 manga
1 laranja
1
1 suco de laranja
0
```

**Saida:**
```
Menos 365 mg
Mais 8 mg
Mais 4 mg
120 mg
```
