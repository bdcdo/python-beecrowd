# 2313 - Qual Triângulo

**Categoria:** Iniciante
**Assunto:** Seleção
**Nivel:** 3
**Autor:** Por Alexandre A. Melo, IFSC  Brazil
**Timelimit: 1**

---

## Descricao

Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno, isóceles ou equilátero e se trata-se de um triângulo retângulo ou não.

## Entrada

A entrada consiste em três números inteiros **A**,**B** e **C**(0 < **A**,**B**,**C** < 10^5).

## Saida

A saída deve conter a string **"Invalido"** se os valores lidos não formarem um triângulo. Se os valores formarem um triângulo a saída deve ser **"Valido-Equilatero"**, **"Valido-Escaleno"** ou **"Valido-Isoceles"** de acordo com a característica do triângulo seguido de **"Retangulo: S"** se o triângulo for retângulo ou **"Retangulo: N"** se não for, conforme os exemplos.

## Exemplo 1

**Entrada:**
```
4 6 2
```

**Saida:**
```
Invalido
```

## Exemplo 2

**Entrada:**
```
4 3 3
```

**Saida:**
```
Valido-Isoceles
Retangulo: N
```

## Exemplo 3

**Entrada:**
```
3 4 5
```

**Saida:**
```
Valido-Escaleno
Retangulo: S
```
