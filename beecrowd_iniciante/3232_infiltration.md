# 3232 - Infiltration

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** By Unknown  Finland
**Timelimit: 1**

---

## Descricao

Rookie Pirate Captain Jack Albatross has secretly laid anchor in a hidden bay not far from Port Wine, the local meeting point for grizzled pirates and denizens of the sea. Disguising as a messenger, you have infiltrated the service of the dreaded legendary Captain Stevie, and you are entrusted with carrying small encrypted messages between Captain Stevie and his staff of shipmates. Your task is to break the encryption of the messages in aid of young Captain Albatross, giving him a much-needed edge in his quest for peg-legged fame. Fortunately, you (in contrast to Captain Albatross) have been around for a while and you’ve come to know what words to expect in written pirate messages. The following is a table of words having common occurrences:


In a (mixed alphabet) substitution cipher, each letter of the plain text is replaced with another, in this case arbitrary but unique, letter from the alphabet. Given a text encrypted with a substitution cipher and the given set of the twelve known words above, your task is to decode the encrypted text and provide us and Captain Albatross with the plain text. This can be accomplished if and only if there is a unique substitution mapping from the encrypted letters to plain text letters such that


1. a subset **S** of the twelve words show up in the plain text, and
2. the number of different letters in the words in **S** is equal to the number of different letters in the encrypted

                        text.

Note that not all the known words may be present in the plain text and that replacements are not mutual (’a’ being encrypted by ’h’ does NOT necessarily mean that ’h’ is encrypted by ’a’).

## Entrada

A text encrypted by a substitution cipher. The encrypted text is given on one line containing at most 200 characters from the set [’a’-’z’,’ ’]. Only the letters [’a’-’z’] of the plain text are encrypted, the spaces are kept unencrypted.

## Saida

The decrypted plain text if possible, or the string “Impossible” if the text cannot be uniquely decrypted using the set of known words.

## Exemplo 1

**Entrada:**
```
Input Samples
```

**Saida:**
```
Output Samples
```

## Exemplo 2

**Entrada:**
```
ex eoii jpxbmx cvz uxju sjzzcn jzz
```

**Saida:**
```
we will avenge our dead parrot arr
```

## Exemplo 3

**Entrada:**
```
wl jkd
```

**Saida:**
```
Impossible
```

## Exemplo 4

**Entrada:**
```
dyd jkl cs
```

**Saida:**
```
Impossible
```
