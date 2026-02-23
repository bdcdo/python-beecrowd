# 3234 - Kindergarten

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** By Unknown  Finland
**Timelimit: 1**

---

## Descricao

Every year the three friendly teachers at the kindergarten let their classes’ kids change classes to form three new ones. Some kids, of course, are old enough to leave, but those who stay for another year are rearranged among the three teachers.


The teachers even let the kids have their say in the process. As friendship both comes and goes hastily in young years, each kid **X** ranks every other kid **Y** according to how glad **X** would be to have **Y** in her new class. In fact, **X** produces a preference list giving a total order of the other kids, i.e. there are no such things as ties – kids she would be equally glad to have as classmates.


The three teachers do not mind if the new classes formed are unbalanced in size, since they fill up their classes with new kids about to start their first year at the kindergarten. They do, however, want all the kids in their own new class to be different from last year since even a teacher needs a break after a whole year with the same kids. They decide that the best partition into three classes under these premises is one where no kid is in the same class as a kid not listed among the top **T** entries on their preference list, for **T** as small as possible. Note that the kids in a new class may very well be the same as in an old one, but then with a new teacher!

## Entrada

The first line of input contains a positive integer **n** ≤ 200 giving the number of kids to be rearranged at the kindergarden. The kids are numbered 1 through **n**.


Then follow **n** lines describing the kids. The **i-th** row first contains the identifier of their current class’ teacher (an integer 0, 1, or 2), and next the **n** − 1 integers {1, 2, 3, ..., **i** − 1, **i** + 1, ..., **n**} in some order, describing the classmate preference list of the **i-th** kid, in descending order.

## Saida

The smallest non-negative integer **T**, such that there is a partitioning of the kids in three new classes such that


• No kid has the same teacher as in their current class, and


• all kids’ classmates are among the top **T** places of their preference lists, respectively.

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
6
0 2 3 4 5 6
0 1 3 4 5 6
1 6 5 4 2 1
2 6 5 3 2 1
1 1 2 3 4 6
2 1 2 3 4 5
```

**Saida:**
```
4
```

## Exemplo 3

**Entrada:**
```
3
0 2 3
1 1 3
2 1 2
```

**Saida:**
```
0
```
