#!/usr/bin/python

from __future__ import print_function
from PIL import Image
from operator import itemgetter
import pickle


asc = ['~','!','@','#','$','%','^','&','*','(',')','_','+','`','1','2','3','4','5','6','7','8','9','0','-','=','Q','W','E','R','T','Y','U','I','O','P','{','}','|','A','S','D','F','G','H','J','K','L',':','"','Z','X','C','V','B','N','M','<','>','?','q','w','e','r','t','y','u','i','o','p','[',']','\\','a','s','d','f','g','h','j','k','l',';',"'",'z','x','c','v','b','n','m',',','.','/']

pixCount = []

im = Image.open('pics/ascii.png')
width, height = im.size

#print (width)

im = im.convert(mode='L')

for char in range (0, width-26, 26):
	count = 0
	for i in range(51):
		for j in range(26):
			#print (i,j, im.getpixel((i,char+j)))
			#print (char)
			if ((im.getpixel((char+j, i))) > 0):
				count += 1
	#asc[char/26].append(count)
	pixCount.append([asc[char/26], count])

pixOrder = sorted(pixCount, key=itemgetter(1))

for pix in pixOrder:
	print ( pix[0], pix[1])

with open('asciiGradient', 'wb') as out:
	pickle.dump(pixOrder, out)		 
