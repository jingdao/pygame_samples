import itertools
f = open('dictionary.txt','r')
words = set([s.lower() for s in f.read().split('\n')])
print(len(words),'words')

def anagrams(a):
  for w in words:
    if sorted(w)==sorted(a):
      print(w)

def scrabble(a):
	for i in range(1,len(a)):
		for j in itertools.combinations(a, i):
			substring = ''.join(j)
			anagrams(substring)

def morph(A, B, steps):
	previous_frontier = [[A]]
	current_frontier = []
	found = False
	for s in range(steps):
		for l in previous_frontier:
			w1 = l[-1]
			for i in range(len(w1)):
				for j in list(range(ord('a'),ord(w1[i]))) + list(range(ord(w1[i])+1, ord('z')+1)):
					new_word = w1[:i] + chr(j) + w1[i+1:]
					if new_word in words:
						current_frontier.append(l + [new_word])
		previous_frontier = current_frontier
		current_frontier = []
		if found:
			break
	for l in previous_frontier:
		if l[-1]==B:
			print(l)

anagrams('steal')
scrabble('steal')
morph('moon','golf', 4)
morph('wall','door', 5)
