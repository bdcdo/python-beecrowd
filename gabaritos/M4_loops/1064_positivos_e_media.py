# ============================================================
# Beecrowd 1064 - Positivos e Media
# https://judge.beecrowd.com/pt/problems/view/1064
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Fixacao
# Conceitos:     for, range(), float(), input(), acumulador, contador, if
# ============================================================

contador = 0
soma = 0.0

for i in range(6):
    valor = float(input())
    if valor > 0:
        contador = contador + 1
        soma = soma + valor

print(f"{contador} valores positivos")
print(f"{soma / contador:.1f}")
