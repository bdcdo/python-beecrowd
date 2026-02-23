# Guia de Aprendizado Python - Beecrowd Iniciante

Repositorio com os **334 problemas** de nivel "Iniciante" do [Beecrowd](https://judge.beecrowd.com), organizados em markdown com descricao completa, exemplos de entrada/saida e metadados.

## Objetivo

Servir como base para um guia de aprendizado de Python, usando problemas praticos e progressivos do Beecrowd. Cada problema contem:

- Descricao completa do enunciado
- Especificacao de entrada e saida
- Exemplos com entrada e saida esperada
- Metadados (categoria, nivel, autor, time limit)

## Estrutura do Repositorio

```
README.md                  # Este arquivo
problems_list.json         # Lista completa dos 334 problemas (JSON)
beecrowd_iniciante/        # Problemas em markdown
  README.md                # Indice com tabela de todos os problemas
  1000_hello_world.md      # Problema 1000
  1001_extremamente_basico.md
  ...
scripts/                   # Scripts de scraping e utilidades
  parse_html_to_md.py      # Converte HTML -> Markdown
  scrape_html.py           # Scraper com Playwright (Python)
  scrape_problems.js       # Scraper HTTP direto (Node.js)
  download_missing.py      # Baixa HTML faltantes
  verify_completeness.py   # Verifica completude dos problemas
```

## Estatisticas

| Metrica | Valor |
|---------|-------|
| Total de problemas | 334 |
| Problemas com conteudo completo | 334 (100%) |
| Categorias principais | 8 |

### Distribuicao por Assunto

| Assunto | Quantidade |
|---------|:----------:|
| Sequencial | 21 |
| Selecao | 27 |
| Repeticao | 55 |
| Vetores | 10 |
| Matrizes | 17 |
| Ad-Hoc | 25 |
| Matematica | 4 |
| String | 2 |
| Saida | 9 |
| Outros | 164 |

## Como Usar

1. Navegue pela pasta [`beecrowd_iniciante/`](beecrowd_iniciante/) para ver os problemas
2. Use o [indice](beecrowd_iniciante/README.md) para encontrar problemas por ID ou nome
3. Consulte a tabela abaixo para encontrar problemas por assunto

## Trilha de Aprendizado Sugerida

1. **Hello World** - Comece pelo problema 1000
2. **Sequencial** - Operacoes basicas, variaveis, tipos de dados
3. **Selecao** - Condicionais (if/else)
4. **Repeticao** - Lacos (for/while)
5. **Vetores** - Listas e arrays
6. **Matrizes** - Listas bidimensionais
7. **Ad-Hoc** - Problemas variados que combinam conceitos

## Problemas por Assunto

### Sequencial (21 problemas)

| ID | Nome | Nivel |
|---:|------|:-----:|
| 1001 | [Extremamente Basico](beecrowd_iniciante/1001_extremamente_basico.md) | 4 |
| 1002 | [Area do Circulo](beecrowd_iniciante/1002_area_do_circulo.md) | 4 |
| 1003 | [Soma Simples](beecrowd_iniciante/1003_soma_simples.md) | 1 |
| 1004 | [Produto Simples](beecrowd_iniciante/1004_produto_simples.md) | 1 |
| 1005 | [Media 1](beecrowd_iniciante/1005_media_1.md) | 2 |
| 1006 | [Media 2](beecrowd_iniciante/1006_media_2.md) | 1 |
| 1007 | [Diferenca](beecrowd_iniciante/1007_diferenca.md) | 1 |
| 1008 | [Salario](beecrowd_iniciante/1008_salario.md) | 2 |
| 1009 | [Salario com Bonus](beecrowd_iniciante/1009_salario_com_bonus.md) | 2 |
| 1010 | [Calculo Simples](beecrowd_iniciante/1010_calculo_simples.md) | 3 |
| 1011 | [Esfera](beecrowd_iniciante/1011_esfera.md) | 2 |
| 1012 | [Area](beecrowd_iniciante/1012_area.md) | 2 |
| 1013 | [O Maior](beecrowd_iniciante/1013_o_maior.md) | 3 |
| 1014 | [Consumo](beecrowd_iniciante/1014_consumo.md) | 1 |
| 1015 | [Distancia Entre Dois Pontos](beecrowd_iniciante/1015_distancia_entre_dois_pontos.md) | 1 |
| 1016 | [Distancia](beecrowd_iniciante/1016_distancia.md) | 1 |
| 1017 | [Gasto de Combustivel](beecrowd_iniciante/1017_gasto_de_combustivel.md) | 1 |
| 1018 | [Cedulas](beecrowd_iniciante/1018_cedulas.md) | 4 |
| 1019 | [Conversao de Tempo](beecrowd_iniciante/1019_conversao_de_tempo.md) | 1 |
| 1020 | [Idade em Dias](beecrowd_iniciante/1020_idade_em_dias.md) | 2 |
| 1021 | [Notas e Moedas](beecrowd_iniciante/1021_notas_e_moedas.md) | 6 |

### Selecao (27 problemas)

| ID | Nome | Nivel |
|---:|------|:-----:|
| 1035 | [Teste de Selecao 1](beecrowd_iniciante/1035_teste_de_selecao_1.md) | 2 |
| 1036 | [Formula de Bhaskara](beecrowd_iniciante/1036_formula_de_bhaskara.md) | 3 |
| 1037 | [Intervalo](beecrowd_iniciante/1037_intervalo.md) | 3 |
| 1038 | [Lanche](beecrowd_iniciante/1038_lanche.md) | 1 |
| 1040 | [Media 3](beecrowd_iniciante/1040_media_3.md) | 5 |
| 1041 | [Coordenadas de um Ponto](beecrowd_iniciante/1041_coordenadas_de_um_ponto.md) | 3 |
| 1042 | [Sort Simples](beecrowd_iniciante/1042_sort_simples.md) | 2 |
| 1043 | [Triangulo](beecrowd_iniciante/1043_triangulo.md) | 2 |
| 1044 | [Multiplos](beecrowd_iniciante/1044_multiplos.md) | 2 |
| 1045 | [Tipos de Triangulos](beecrowd_iniciante/1045_tipos_de_triangulos.md) | 4 |
| 1046 | [Tempo de Jogo](beecrowd_iniciante/1046_tempo_de_jogo.md) | 2 |
| 1047 | [Tempo de Jogo com Minutos](beecrowd_iniciante/1047_tempo_de_jogo_com_minutos.md) | 9 |
| 1048 | [Aumento de Salario](beecrowd_iniciante/1048_aumento_de_salario.md) | 2 |
| 1049 | [Animal](beecrowd_iniciante/1049_animal.md) | 3 |
| 1050 | [DDD](beecrowd_iniciante/1050_ddd.md) | 2 |
| 1051 | [Imposto de Renda](beecrowd_iniciante/1051_imposto_de_renda.md) | 2 |
| 1052 | [Mes](beecrowd_iniciante/1052_mes.md) | 2 |
| 1061 | [Tempo de um Evento](beecrowd_iniciante/1061_tempo_de_um_evento.md) | 3 |
| 1828 | [Bazinga!](beecrowd_iniciante/1828_bazinga.md) | 4 |
| 1983 | [O Escolhido](beecrowd_iniciante/1983_o_escolhido.md) | 2 |
| 2057 | [Fuso Horario](beecrowd_iniciante/2057_fuso_horario.md) | 2 |
| 2313 | [Qual Triangulo](beecrowd_iniciante/2313_qual_triangulo.md) | 3 |
| 2344 | [Notas da Prova](beecrowd_iniciante/2344_notas_da_prova.md) | 1 |
| 2670 | [Maquina de Cafe](beecrowd_iniciante/2670_maquina_de_cafe.md) | 3 |
| 2702 | [Escolha Dificil](beecrowd_iniciante/2702_escolha_dificil.md) | 1 |
| 2780 | [Basquete de Robos](beecrowd_iniciante/2780_basquete_de_robos.md) | 1 |
| 2787 | [Xadrez](beecrowd_iniciante/2787_xadrez.md) | 1 |

### Repeticao (55 problemas)

| ID | Nome | Nivel |
|---:|------|:-----:|
| 1059 | [Numeros Pares](beecrowd_iniciante/1059_numeros_pares.md) | 1 |
| 1060 | [Numeros Positivos](beecrowd_iniciante/1060_numeros_positivos.md) | 1 |
| 1064 | [Positivos e Media](beecrowd_iniciante/1064_positivos_e_media.md) | 2 |
| 1065 | [Pares entre Cinco Numeros](beecrowd_iniciante/1065_pares_entre_cinco_numeros.md) | 1 |
| 1066 | [Pares, Impares, Positivos e Negativos](beecrowd_iniciante/1066_pares_impares_positivos_e_negativos.md) | 1 |
| 1067 | [Numeros Impares](beecrowd_iniciante/1067_numeros_impares.md) | 2 |
| 1070 | [Seis Numeros Impares](beecrowd_iniciante/1070_seis_numeros_impares.md) | 1 |
| 1071 | [Soma de Impares Consecutivos I](beecrowd_iniciante/1071_soma_de_impares_consecutivos_i.md) | 2 |
| 1072 | [Intervalo 2](beecrowd_iniciante/1072_intervalo_2.md) | 1 |
| 1073 | [Quadrado de Pares](beecrowd_iniciante/1073_quadrado_de_pares.md) | 1 |
| 1074 | [Par ou Impar](beecrowd_iniciante/1074_par_ou_impar.md) | 2 |
| 1075 | [Resto 2](beecrowd_iniciante/1075_resto_2.md) | 2 |
| 1078 | [Tabuada](beecrowd_iniciante/1078_tabuada.md) | 1 |
| 1079 | [Medias Ponderadas](beecrowd_iniciante/1079_medias_ponderadas.md) | 1 |
| 1080 | [Maior e Posicao](beecrowd_iniciante/1080_maior_e_posicao.md) | 2 |
| 1094 | [Experiencias](beecrowd_iniciante/1094_experiencias.md) | 3 |
| 1095-1099 | Sequencia IJ 1-4, Soma Impares II | 1-2 |
| 1101 | [Sequencia de Numeros e Soma](beecrowd_iniciante/1101_sequencia_de_numeros_e_soma.md) | 4 |
| 1113-1118 | Crescente/Decrescente, Senha, Quadrante, Validacao | 1-3 |
| 1131-1134 | Grenais, Multiplos 13, Resto, Combustivel | 1-3 |
| 1142-1146 | PUM, Quadrado/Cubo, Sequencias Logicas | 1-3 |
| 1149-1165 | Somando, Fibonacci, Fatorial, Sequencias, Primos | 1-5 |
| 1541 | [Construindo Casas](beecrowd_iniciante/1541_construindo_casas.md) | 2 |
| 1564 | [Vai Ter Copa?](beecrowd_iniciante/1564_vai_ter_copa.md) | 2 |
| 1589 | [Bob Conduite](beecrowd_iniciante/1589_bob_conduite.md) | 1 |
| 2311 | [Saltos Ornamentais](beecrowd_iniciante/2311_saltos_ornamentais.md) | 2 |
| 2483 | [Feliz Nataaal!](beecrowd_iniciante/2483_feliz_nataaal.md) | 1 |

### Vetores (10 problemas)

| ID | Nome | Nivel |
|---:|------|:-----:|
| 1172-1180 | Substituicao, Preenchimento, Selecao, Troca, Fibonacci em Vetor | 1-3 |
| 2310 | [Voleibol](beecrowd_iniciante/2310_voleibol.md) | 2 |

### Matrizes (17 problemas)

| ID | Nome | Nivel |
|---:|------|:-----:|
| 1181-1190 | Linha, Coluna, Diagonais, Areas da Matriz | 1-4 |
| 1435 | [Matriz Quadrada I](beecrowd_iniciante/1435_matriz_quadrada_i.md) | 2 |
| 1478 | [Matriz Quadrada II](beecrowd_iniciante/1478_matriz_quadrada_ii.md) | 1 |
| 1534 | [Matriz 123](beecrowd_iniciante/1534_matriz_123.md) | 1 |
| 1557 | [Matriz Quadrada III](beecrowd_iniciante/1557_matriz_quadrada_iii.md) | 1 |
| 1827 | [Matriz Quadrada IV](beecrowd_iniciante/1827_matriz_quadrada_iv.md) | 1 |
| 2542 | [Iu-Di-Oh!](beecrowd_iniciante/2542_iu_di_oh.md) | 4 |
| 2552 | [PaodeQuejoSweeper](beecrowd_iniciante/2552_paodequejosweeper.md) | 2 |

> Para a lista completa de todos os 334 problemas, consulte o [indice em beecrowd_iniciante/README.md](beecrowd_iniciante/README.md).

## Status do Projeto

- [x] Lista de 334 problemas iniciantes catalogados
- [x] HTML de todos os problemas baixados
- [x] Conversao para Markdown com descricao, entrada, saida e exemplos
- [x] Organizacao por assunto/categoria
- [ ] Gabaritos em Python para cada problema
- [ ] Material teorico para cada topico (sequencial, selecao, etc.)
