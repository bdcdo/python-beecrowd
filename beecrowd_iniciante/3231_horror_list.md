# 3231 - Horror List

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** By Unknown  Finland
**Timelimit: 1**

---

## Descricao

It was time for the 7th Nordic Cinema Popcorn Convention, and this year the manager Ian had a brilliant idea. In addition to the traditional film program, there would be a surprise room where a small group of people could stream a random movie from a large collection, while enjoying popcorn and martinis.


However, it turned out that some people were extremely disappointed, because they got to see movies like Ghosts of Mars, which instead caused them to tear out their hair in despair and horror.


To avoid this problem for the next convention, Ian has come up with a solution, but he needs your help to implement it. When the group enters the surprise room, they will type in a list of movies in a computer. This is the so-called horror list, which consists of bad movies that no one in the group would ever like to see. Of course, this list varies from group to group.


You also have access to the database Awesome Comparison of Movies which tells you which movies are directly similar to which. You can assume that movies that are similar to bad movies will be almost as bad. More specificly, we define the Horror index as follows:


\(H1 = \left\{\begin{matrix} 0 & \textrm{if movie is on horror list. This overrides the other definitions.}\\ Q + 1 & \textrm{if the worst directly similar movie has HI = Q}\\ +\infty & \textrm{if not similar at all to a horrible movie} \end{matrix}\right.\)

## Entrada

The first line of input contains three positive integers **N**, **H**, **L** (1 ≤ **H** < **N** ≤ 1000, 0 ≤ **L** ≤ 10000), where **N** is the number of movies (represented by IDs, ranging from 0 to **N** − 1), **H** is the number of movies on the horror list and **L** is the number of similarities in the database.


The second line contains **H** unique space-separated integers **xi** (0 ≤ **x_i** < **N**) denoting the ID of the movies on the horror list.


The following **L** lines contains two space-separated integers **a_i**, **b_i** (0 ≤ **a_i** < **b_i** < **N**), denoting that movie with ID ai is similar to movie with ID **b_i** (and vice verca).

## Saida

Output the ID of the best movie in the collection (highest Horror Index). In case of a tie, output the movie with the lowest ID.

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
6 3 5
0 5 2
0 1
1 2
4 5
3 5
0 2
```

**Saida:**
```
1
```

## Exemplo 3

**Entrada:**
```
6 2 3
5 2
0 5
0 1
3 4
```

**Saida:**
```
3
```
