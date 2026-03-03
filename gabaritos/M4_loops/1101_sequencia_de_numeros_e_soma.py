# ============================================================
# Beecrowd 1101 - Sequencia de Numeros e Soma
# https://judge.beecrowd.com/pt/problems/view/1101
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Aprofundamento
# Conceitos:     while, break, for, range(), acumulador
# ============================================================

while True:
    m, n = input().split()
    m = int(m)
    n = int(n)

    if m <= 0 or n <= 0:
        break

    menor = min(m, n)
    maior = max(m, n)

    soma = 0
    numeros = []
    for i in range(menor, maior + 1):
        numeros.append(str(i))
        soma = soma + i

    print(" ".join(numeros) + f" Sum={soma}")
