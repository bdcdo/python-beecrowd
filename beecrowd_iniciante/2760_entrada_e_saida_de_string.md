# 2760 - Entrada e Saída de String

**Categoria:** Iniciante
**Assunto:** String
**Nivel:** 5
**Autor:** Por Roberto A. Costa Jr, UNIFEI  Brazil
**Timelimit: 1**

---

## Descricao

O seu professor gostaria de fazer um programa com as seguintes características:


1. Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
2. Leia uma frase para a primeira variável;
3. Leia uma frase para a segunda variável;
4. Leia uma frase para a terceira variável;
5. Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável lida no passo 4. Não esqueça de pular linha;
6. Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, a terceira variável lida no passo 2. Não esqueça de pular linha;
7. Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, a terceira variável lida no passo 3. Não esqueça de pular linha;
8. Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.

## Entrada

A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem uma variável **A** que armazena uma frase de no máximo 100 caracteres. Na segunda linha tem uma variável **B** que armazena uma frase de no máximo 100 caracteres. Na terceira linha tem uma variável **C** que armazena uma frase de no máximo 100 caracteres. Conforme mostrado no exemplo de entrada a seguir.

## Saida

Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas da forma descrita nos itens 5, 6, 7 e 8. Conforme mostra o exemplo de saída a seguir.

## Exemplo 1

**Entrada:**
```
Roberto
Carlos
Aldo
```

**Saida:**
```
RobertoCarlosAldo
CarlosAldoRoberto
AldoRobertoCarlos
RobertoCarlosAldo
```

## Exemplo 2

**Entrada:**
```
aaaa bbbb cccc
cccc
xxxxx xxxx xx
```

**Saida:**
```
aaaa bbbb ccccccccxxxxx xxxx xx
ccccxxxxx xxxx xxaaaa bbbb cccc
xxxxx xxxx xxaaaa bbbb cccccccc
aaaa bbbb ccccxxxxx xxxx
```
