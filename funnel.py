# -*- coding: utf-8 -*-
# reddit daily programmer challenge 366

# store the words somewhere
first_word = str(input("Enter your first word:"))
second_word = str(input("Enter your second word:"))

print(first_word)
print(second_word)
# determine how much space to explore with the second word
x = (len(first_word))

print(x)

# store each letter as part of a list
# have a function remove each letter in the first list
# continue to compare each list until a match
# once all letters have been removed if no match, then return false

# start removing letters
first_word_manipulated = first_word[0:x-1]
print(first_word_manipulated)

# the compare we want
# is in the right one or should it be ==?
if first_word_manipulated == second_word:
    print('These match')

# continue to remove letters
if first_word_manipulated not in second_word:
    print('These do not match')
