from __future__ import print_function

var = raw_input('> ')

test = "this is a test" + var

with open('testout.txt', 'w') as out:
	for c in test:
		out.write(c)
	out.write('\n')
with open('testout.txt', 'a') as out:
	for c in test:
		out.write(c)
