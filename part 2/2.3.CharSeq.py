str = input()
count  = {}

def char_seq(str):
    max_char_index = 0
    max_char = ''

    for char in str: 
        count[char] = 0

    for char in str:
        count[char] += 1
        
        if count[char] > max_char_index:
            max_char_index = count[char]
            max_char = char
        
    return max_char, max_char_index
char, index = char_seq(str)
print(char, end=' ')
print(index)