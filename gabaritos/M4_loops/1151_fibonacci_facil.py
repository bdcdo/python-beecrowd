# ============================================================
# Beecrowd 1151 - Fibonacci Facil
# https://judge.beecrowd.com/pt/problems/view/1151
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Aprofundamento
# Conceitos:     for, range(), fibonacci, acumulador
# ============================================================

n = int(input())

a = 0
b = 1

numeros = []
for i in range(n):
    numeros.append(str(a))
    c = a + b
    a = b
    b = c

print(" ".join(numeros))
