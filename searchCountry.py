import sys,io
import subprocess
import re
import os.path

if __name__=='__main__':
	args=sys.argv
	argCount=len(args)
	if(args[1]=="-help"):
		print("refer to the following format")
		print("python searchCountry.py \"text file with ip written\"   \"Output destination text file path\"")
		quit()
	if(argCount!=3):
		print("Check Format")
		print("python searchCountry.py \"text file with ip written\"  \"Output destination text file path\"")
		quit()
	country=''
	ipAddress = open(args[1],"r")
	file=open(args[2],'w')
	cmd="whois "
	file.write('-----------------------------------------')
	file.write('\n')

	for ip in ipAddress:
		print(ip)
		ip=ip.replace('\n','')
		whoisResult=subprocess.Popen(["whois",ip],stdout=subprocess.PIPE )
		grep=subprocess.Popen(["grep","country\|Country\|Organization"],stdin=whoisResult.stdout, stdout=subprocess.PIPE)
		whoisResult.stdout.close()
		country=grep.communicate()[0]
		file.write(ip)
		file.write('\n')
		file.write(country)
		file.write('\n')
		file.write('---------------------------------------------')
		file.write('\n')
	ipAddress.close()
	file.close()	
	
	
	

		
