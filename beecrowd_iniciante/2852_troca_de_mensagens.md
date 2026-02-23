# 2852 - Troca de Mensagens

**Categoria:** Iniciante
**Assunto:** -
**Nivel:** 5
**Autor:** Por Jessica Dagostini, beecrowd  Brazil
**Timelimit: 1**

---

## Descricao

João e Enzo adoram criptografar as suas mensagens. Para essa criptografia, eles utilizam a técnica da cifra de Vigenère. Essa técnica é bastante semelhante a cifra de Cesar, porém utiliza de diversas "chaves" para cada letra da frase a ser criptografada. A tabela abaixo demonstra o padrão da cifra, consistindo na repetição do alfabeto 26 vezes, onde em cada linha uma letra é deslocada para a esquerda em relação a linha anterior. Essas 26 linhas correspondem às 26 possíveis cifras de César.


![](https://resources.beecrowd.com/gallery/images/contests/UOJ_383_K.png)


Uma palavra aleatória é escolhida como palavra-chave, e cada letra desta palavra vai indicar a linha a ser utilizada para cifrar ou decifrar uma letra da mensagem. Por exemplo:


- O texto a ser criptografado é "ciencia da computacao";
- Definimos como palavra-chave "obi";
- Agora, devemos repetir a palavra-chave tantas vezes forem necessárias até obtermos o comprimento do texto a ser criptografado:
                        - ciencia da computacao
- obiobio bi obiobiobio
- Para realizar a criptografia da primeira letra, devemos encontrar a linha da letra "o" na tabela, e procurar pela coluna da primeira letra da palavra, "c". Para a segunda letra, devemos procurar pela linha "b" coluna "i", e assim por diante, até termos como resultado:
                        - qjmbdqo ei qpudvbodic

Uma vez que realizar a cifragem de todas as palavras das mensagens a serem enviadas é um trabalho bastante custoso, os amigos decidiram que somente irão criptografar as palavras que iniciarem com uma letra consoante. Sendo assim, eles *somente aplicarão a palavra-chave nas palavras que eles irão de fato criptografar*.


Dada uma palavra-chave e um texto de uma mensagem, sua tarefa é criptografar esta mensagem utilizando a cifra de Vigenère mas não esquecendo da regra adicionada por João e Enzo.

## Entrada

A primeira linha contém uma palavra-chave **K** (3 ≤ **K** ≤ 45), que representa a chave para a criptografia. Ela somente é formada pelo alfabeto (a-z) em letras minúsculas, sem espaços. A linha a seguir contém um inteiro **N** (1 ≤ **N** ≤ 150) que indica a quantidade de mensagens a serem criptografadas. As próximas **N** linhas correspondem as mensagens. Estas mensagens não ultrapassam 10^5 caracteres e são compostas pelo alfabeto (a-z) em letras minúsculas e por espaços.

## Saida

A saída deve apresentar a mensagem criptografada, de acordo com a regra dos amigos.

## Exemplo 1

**Entrada:**
```
obi
2
olimpiada brasileira de informatica
ciencia da computacao
```

**Saida:**
```
olimpiada psigjtsjzo em informatica
qjmbdqo ei qpudvbodic
```

## Exemplo 2

**Entrada:**
```
informatica
2
ciencia da computacao
olimpiada brasileira de informatica
```

**Saida:**
```
kvjbtua wi eouczhroah
olimpiada jefgzxebzc dm informatica
```
