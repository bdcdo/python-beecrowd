# ============================================================
# Beecrowd 1098 - Sequencia IJ 4
# https://judge.beecrowd.com/pt/problems/view/1098
# ============================================================
# Modulo:        M4 - Loops
# Classificacao: Aprofundamento
# Conceitos:     for, range(), loops aninhados, f-string, float
# ============================================================

for passo in range(11):
    i = passo * 2
    for k in range(1, 4):
        j = i + k * 10

        i_int = i % 10 == 0
        j_int = j % 10 == 0

        if i_int:
            parte_i = str(i // 10)
        else:
            parte_i = f"{i / 10:.1f}"

        if j_int:
            parte_j = str(j // 10)
        else:
            parte_j = f"{j / 10:.1f}"

        print(f"I={parte_i} J={parte_j}")
