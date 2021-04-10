# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from
# a list. You will be given two inputs a word and an array with words.
#     You should return an array of all the anagrams or an empty array if there are none. For example:
# #anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
# #
# #
# #


from itertools import permutations


def anagrams(word, words):
    result = []
    for el in words:
        perm = list(permutations(word))
        for p in perm:
            p = ''.join(str(i) for i in p)
            if el in p and el not in result and len(el) == len(p):
                result.append(el)
    return result
