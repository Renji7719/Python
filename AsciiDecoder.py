import sys

if __name__=='__main__':
	args=sys.argv
	decodedText=''
	decodedList=[]
	encodedText = args[1]
	encodedText=encodedText.replace(' ',',') 
	encodedList=encodedText.split(",")

	for encodedWord in encodedList:
		decodedList.append(chr(int(encodedWord)))

	for decodedWord in decodedList:
		decodedText=decodedText+decodedWord

	print(decodedText)
		
