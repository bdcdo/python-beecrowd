# 2823 - Eearliest Deadline First

**Categoria:** Iniciante
**Assunto:** -
**Nivel:** 4
**Autor:** Por Emilio Wuerges, UFFS  Brazil
**Timelimit: 1**

---

## Descricao

Neste problema o seu trabalho é verificar se um conjunto de processos periódicos que possuem restrição de tempo-real pode ser escalonado.


Um processo de tempo real é caracterizado por dois números. O primeiro é o custo computacional do processo. Ou seja, o tempo que o processo gasta quando entrar em execução. O segundo número é o período em que o processo executa. Ou seja, a cada período de tempo, o processo reinicia.


O conjunto será escalonado usando o algoritmo EDF (Earliest Deadline First). Sabe-se que o algoritmo EDF é ótimo. Ou seja, se um conjunto de tarefas não poder ser escalonado pelo EDF, ele não poderá ser escalonado por nenhum outro algoritmo.


O sistema operacional que receberá estas tarefas está rodando em uma máquina single core. As tarefas são preemptáveis. Isto é uma tarefa pode tomar o lugar de outra durante a execução, se for necessário.


Considere que o custo de trocar entre tarefas é 0.

## Entrada

A primeira linha da entrada possui um valor \(1 \leq N \leq 10\), que é número de processos a ser avaliado.


Cada **N** linha seguinte representa um processo, e contém 2 valores \(1 \leq C \leq 5\) e \(C \leq P \leq 100\), que representam o custo computacional e o período de cada processo, respectivamente.

## Saida

A saída consiste de uma única linha, contendo ou o string **OK** ou do string **FAIL**, caso o escalonamento seja possível ou não, respectivamente.

## Exemplo 1

**Entrada:**
```
2
3 5
2 5
```

**Saida:**
```
OK
```

## Exemplo 2

**Entrada:**
```
4
1 5
4 9
5 15
2 45
```

**Saida:**
```
FAIL
```
