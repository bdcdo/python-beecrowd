# 3235 - Luggage

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** By Unknown  Finland
**Timelimit: 1**

---

## Descricao

Johan has a really boring job at the airport. It is his duty to make sure no bags collide when sliding onto the circular conveyor belt in the luggage pick-up zone. All pieces of luggage are loaded onto a straight conveyer belt which ends above the circular conveyor belt. Johan is then manually varying the speed of the straight conveyor so that no collisions occur. He would rather set a constant speed so that he can go to the fika room. There is a sensor at the start of the long conveyor belt so that he can get the positions of all pieces of luggage into his computer. Now all he needs is a program giving him the maximum speed that will avoid all collisions.


The circular conveyor belt moves at a constant speed of 1 m/s. If a piece of luggage is dropped on the circular belt within one meter of the position of an other piece of luggage they may collide, so this should be avoided. Some bags might be picked up on the first round, but you can not know in advance which will be left. The straight conveyor can be set to any speed between 0.1 m/s and 10 m/s.

## Entrada

The first line of input contains two positive integers **N** and **L** (1 ≤ **N** ≤ **L** ≤ 1000), where **N** is the number of pieces of luggage and **L** is the length of the circular conveyor belt in meters. The second line contains **N** unique space-separated numbers **x_i** (0 ≤ **x_i** ≤ 1000) with two digits after the decimal point, denoting luggage positions in meters.

## Saida

Output the maximum speed **v** in m/s (0.1 ≤ **v** ≤ 10) that makes sure no collisions will occur, or “no fika” if there is no such speed. The answer is considered correct if it has an absolute error of at most 10^−9. You may assume that when an optimal **v** exists, each speed in the interval [**v** − 10^−9 , **v**] will also be a valid speed.

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
2 3
0.00 2.00
```

**Saida:**
```
2
```

## Exemplo 3

**Entrada:**
```
3 4
0.05 1.00 3.50
```

**Saida:**
```
0.5
```
