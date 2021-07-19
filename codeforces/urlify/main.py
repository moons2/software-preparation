'''
write a method to replace all spaces in a string
with '%20'. You may assume that the string has sufficient space
at the end to hold the additional characters, and that you are given the
'true' length of the string.

in:     'Mr John So    '
out:    'Mr%20John%20So'
'''

# First I would ask the format of the string
# if ASCII or UNICODE, or if I should
# treat this by myself

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    print(string)


def URLify(string):
    # empty string
    if not len(string):
        return

    # a buff of the same length of string
    buff = [' '] * len(string)

    i = n_spaces = 0

    while (i < len(string) and (i + n_spaces*2) < len(string)):
        if (string[i] == ' '):
            buff[i + n_spaces*2:i + n_spaces*2+3] = '%20'
            n_spaces += 1
        else:
            buff[i + n_spaces*2] = string[i]

        i += 1

    print(''.join(buff))



def URLifyV2(string):
    # empty string
    if not len(string):
        return

    # strings are consts in python
    # this way I use a vector here
    strng = list(string)

    new_indx = len(strng)
    lst_indx = 0

    # this for finds the last
    # index with letter in string
    for i in range(len(strng)):
        if strng[i] != ' ':
            lst_indx = i

    for j in range(lst_indx, -1, -1):
        if(strng[j] == ' '):
            strng[new_indx - 3: new_indx] = '%20'
            new_indx -= 3
        else:
            strng[new_indx-1] = strng[j]
            new_indx -= 1

    return strng

if __name__ == '__main__':
    #URLify(str(input()))
    #rlify(list(str(input())), 6)
    print(URLifyV2(str(input())))
