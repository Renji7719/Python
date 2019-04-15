import sys
import subprocess
import re
import os.path

if __name__=='__main__':
	country=''
	ipAddress = open("ipdata.txt","r")
	file=open("country.txt",'w')
	cmd="whois "
	file.write('-----------------------------------------')
	file.write('\n')

	for ip in ipAddress:
		print(ip)
		ip=ip.replace('\n','')
		whoisResult=subprocess.Popen(["whois",ip],stdout=subprocess.PIPE )
		grep=subprocess.Popen(["grep","ountry"],stdin=whoisResult.stdout, stdout=subprocess.PIPE)
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
	
	
	

		
