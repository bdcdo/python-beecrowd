# 3343 - Attack On Gasparini

**Categoria:** Iniciante
**Assunto:** Ad-Hoc
**Nivel:** 8
**Autor:** Por Eliton Machado, UDESC  Brazil
**Timelimit: 1**

---

## Descricao

O grandioso rei da ilha Paradis é avisado que os titãs estão organizando um ataque!


Os titãs possuem 3 tamanhos, titãs pequenos de **p** metros, titãs médios de **m** metros e titãs grandes de **g** metros. Vários titãs de diferentes tamanhos estão se organizando para um ataque, e o rei precisa construir várias muralhas de **x** metros para pará-los.


Felizmente o rei conhece a estratégia dos titãs, eles atacarão em sequência, um após o outro. Quando um titã de tamanho **k** encontra uma muralha uma das duas situações acontecem:


- Se a muralha for maior ou do mesmo tamanho que o titã, ele destrói **k** metros da muralha depois se cansa e morre, assim a muralha fica **k** metros mais baixa.
- Se a muralha for menor que o titã, ele pula aquela muralha e segue para a próxima.

O rei pede a você, conselheiro do rei, qual o menor número de muralhas que precisam ser construídas antes do ataque para parar o ataque dos titãs.

## Entrada

Na primeira linha seguirão 2 inteiros, **n** e **x**, separados por um espaço, que representam a quantidade de titãs que compõem o ataque e o tamanho das muralhas a serem construídas.


Na segunda linha segue uma string de tamanho **n**, composta pelos caracteres P, M e G, indicando o tamanho (pequeno, médio e grande respectivamente) do i-ésimo titã. O titã \(T_{i+1}\) atacara depois do titã \(T_i\).


Na terceira linha seguem 3 inteiros, **p**, **m** e **g**, que representam o tamanho de um titã pequeno, médio e grande respectivamente.


- \(1 \le n \le 3 \times 10^5\)
- \(1 \le x \le 10^5\)
- \(1 \le p \le m \le g \le x\)

## Saida

Baseado na descrição do problema, imprima a quantidade miníma de muralhas para parar o ataque dos titãs.

## Exemplo 1

**Entrada:**
```
3 20
MPG
3 8 10
```

**Saida:**
```
2
```

## Exemplo 2

**Entrada:**
```
8 20
MGGPGGGP
3 8 10
```

**Saida:**
```
4
```

## Exemplo 3

**Entrada:**
```
4 6
GPMP
3 4 5
```

**Saida:**
```
3
```
