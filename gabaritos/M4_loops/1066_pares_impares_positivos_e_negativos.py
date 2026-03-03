# ============================================================
# Beecrowd 1066 - Pares, Impares, Positivos e Negativos
# https://judge.beecrowd.com/pt/problems/view/1066
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Fixacao
# Conceitos:     for, range(), int(), input(), multiplos contadores, if/else, % (modulo)
# ============================================================

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if valor > 0:
        positivos = positivos + 1
    elif valor < 0:
        negativos = negativos + 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
