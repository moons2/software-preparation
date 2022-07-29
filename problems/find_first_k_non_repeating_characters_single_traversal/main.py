'''
Find first `k` non-repeating characters in a string in a single traversal

Given a string, find first k non-repeating characters in it by doing only a single traversal of it.

INPUT:

ABCDBAGHCHFAC and k = 3, 

OUTPUT:

'D', 'G', 'F'.

---

SOLUTION 1:
	uma primeira abordagem seria percorrer a lista de entrada inserindo
	os elementos em um dicionario cuja chave seja a letra e o valor seja
	a contagem de quantas vezes ocorreu. E por fim, percorrer
	a lista mais uma vez imprimindo os k primeiros itens cujo valor
	no dicionário é 1.
	Contudo com isso não seria respeitado a restrição

SOLUTION 2:
	percorremos a lista mapeando os caracteres e suas quantidades e inserindo
	em um dicionario, depois percorremos o dicionario e adicionando
	a uma min heap os itens onde o valor é 1.
	e por ultimo damos um pop no k primeiros elementos.

'''