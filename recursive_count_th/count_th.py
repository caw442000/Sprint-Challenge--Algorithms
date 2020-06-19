'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    substring = 'th'
    length_of_word = len(word)
    length_of_substring = len(substring)
    # check to see if word exist or that it is possible for the string to be in the word
    if length_of_word == 0 or length_of_word < length_of_substring:
        return 0
    # checks to see if the first space up to length of string is equal to substring
    if word[0:length_of_substring] == substring:
        # returns a count of 1 and then sends the a new word down the recursion without the first letter of the word that was
        # originally passed in
        return 1 + count_th(word[1: ])
    else:
        # since it does not equal it sends the a new word down the recursion without the first letter of the word that was
        # originally passed in
        return count_th(word[1: ])
