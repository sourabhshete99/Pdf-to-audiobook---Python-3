# accept a pdf file and convert it to audio format

import pyttsx3
import PyPDF2

try:
	fil= input('\n Enter name of your PDF file :')
	book=open(fil,'rb')
except:
	print('\n Enter  valid filename or make sure it is the same directory or folder where your this program file is \n')

#	initialize sp variable  with speaker
sp=pyttsx3.init()
rate = sp.getProperty('rate')
#	I've kept the rate of speaking to 150, you may change it from 50 to 300 as per your convenience
sp.setProperty('rate', 150)

#	assign file taken from input to pdfReader
rd=PyPDF2.PdfFileReader(book)
#	count number of pages in file
pages=rd.numPages

#	go through each page and read it
for i in range(0,pages):
	page=rd.getPage(i)
	text=page.extractText()
	sp.say(text)
	sp.runAndWait()

