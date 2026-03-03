# ============================================================
# Beecrowd 1095 - Sequencia IJ 1
# https://judge.beecrowd.com/pt/problems/view/1095
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Aprofundamento
# Conceitos:     for, range(), loops aninhados, f-string
# ============================================================

j = 60
for i in range(1, 62, 3):
    if j < 0:
        break
    print(f"I={i} J={j}")
    j = j - 5
