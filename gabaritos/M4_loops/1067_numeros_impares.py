# ============================================================
# Beecrowd 1067 - Numeros Impares
# https://judge.beecrowd.com/pt/problems/view/1067
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Basico
# Conceitos:     for, range(), int(), input(), if, % (modulo)
# ============================================================

x = int(input())

for numero in range(1, x + 1):
    if numero % 2 != 0:
        print(numero)
