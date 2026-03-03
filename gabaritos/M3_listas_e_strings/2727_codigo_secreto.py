# ============================================================
# Beecrowd 2727 - Codigo Secreto
# https://judge.beecrowd.com/pt/problems/view/2727
# ============================================================
# Modulo:        M3 - Listas e strings
# Classificacao: Aprofundamento
# Conceitos:     string, split(), len(), for (leitura), chr(), ord()
# ============================================================

while True:
    try:
        n = int(input())
    except EOFError:
        break
    for i in range(n):
        codigo = input()
        grupos = codigo.split()
        num_grupos = len(grupos)
        pontos_por_grupo = len(grupos[0])
        posicao = (num_grupos - 1) * 3 + (pontos_por_grupo - 1)
        letra = chr(ord('a') + posicao)
        print(letra)
