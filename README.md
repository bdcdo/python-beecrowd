# Guia de Python com Beecrowd

Material de aula interativo para alunos de Direito que combina explicações de conceitos Python com exercícios práticos da plataforma [Beecrowd](https://judge.beecrowd.com/). Construído como um [Jupyter Book v2](https://mystmd.org/) com notebooks executáveis.

## Estrutura do livro

| Módulo | Tema | Exercícios |
|--------|------|:----------:|
| **Módulo 1** | Variáveis e Operações | 37 |
| **Módulo 2** | Condicionais | 29 |
| **Módulo 3** | Listas e Strings | 18 |

Cada módulo contém notebooks de conceitos e uma lista de exercícios Beecrowd classificados em 3 níveis (Básico, Fixação, Aprofundamento). **84 exercícios** no total.

## Como visualizar o livro

### Pré-requisitos

- [Node.js](https://nodejs.org/) 18+

### Preview ao vivo

Todos os comandos devem ser executados de dentro do diretório `book/`:

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

## Banco de problemas

O diretório `beecrowd_iniciante/` contém os **334 problemas** de nível Iniciante do Beecrowd em Markdown, com descrição completa, entrada/saída e exemplos. Veja o [índice completo](beecrowd_iniciante/README.md).

## Status do projeto

- [x] 334 problemas Beecrowd catalogados em Markdown
- [x] Jupyter Book v2 com 3 módulos de ensino
- [x] Notebooks interativos de conceitos
- [x] Exercícios organizados por módulo e nível
- [ ] Gabaritos em Python para cada problema
