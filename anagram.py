def Anagram(word1, word2):
	dictionary1 = {}
	dictionary2 = {}
	for char in word1:
		dictionary1[char] = dictionary1.get(char, 0) + 1
	for char in word2:
		dictionary2[char] = dictionary2.get(char, 0) + 1

	return dictionary1 == dictionary2

"""
l:1
i:1
s:1
t:1
e:1
n:1

s:1
i:1
l:1
e:1
n:1
t:1

"""