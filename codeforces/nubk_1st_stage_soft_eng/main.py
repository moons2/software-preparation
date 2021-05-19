# src: primeira fase Soft Eng at Nubank
def decode(encodedString):
    reversed_ascii_arr = []

    i = 0
    while(i < len(encodedString)):

        if(32 <= int(encodedString[i: i+2][::-1]) <= 99):
            reversed_ascii_arr.insert(0, chr(int(encodedString[i: i+2][::-1])))
            i += 2
        elif(100 <= int(encodedString[i: i+3][::-1]) <= 122):
            reversed_ascii_arr.insert(0, chr(int(encodedString[i: i+3][::-1])))
            i += 3

    return ''.join(reversed_ascii_arr)

if __name__ == '__main__':
    encodedString = input()

    decoded = decode(encodedString)

    print(decoded)

