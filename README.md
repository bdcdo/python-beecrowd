# Introdução a Python com Beecrowd

Material de aula interativo que combina explicações de conceitos Python com exercícios práticos da plataforma [Beecrowd](https://judge.beecrowd.com/). Construído com [Jupyter Book v2](https://mystmd.org/) e executável no navegador via JupyterLite.

**Site publicado:** [https://bdcdo.github.io/python-beecrowd/](https://bdcdo.github.io/python-beecrowd/)

## Estrutura do projeto

```
book/                         # Conteúdo do livro (MyST/Jupyter Book)
├── myst.yml                  # Configuração e TOC
├── intro.ipynb               # Página inicial
├── como_usar.ipynb           # Guia de uso
├── m1_variaveis_e_operacoes/ # Módulo 1
├── m2_condicionais/          # Módulo 2
├── m3_listas_e_strings/      # Módulo 3
└── m4_loops/                 # Módulo 4
gabaritos/                    # Soluções dos exercícios (não publicadas)
├── M1_variaveis_e_operacoes/
├── M2_condicionais/
├── M3_listas_e_strings/
├── M4_loops/
├── M5_dicionarios/
└── M6_funcoes/
scripts/                      # Scripts auxiliares (testes, CSV)
```

## Módulos implementados

| Módulo | Tema | Exercícios | Status |
|--------|------|:----------:|--------|
| **M1** | Variáveis e Operações | 40 | Publicado |
| **M2** | Condicionais | 25 | Publicado |
| **M3** | Listas e Strings | 16 | Publicado |
| **M4** | Loops | 35 | Publicado |

**Total: 116 exercícios** organizados por nível (Básico, Fixação, Aprofundamento).

## Planejamento: Módulos 5 e 6

### M5 — Dicionários

- **Gabaritos prontos:** 9 soluções em `gabaritos/M5_dicionarios/`
- **Temas previstos:** criação de `dict`, `.get()`, iteração com `.items()`, dicionários aninhados
- **Exercícios candidatos:** 1037, 1038, 1048, 1049, 1050, 1052, 2670, 2787
  - Vários são revisitações de problemas do M2 resolvidos com dicionários em vez de `if/elif`

### M6 — Funções

- **Gabaritos prontos:** 8 soluções em `gabaritos/M6_funcoes/`
- **Temas previstos:** `def`, `return`, parâmetros, refatoração de código existente
- **Exercícios candidatos:** 1043, 1071, 1078, 1151, 1153, 1160, 1164, 1165
  - Revisitações de problemas do M2 e M4, refatorados com funções

### Decisões pendentes

- **Curadoria de exercícios:** definir quais dos gabaritos entram em cada nível (Básico/Fixação/Aprofundamento)
- **Notebooks de conceitos:** decidir quantos notebooks por módulo e quais seções
- **Exercícios revisitados:** como anotar que um exercício já apareceu em módulo anterior (badge, nota de rodapé, etc.)

## Como visualizar o livro

### Pré-requisitos

- [Node.js](https://nodejs.org/) 18+

### Preview ao vivo

```bash
cd book
npx mystmd start
```

Abre o livro em `http://localhost:3000` com hot-reload.

### Build estático

```bash
cd book
npx mystmd build --html
```

O site gerado fica em `book/_build/html/`.
