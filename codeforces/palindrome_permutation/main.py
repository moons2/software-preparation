'''
Given a string, write a func to check if it is a permutation of
a palindrome. A palindrome is a word of phrase that is the same
fowards and backwards. A permutation is a rearrangement of
letters. The palindrome does not need to be limited to just dictionary words.

IN: Tact Coa
OUT: True {'taco cat', 'atco cta'}
'''
def IsPalindromePermutation(str):
	str = str.replace(' ', '')
	str = str.lower()

	if(len(str) < 2):
		return True

	lFH = {}

	for char in str:
		if(lFH.get(char)):
			lFH[char] += 1
		else:
			lFH[char] = 1

	oddAlreadyFound = False

	for value in lFH.values():
		if(value % 2 != 0):
			if(oddAlreadyFound):
				return False
			oddAlreadyFound = True
	return True



if __name__ == '__main__':
	print(IsPalindromePermutation(str(input())))