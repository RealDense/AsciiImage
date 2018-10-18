#!/usr/bin/python

from __future__ import print_function
from PIL import Image
import pickle

fileExt = raw_input('File Extention name ')
fileOut = 'textImg/txIm_' + fileExt + '.txt'

#ascPix = (' ', '.', ',', ';', '!', 'v', 'l', 'L', 'F', 'E', '$')
ascPix = (' ', '.', '~', ',', ';', '!', '+', 'l', 'z', '}', 'y', 'e', '3', 'A', 'H', 'K', 'Q', 'W', '@')

im = Image.open('pics/' + fileExt + '.png')
width, height = im.size

scale = int(input('How much would you like to scale it down? '))

width = int(width/scale)
height = int(height/scale)

with open('asciiGradient', 'rb') as txtIn:
	pixOrder = pickle.load(txtIn)	

#print (pixOrder[4])
#print (len(pixOrder))
#print width
#print height

im = im.convert(mode='L')
#im.show()
im = im.resize((width, height), Image.ANTIALIAS)
#im.show()

pix = (im.getpixel((1,1)))
#print (pix)
#print ("%.3f" % (pix/255.0*10))
#print (int(pix/255.0*10))
#print (ascPix[int(pix/255.0*10)])
textFile = 'textImg/txIm_' + fileExt + '_' + str(scale) + '.txt' 

with open(textFile, 'w+') as out:
	for i in range(0, height, 2):
		if (i > height -2):
			break
		#count = 0
		for j in range(width):
			pix = (im.getpixel((j,i)) + im.getpixel((j, i+1)))/2.0
			index = int(pix/255.0*len(ascPix))
			if (index == len(ascPix)):
				index = index -1
			index2 = len(ascPix) -1 - int(pix/255.0*len(ascPix))
			out.write(ascPix[index2])
				
			#print (index)
			print (ascPix[index], end='')
			#count += 1
	
		out.write('\n')
		print (' ')
