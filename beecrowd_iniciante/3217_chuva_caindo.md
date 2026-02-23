# 3217 - Chuva Caindo

**Categoria:** Iniciante
**Assunto:** Desconhecido
**Nivel:** 5
**Autor:** Por Mikael Goldmann  Finland
**Timelimit: 1**

---

## Descricao

A precipitação é medida em milímetros. A chuva é coletada em um tubo vertifcal transparente com marcações milimétricas, e uma vez que a chuva para de cair, pode-se verificar a altura da água no tubo.


Em nosso problema, o tubo infelizmente tem um vazamento na altura **L** milímetros (mm). Se o nível da água estiver acima do vazamento, a água é drenada do tubo a uma taxa de **K** milímetros por hora (mm/h).


Queremos saber quanta chuva caiu durante uma determinada precipitação. *Assumimos que o tubo é alto o suficiente para nao transbordar. Também assumimos que a chuva cai a uma taxa uniforme (desconhecida) durante uma precipitação e que a água não evapora do tubo. A altura do vazamento em si também é insignificante.*

## Entrada

A entrada é uma linha com cinco números positivos: ***L K T₁ T₂ H*** onde


**L** é onde está o vazamento (mm)


**K** é a taxa de vazamento de água (mm/h)


**T₁** é a duração da chuva (h)


**T₂** é o tempo entre o final da chuva e a observação do nível da água (h)


**H** é o nível de água no tubo quando o observamos (mm)


Cada número é de pelo menos 0,01 e no máximo 1000,00, e cada um é fornecido com duas casas decimais.

## Saida

Uma linha com dois números de ponto flutuante **F₁ F₂** onde **F₁** é a menor precipitação em milímetros que resultaria na observação dada, e **F₂**é a maior precipitação em milímetros que resultaria na observação dada. Valores com erro absoluto ou relativo menor 10⁻⁶ são aceitáveis.

## Exemplo 1

**Entrada:**
```
80.00 0.50 2.00 1.50 80.00
```

**Saida:**
```
80.000000 80.759403
```

## Exemplo 2

**Entrada:**
```
150.00 1.00 100.00 150.00 100.00
```

**Saida:**
```
100.000000 100.000000
```
