# 2758 - Entrada e Saída de Números Reais

**Categoria:** Iniciante
**Assunto:** Números Reais
**Nivel:** 4
**Autor:** Por Roberto A. Costa Jr, UNIFEI  Brazil
**Timelimit: 1**

---

## Descricao

O seu professor gostaria de fazer um programa com as seguintes características:


1. Crie duas variáveis para armazenar números reais de precisão simples;
2. Crie duas variáveis para armazenar números reais de precisão dupla;
3. Leia o primeiro número de precisão simples que sempre terá uma casa decimal;
4. Leia o segundo número de precisão simples que sempre terá duas casas decimais;
5. Leia o primeiro número de precisão dupla que sempre terá três casas decimais;
6. Leia o segundo número de precisão dupla que sempre terá quatro casas decimais;
7. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável lida no passo 4. Não esqueça de pular linha;
8. Imprima a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável lida no passo 5, uma virgula, um espaço em branco, a letra D, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável lida no passo 6. Não esqueça de pular linha;
9. Repita o procedimento 7, imprimindo os números com uma casa decimal;
10. Repita o procedimento 8, imprimindo os números com uma casa decimal;
11. Repita o procedimento 7, imprimindo os números com duas casas decimais;
12. Repita o procedimento 8, imprimindo os números com duas casas decimais;
13. Repita o procedimento 7, imprimindo os números com três casas decimais;
14. Repita o procedimento 8, imprimindo os números com três casas decimais;
15. Repita o procedimento 7, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E;
16. Repita o procedimento 8, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E;
17. Repita o procedimento 7, imprimindo somente a parte inteira do número;
18. Repita o procedimento 8, imprimindo somente a parte inteira do número.

## Entrada

A entrada consiste em vários arquivos de teste. Em cada arquivo de teste tem duas linhas. Na primeira linha tem dois números reais **A** e **B** **(-1000.0 ≤ A, B ≤ 1000.0)**, separados por espaço em branco. Na segunda linha tem dois números reais **C** e **D** **(-1000.0 ≤ C, D ≤ 1000.0)**, separados por espaço em branco. Conforme mostrado no exemplo de entrada a seguir.

## Saida

Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem doze linhas da forma descrita no item 7 e 8. Conforme mostra o exemplo de saída a seguir.

## Exemplo 1

**Entrada:**
```
1.2 3.45
3.451 3.4516
```

**Saida:**
```
A = 1.200000, B = 3.450000
C = 3.451000, D = 3.451600
A = 1.2, B = 3.5
C = 3.5, D = 3.5
A = 1.20, B = 3.45
C = 3.45, D = 3.45
A = 1.200, B = 3.450
C = 3.451, D = 3.452
A = 1.200E+00, B = 3.450E+00
C = 3.451E+00, D = 3.452E+00
A = 1, B = 3
C = 3, D = 3
```

## Exemplo 2

**Entrada:**
```
2127.9 -821.45
-1020.456 1352.4548
```

**Saida:**
```
A = 2127.899902, B = -821.450012
C = -1020.456000, D = 1352.454800
A = 2127.9, B = -821.5
C = -1020.5, D = 1352.5
A = 2127.90, B = -821.45
C = -1020.46, D = 1352.45
A = 2127.900, B = -821.450
C = -1020.456, D = 1352.455
A = 2.128E+03, B = -8.215E+02
C = -1.020E+03, D = 1.352E+03
A = 2128, B = -821
C = -1020, D = 1352
```
