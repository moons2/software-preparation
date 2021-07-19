#include <iostream>         // I/O operations
#include <string>           // chain supply 
#include <unordered_map>    // hash map
#include <unordered_set>    // undordered_set

/*
    implement an algorithm  to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
*/

using namespace std;

bool isUnique(string str);

int main()
{

    string str;

    getline(cin, str);
    isUnique(str) ? cout << "True" : cout << "False";

    return 0;
}

bool isUnique(string str)
{
    int str_size = str.length();

    if (!str_size or str_size > 128)
        return false;
    
    // my hash map who houses <key, value> = <charType, intType>
    // unordered_map<char, int> umap;

    unordered_set<char> char_hash;

    for (char c: str){
        // every letter must enter in this chunk of code
        // only once
        if (char_hash.find(c) == char_hash.end()){
            char_hash.insert(c);
        }
        else // otherwise I know one repetition occured
            return false;
    }

    return true;
}