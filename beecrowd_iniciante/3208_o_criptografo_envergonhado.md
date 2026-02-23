# 3208 - O Criptógrafo Envergonhado

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** Por Nils Grimsmo  Noruega
**Timelimit: 3**

---

## Descricao

O jovem e muito promissor criptógrafo Odd Even implementou o módulo de segurança de um grande sistema com milhares de usuários, que já está em uso em sua empresa. As chaves criptográficas são criadas a partir do produto de dois primos e são consideradas seguras porque não existe um método conhecido para fatorar tal produto de forma eficaz.


O que Odd Even não pensou é que os dois fatores em uma chave devem ser grandes, não apenas o produto. Agora é possível que alguns dos usuários do sistema tenham chaves fracas. Em uma tentativa desesperada de não ser demitido, Odd Even analisa secretamente todas as chaves dos usuários, para verificar se são fortes o suficiente. Ele usa seu poderoso Atari e é especialmente cuidadoso ao verificar a chave de seu chefe.

## Entrada

A entrada consiste em não mais do que 20 casos de teste. Cada caso de teste é uma linha com os inteiros 4 ≤ **K** ≤ 10 ^ 100  e 2 ≤ **L** ≤ 10 ^ 6 . **K** é a própria chave, um produto de dois primos. **L** é o tamanho mínimo desejado dos fatores na chave. O conjunto de entrada é encerrado por um caso em que **K** = 0 e **L** = 0.

## Saida

Para cada número **K**, se um de seus fatores for estritamente menor do que o **L** exigido, seu programa deve produzir "BAD **p**" , onde **p** é o menor fator em **K**. Caso contrário, a saída deve ser "GOOD". Os casos devem ser separados por uma quebra de linha.

## Exemplo

**Entrada:**
```
143 10
143 20
667 20
667 30
2573 30
2573 40
0 0
```

**Saida:**
```
GOOD
BAD 11
GOOD
BAD 23
GOOD
BAD 31
```
