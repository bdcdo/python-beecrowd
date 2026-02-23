# 3140 - Copiando e Colando Código

**Categoria:** Iniciante
**Assunto:** Leitura e escrita
**Nivel:** 1
**Autor:** Por Roger Eliodoro Condras, UFSC-ARA  Brazil
**Timelimit: 1**

---

## Descricao

Durante a pandemia, com a suspensão temporária do calendário acadêmico na UFSC, Lucas tem aproveitado o tempo livre para fazer vários cursos online e aprender a usar novas tecnologias e bibliotecas de programação.


Recentemente ele participou de um bootcamp gratuito sobre o uso de Node.js e da biblioteca ReactJS e ficou apaixonado. Ele gostou tanto que ele decidiu portar um site que ele havia criado em HTML para esse novo formato.


Para sorte de Lucas, ele pode reaproveitar boa parte dos scripts em HTML, mas algumas partes deixam de ser necessárias, já que o Node.js e + ReactJS passam a gerá-las automaticamente. Como são vários arquivos para ele analisar e dar control+c, control+v nos códigos, ele gostaria da sua ajuda para agilizar o processo.


Dado um arquivo em HTML, você deve escrever um programa que retorne apenas o conteúdo que esteja entre as tags "<body>" e "</body>", todo resto deve ser ignorado.


Como o Lucas é um cara caprichoso, o código está devidamente indentado. Nas linhas de abertura e fechamento da tag body não há mais nada além da própria tag e os espaços de indentação.

## Entrada

A entrada possuí várias linhas, as linhas do arquivo HTML fornecido pelo Lucas, e termina com EOF. Cada linha consiste em uma sequência de caracteres imprimíveis da Tabela ASCII e é garantido que nenhuma delas possuí mais de 1.000 caracteres ou está em branco.


É garantido que as tags de abertura e fechamento do body, "<body>" e "</body>" respectivamente, aparecem apenas uma vez em todo o arquivo de entrada.

## Saida

Você deve imprimir todas as linhas que estejam entre as tags "<body>" e "</body>" sem incluir elas e mantendo a exata formatação original do arquivo.

## Exemplo

**Entrada:**
```
<html>
<head>
<title>Meu primeiro programa em HTML</title>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
```

**Saida:**
```
<h1>Hello World!</h1>
```
