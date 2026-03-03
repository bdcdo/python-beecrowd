# ============================================================
# Beecrowd 1175 - Troca em Vetor I
# https://judge.beecrowd.com/pt/problems/view/1175
# ============================================================
# Modulo:        M3 - Listas e strings
# Classificacao: Fixacao
# Conceitos:     lista, for (leitura/impressao), indexing, troca de valores
# ============================================================

vetor = []
for i in range(20):
    valor = int(input())
    vetor.append(valor)

for i in range(10):
    vetor[i], vetor[19 - i] = vetor[19 - i], vetor[i]

for i in range(20):
    print(f"N[{i}] = {vetor[i]}")
