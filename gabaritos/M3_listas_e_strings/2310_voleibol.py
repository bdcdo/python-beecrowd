# ============================================================
# Beecrowd 2310 - Voleibol
# https://judge.beecrowd.com/pt/problems/view/2310
# ============================================================
# Modulo:        M3 - Listas e strings
# Classificacao: Fixacao
# Conceitos:     lista, split(), for (leitura), int(), f-string, acumuladores
# ============================================================

n = int(input())

total_saques = 0
total_bloqueios = 0
total_ataques = 0
sucesso_saques = 0
sucesso_bloqueios = 0
sucesso_ataques = 0

for i in range(n):
    nome = input()
    tentativas = input().split()
    s = int(tentativas[0])
    b = int(tentativas[1])
    a = int(tentativas[2])
    sucessos = input().split()
    s1 = int(sucessos[0])
    b1 = int(sucessos[1])
    a1 = int(sucessos[2])
    total_saques = total_saques + s
    total_bloqueios = total_bloqueios + b
    total_ataques = total_ataques + a
    sucesso_saques = sucesso_saques + s1
    sucesso_bloqueios = sucesso_bloqueios + b1
    sucesso_ataques = sucesso_ataques + a1

perc_saques = sucesso_saques / total_saques * 100
perc_bloqueios = sucesso_bloqueios / total_bloqueios * 100
perc_ataques = sucesso_ataques / total_ataques * 100

print(f"Pontos de Saque: {perc_saques:.2f} %.")
print(f"Pontos de Bloqueio: {perc_bloqueios:.2f} %.")
print(f"Pontos de Ataque: {perc_ataques:.2f} %.")
