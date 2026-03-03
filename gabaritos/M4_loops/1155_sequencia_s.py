# ============================================================
# Beecrowd 1155 - Sequencia S
# https://judge.beecrowd.com/pt/problems/view/1155
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Basico
# Conceitos:     for, range(), acumulador, serie harmonica, formatacao
# ============================================================

s = 0.0

for i in range(1, 101):
    s = s + 1.0 / i

print(f"{s:.2f}")
