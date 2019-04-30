import sys,io
import subprocess
import re
import os.path

#victimに対してpostTextの内容をcurlを使ってPostする
def Curl_Victim(victim,postText):
    command = ["curl", "-D","-",victim,"-d",postText]
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #resはバイト列なので、可読な文字列に変換
    sys.stdout.buffer.write(res.stdout)
    return res.stdout

#textPathに存在するテキストを読み込んで、ユーザー名とパスワードを配列に格納してreturnする。
def Output_UserPass(postText):
    #params以前と以降に分離。ゴミをなるべく排除。</string>とUserとPasswordだけにしてUserとPasswordをDictionaryに格納
    tempUsrPss=postText.split('params')
    UsrPss=tempUsrPss[2]
    UsrPss=UsrPss.replace("<name>","")
    UsrPss=UsrPss.replace("</name>","")
    UsrPss=UsrPss.replace("<value>","")
    UsrPss=UsrPss.replace("</value>","")
    UsrPss=UsrPss.replace("<array>","")
    UsrPss=UsrPss.replace("</array>","")
    UsrPss=UsrPss.replace("<data>","")
    UsrPss=UsrPss.replace("</data>","")
    UsrPss=UsrPss.replace("</member>","")
    UsrPss=UsrPss.replace("</struct>","")
    UsrPss=UsrPss.replace("</param>","")
    UsrPss=UsrPss.replace("</params>","")
    UsrPss=UsrPss.replace("</methodcall>","")
    UsrPss=UsrPss.replace("<string>","")
    UsrPss=UsrPss.replace("¥n","")
    UsrPss=UsrPss.replace(" ","")
    #この時点でUserPassにはUser名とPasswordと空白が格納されている
    UserPass=UsrPss.split("</string>")
    del UserPass[2]
    print(UserPass)
    return UserPass
    
    
    

if __name__=='__main__':
    args=sys.argv
    argCount=len(args)
    if(args[1]=="-help"):
        print("Refer to the following format")
        print("python XMLRPC_Check.py \"text file with postData written\"   \"Victim\"")
        quit()
    if(argCount!=3):
        print("Check Format")
        print("python XMLRPC_Check.py \"text file with postData written\"   \"Victim\"")
        quit()
    # すべての内容を読み込む
    allPostData = open(arts[1], "r")
    allContents = allPostData.read()
    allPostData.close()
    #パケット単位でテキストを分ける。
    byPostData=allContents.split("POST")

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
    allPostData.close()

