def longest_word (my_string):
    '''Выводит самое длинное слово  '''
    string_list = my_string.split(' ')
    max = 0
    for word in string_list: 
        if len(word) > max:
            max = len(word)
            longest = word
        elif len(word) == max:
            max = len(word)
            longest = longest + ' '  + word
    return longest

my_word = input('Type any string: ')
longest = longest_word(my_word)
print ('The longest word is: ' + longest)