'''
implement an algorithm  to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

import time

# RESOLVED BY MYSELF
def byMySelf(string):
	letterFreq = set()

	for letter in string:
		if letterFreq.__contains__(letter):
			return False
		letterFreq.add(letter)
	return True

# RESOLUCAO DO LIVRO

# Primeiramente pergunte ao entrevistador se os caracteres
# São no formato ASCII ou Unicode, pois a forma de tratá-los eh
# diferente e isso demonstra cuidado aos detalhes
# por simplicidade tomaremos o formato ASCII

# depois ums insight aqui é saber a quantidade máxima de caracteres
# e a resposta para essa pergunta é 128 caracteres únicos
# assim se a string tiver mais de 128 caracteres sabemos que
# ha repeticoes

def isUniqueChars(string):
	if len(string) > 128:
		return False

	repeats = [False] * 128

	for letter in string:
		if(repeats[ord(letter)]):
			return False # means there is repetition

		# otherwise
		repeats[ord(letter)] = True
	return True

if __name__ == '__main__':
	stringInputs = ['abcdefghijklmnopqrstuvwxyzz',
	'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZZ',
	'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
	times = []
	for i in range(len(stringInputs)):
		timeBegin = time.perf_counter()
		print(isUniqueChars(stringInputs[i]))
		duration = time.perf_counter() - timeBegin

		print(duration)
		times.append(duration)

	print(min(times))