#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm> // remove_if

using namespace std;

bool IsPalindromePermutation(string str)
{
	str.erase(std::remove(str.begin(), str.end(), ' '), str.end());

	if(str.length() < 2)
		return true;

	// guaranting all letters are up/lower case
	for_each(str.begin(), str.end(), [](char &c){
		c = tolower(c);
	});


	unordered_map<char, int> lFH;

	for(char c: str){
		if(lFH.find(c) != lFH.end())
			lFH[c]++;
		else
			lFH[c] = 1;
	}

	bool oddAlreadyFound = false;

	for(const auto& n: lFH){
		//cout << n.first << " : " << n.second << endl;
		if(n.second % 2 != 0){
			if(oddAlreadyFound)
				return false;
			oddAlreadyFound = true;
		}
	}

	return true;
}

int main()
{
	string str;
	getline(cin, str);
	cout << IsPalindromePermutation(str) << endl;

	return 0;
}