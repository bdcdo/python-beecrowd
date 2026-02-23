# Como Usar Este Guia

## Navegação

Use o **menu lateral** para navegar entre os módulos e seções. Cada módulo começa com notebooks de conceitos e termina com listas de exercícios.

## Níveis de exercícios

Os exercícios estão organizados em 3 níveis progressivos:

| Nível | Objetivo | Quando fazer |
|-------|----------|--------------|
| **Básico** | Aplicar o conceito de forma direta | Assim que terminar de ler os conceitos |
| **Fixação** | Praticar variações e reforçar o aprendizado | Depois de resolver todos os básicos |
| **Aprofundamento** | Combinar conceitos e resolver problemas mais elaborados | Quando se sentir confiante nos níveis anteriores |

## Sobre o `input()` nos notebooks

```{admonition} Importante
:class: warning

Nos notebooks deste guia, **não usamos `input()` diretamente** porque ele bloqueia a execução automática das células. Em vez disso, simulamos a entrada com **atribuição direta**.
```

**No Beecrowd (código real):**
```python
N = int(input())
```

**No notebook (simulação):**
```python
# Simulando a entrada: N = 576
N = 576
```

Quando for resolver os exercícios no Beecrowd, use `input()` normalmente. Os notebooks servem para **entender o conceito** — a submissão no judge usa o padrão com `input()`.

## Receitas de input() para o Beecrowd

Copie e cole o padrão que se encaixa no seu problema:

**Ler 1 número inteiro:**
```python
N = int(input())
```

**Ler 1 número decimal:**
```python
X = float(input())
```

**Ler 1 texto:**
```python
S = input()
```

**Ler 2 inteiros na mesma linha:**
```python
A, B = map(int, input().split())
```

**Ler 3 decimais na mesma linha:**
```python
A, B, C = map(float, input().split())
```

**Ler 3 inteiros na mesma linha:**
```python
A, B, C = map(int, input().split())
```

## Dicas para aproveitar ao máximo

1. **Execute as células** — não apenas leia, execute cada célula e observe a saída
2. **Modifique os exemplos** — troque valores, teste casos diferentes
3. **Resolva antes de olhar** — tente resolver o exercício antes de consultar qualquer referência
4. **Use o Beecrowd** — submeta suas soluções no judge para validar
